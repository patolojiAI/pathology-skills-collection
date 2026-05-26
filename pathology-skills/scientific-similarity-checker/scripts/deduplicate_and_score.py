#!/usr/bin/env python3
"""
deduplicate_and_score.py
------------------------
Deduplicates article results from multiple databases and computes
a unified similarity profile for each unique article.

Usage:
    python deduplicate_and_score.py --input results.json --target target_abstract.txt

Input JSON format (list of article dicts from any database):
[
  {
    "title": "...",
    "authors": ["Last FM", ...],
    "year": 2023,
    "venue": "Journal Name",
    "doi": "10.xxx/xxx",   # optional
    "pmid": "12345678",    # optional
    "abstract": "...",     # optional
    "source_db": "pubmed"  # which DB returned this
  },
  ...
]
"""

import json
import sys
import re
import argparse
from collections import defaultdict


def normalize_title(title: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    title = title.lower()
    title = re.sub(r'[^\w\s]', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def title_similarity(t1: str, t2: str) -> float:
    """Word-overlap Jaccard similarity between two titles."""
    w1 = set(normalize_title(t1).split())
    w2 = set(normalize_title(t2).split())
    # Remove function words and ubiquitous domain terms from titles
    stops = {
        # function words
        'the', 'a', 'an', 'of', 'in', 'and', 'for', 'on', 'with', 'to',
        'is', 'are', 'was', 'were', 'by', 'from', 'at', 'as', 'via',
        # generic paper-structure words that appear in many titles
        'towards', 'toward', 'using', 'based', 'novel', 'new', 'improved',
        'efficient', 'deep', 'learning', 'neural', 'network', 'approach',
        # medical / clinical generic
        'clinical', 'study', 'analysis', 'detection', 'classification',
        'automated', 'automatic', 'prediction', 'method',
        # imaging generic
        'image', 'images', 'imaging', 'digital', 'pathology', 'histology',
        # AI generic
        'model', 'framework', 'system', 'algorithm',
    }
    w1 -= stops
    w2 -= stops
    if not w1 or not w2:
        return 0.0
    intersection = len(w1 & w2)
    union = len(w1 | w2)
    return intersection / union if union > 0 else 0.0


def abstract_overlap(abs1: str, abs2: str) -> dict:
    """
    Estimate abstract similarity.
    Returns: {
        'word_overlap': float (0-1),
        'shared_phrases': list of str,
        'level': str (Low/Moderate/High/Very High)
    }
    """
    if not abs1 or not abs2:
        return {'word_overlap': 0.0, 'shared_phrases': [], 'level': 'Unknown'}
    
    # Word-level Jaccard
    w1 = set(normalize_title(abs1).split())
    w2 = set(normalize_title(abs2).split())
    stops = (
        # ── English function words ──────────────────────────────────────────
        {'the', 'a', 'an', 'of', 'in', 'and', 'for', 'on', 'with', 'to',
         'is', 'are', 'was', 'were', 'by', 'from', 'at', 'as', 'that',
         'this', 'we', 'our', 'have', 'has', 'been', 'these', 'those',
         'it', 'its', 'which', 'who', 'whom', 'what', 'when', 'where',
         'how', 'be', 'do', 'did', 'does', 'will', 'would', 'could',
         'should', 'may', 'might', 'must', 'shall', 'can', 'not', 'no',
         'nor', 'but', 'or', 'so', 'yet', 'both', 'either', 'each',
         'all', 'any', 'few', 'more', 'most', 'other', 'such', 'than',
         'then', 'too', 'very', 'just', 'also', 'only', 'into', 'about',
         'between', 'through', 'during', 'before', 'after', 'above',
         'below', 'up', 'down', 'out', 'off', 'over', 'under', 'again',
         'further', 'once', 'here', 'there', 'while', 'although',
         'however', 'therefore', 'thus', 'hence', 'whereas', 'since',
         'because', 'whether', 'if', 'unless', 'until', 'among'}
        |
        # ── Generic academic / paper-structure boilerplate ──────────────────
        # These appear in almost every abstract regardless of field and carry
        # zero discriminating information for similarity detection.
        {'study', 'studies', 'results', 'result', 'showed', 'shown', 'show',
         'shows', 'methods', 'method', 'approach', 'approaches', 'technique',
         'techniques', 'conclusion', 'conclusions', 'background', 'objective',
         'objectives', 'purpose', 'aim', 'aims', 'goal', 'goals',
         'introduction', 'discussion', 'abstract', 'paper', 'work', 'works',
         'article', 'report', 'findings', 'finding', 'analysis', 'analyses',
         'propose', 'proposed', 'present', 'presented', 'describe',
         'described', 'introduce', 'introduced', 'demonstrate', 'demonstrated',
         'demonstrates', 'evaluate', 'evaluated', 'evaluation', 'assess',
         'assessed', 'assessment', 'investigate', 'investigated', 'investigation',
         'explore', 'explored', 'examination', 'perform', 'performed',
         'conduct', 'conducted', 'develop', 'developed', 'development',
         'design', 'designed', 'implement', 'implemented', 'implementation',
         'compare', 'compared', 'comparison', 'provide', 'provided',
         'achieve', 'achieved', 'obtain', 'obtained', 'identify',
         'identified', 'use', 'used', 'using', 'based', 'novel', 'new',
         'existing', 'current', 'previous', 'recent', 'state', 'art',
         'well', 'known', 'data', 'dataset', 'datasets', 'set', 'sets',
         'number', 'total', 'large', 'small', 'high', 'low', 'significantly',
         'significant', 'statistical', 'statistically', 'respectively',
         'including', 'included', 'including', 'across', 'within',
         'without', 'compared', 'addition', 'additionally', 'furthermore',
         'moreover', 'therefore', 'overall', 'finally', 'first', 'second',
         'third', 'two', 'three', 'four', 'five', 'multiple', 'several',
         'various', 'different', 'similar', 'same', 'specific', 'general',
         'respectively', 'shown', 'known', 'given', 'important', 'potential',
         'possible', 'likely', 'due', 'per', 'ie', 'eg', 'et', 'al'}
        |
        # ── Artificial Intelligence & Machine Learning ───────────────────────
        # Ubiquitous structural/framing terms that appear in almost every AI
        # abstract and should not drive similarity scores.
        {'neural', 'network', 'networks', 'deep', 'learning', 'machine',
         'model', 'models', 'training', 'trained', 'train', 'testing',
         'test', 'inference', 'input', 'output', 'layer', 'layers',
         'feature', 'features', 'representation', 'representations',
         'classification', 'classify', 'classifier', 'prediction',
         'predictions', 'predict', 'accuracy', 'performance', 'benchmark',
         'benchmarks', 'baseline', 'baselines', 'loss', 'function',
         'optimization', 'optimizer', 'gradient', 'backpropagation',
         'supervised', 'unsupervised', 'semi-supervised', 'self-supervised',
         'generalization', 'overfitting', 'regularization', 'dropout',
         'batch', 'epoch', 'weight', 'weights', 'parameter', 'parameters',
         'architecture', 'architectures', 'convolutional', 'recurrent',
         'lstm', 'gru', 'rnn', 'cnn', 'attention', 'transformer',
         'encoder', 'decoder', 'embedding', 'embeddings', 'latent',
         'space', 'vector', 'vectors', 'dimension', 'dimensions',
         'hidden', 'fully', 'connected', 'pooling', 'activation',
         'relu', 'sigmoid', 'softmax', 'normalization', 'batch',
         'pre-trained', 'pretrained', 'fine-tuned', 'fine-tuning',
         'downstream', 'upstream', 'task', 'tasks', 'end-to-end',
         'state-of-the-art', 'sota', 'outperform', 'outperforms',
         'surpass', 'improve', 'improves', 'improvement', 'gain',
         'objective', 'loss', 'cross-entropy', 'multimodal', 'unimodal',
         'generative', 'discriminative', 'adversarial', 'gan',
         'variational', 'autoencoder', 'backbone', 'head', 'branch',
         'token', 'tokens', 'sequence', 'sequences', 'context',
         'query', 'key', 'value', 'multi-head', 'self-attention',
         'scale', 'scaled', 'position', 'positional', 'augmentation',
         'data', 'dataset', 'training', 'validation', 'test',
         'split', 'fold', 'cross-validation', 'hyperparameter',
         'grid', 'search', 'random', 'seed', 'experiment', 'experiments',
         'ablation', 'sensitivity', 'robustness', 'efficient', 'efficiency',
         'fast', 'faster', 'slow', 'real-time', 'lightweight',
         'compute', 'computation', 'computational', 'gpu', 'cpu', 'memory',
         'throughput', 'latency', 'parallel', 'parallelizable',
         'knowledge', 'transfer', 'distillation', 'graph', 'node',
         'edge', 'point', 'cloud', 'patch', 'patches', 'window',
         'sliding', 'stride', 'kernel', 'filter', 'map', 'maps',
         'detection', 'segmentation', 'recognition', 'localization',
         'generation', 'synthesis', 'reconstruction', 'sampling'}
        |
        # ── Natural Language Processing ──────────────────────────────────────
        {'language', 'text', 'sentence', 'sentences', 'word', 'words',
         'token', 'tokens', 'vocabulary', 'corpus', 'document', 'documents',
         'translation', 'machine', 'natural', 'processing', 'understanding',
         'generation', 'summarization', 'question', 'answering', 'reading',
         'comprehension', 'entailment', 'semantic', 'syntactic', 'parsing',
         'tagging', 'named', 'entity', 'relation', 'extraction',
         'sentiment', 'dialogue', 'conversation', 'chat', 'prompt',
         'instruction', 'fine-tune', 'bleu', 'rouge', 'perplexity',
         'encoder-decoder', 'sequence-to-sequence', 'seq2seq', 'transduction',
         'alignment', 'cross-lingual', 'multilingual', 'monolingual',
         'source', 'target', 'source-target'}
        |
        # ── Medical / Clinical ───────────────────────────────────────────────
        # Terms common to nearly all medical abstracts; not field-specific
        # enough to be meaningful similarity signals.
        {'patient', 'patients', 'clinical', 'hospital', 'cohort',
         'retrospective', 'prospective', 'randomized', 'controlled',
         'trial', 'trials', 'group', 'groups', 'control', 'intervention',
         'treatment', 'treatments', 'therapy', 'therapies', 'therapeutic',
         'outcome', 'outcomes', 'endpoint', 'endpoints', 'follow-up',
         'follow', 'months', 'years', 'diagnosis', 'diagnostic',
         'prognosis', 'prognostic', 'survival', 'mortality', 'morbidity',
         'incidence', 'prevalence', 'risk', 'factor', 'factors',
         'association', 'associations', 'correlation', 'correlations',
         'sensitivity', 'specificity', 'positive', 'negative', 'predictive',
         'value', 'area', 'under', 'curve', 'auc', 'roc', 'confidence',
         'interval', 'odds', 'ratio', 'hazard', 'relative', 'absolute',
         'mean', 'median', 'standard', 'deviation', 'interquartile',
         'range', 'proportion', 'rate', 'rates', 'increase', 'decrease',
         'reduction', 'improvement', 'response', 'remission', 'recurrence',
         'adverse', 'events', 'effect', 'effects', 'safety', 'efficacy',
         'tolerability', 'dose', 'dosage', 'regimen', 'protocol',
         'surgery', 'surgical', 'resection', 'biopsy', 'specimen',
         'sample', 'samples', 'case', 'cases', 'review', 'literature',
         'systematic', 'meta-analysis', 'evidence', 'guideline',
         'guidelines', 'criteria', 'inclusion', 'exclusion', 'consent',
         'ethics', 'ethical', 'approval', 'irb', 'informed', 'written',
         'age', 'sex', 'gender', 'male', 'female', 'median', 'range',
         'laboratory', 'blood', 'serum', 'tissue', 'cell', 'cells',
         'expression', 'mutation', 'variant', 'gene', 'protein',
         'biomarker', 'biomarkers', 'molecular', 'immunohistochemistry'}
        |
        # ── Pathology (general, surgical, molecular) ─────────────────────────
        {'pathology', 'pathological', 'histology', 'histological',
         'histopathology', 'morphology', 'morphological', 'grade',
         'grading', 'stage', 'staging', 'carcinoma', 'adenocarcinoma',
         'tumor', 'tumour', 'tumors', 'tumours', 'lesion', 'lesions',
         'benign', 'malignant', 'malignancy', 'neoplasm', 'neoplasms',
         'slide', 'slides', 'section', 'sections', 'stain', 'staining',
         'hematoxylin', 'eosin', 'immunostaining', 'ihc', 'ki67',
         'mitosis', 'mitotic', 'necrosis', 'invasion', 'invasive',
         'margin', 'margins', 'lymph', 'node', 'nodes', 'metastasis',
         'metastatic', 'primary', 'secondary', 'specimen', 'specimens',
         'resection', 'excision', 'core', 'needle', 'paraffin',
         'frozen', 'formalin', 'fixed', 'ffpe', 'tissue', 'microarray',
         'tma', 'whole', 'wsi', 'field', 'view', 'region', 'interest',
         'roi', 'annotation', 'annotations', 'annotated', 'annotator',
         'pathologist', 'pathologists', 'expert', 'experts', 'agreement',
         'inter-observer', 'intra-observer', 'variability', 'concordance',
         'diagnosis', 'diagnoses', 'report', 'reporting', 'automated',
         'automation', 'computer-aided', 'cad', 'detection', 'classification',
         'grading', 'scoring', 'quantification', 'quantitative',
         'nuclear', 'cytoplasm', 'gland', 'glands', 'duct', 'stroma',
         'stromal', 'epithelial', 'epithelium', 'lymphocyte', 'inflammatory'}
        |
        # ── Digital Pathology ────────────────────────────────────────────────
        {'digital', 'whole-slide', 'whole', 'image', 'images', 'imaging',
         'scanner', 'scanning', 'magnification', 'resolution', 'pixel',
         'pixels', 'patch', 'patches', 'tiling', 'tile', 'tiles',
         'gigapixel', 'multiresolution', 'pyramid', 'level', 'levels',
         'weak', 'weakly', 'supervised', 'label', 'labels', 'labeled',
         'labelled', 'bag', 'bags', 'mil', 'multiple', 'instance',
         'aggregation', 'attention-based', 'pooling', 'slide-level',
         'patient-level', 'region-level', 'cell-level', 'nucleus',
         'nuclei', 'segmentation', 'detection', 'counting', 'density',
         'spatial', 'texture', 'color', 'colour', 'channel', 'channels',
         'rgb', 'hsv', 'normalization', 'stain', 'color-normalization',
         'augmentation', 'preprocessing', 'artifact', 'artifacts',
         'focus', 'blur', 'quality', 'control', 'qc', 'openslide',
         'qupath', 'imagej', 'pathml', 'pathomics', 'computationally',
         'computational', 'virtual', 'slide', 'cohort', 'multi-site',
         'external', 'internal', 'validation', 'generalization',
         'retrospective', 'collected', 'scanned', 'available',
         'publicly', 'released', 'tcga', 'camelyon', 'challenge',
         'competition', 'benchmark'}
        |
        # ── Image Analysis & Computer Vision ────────────────────────────────
        {'image', 'images', 'visual', 'vision', 'pixel', 'pixels',
         'object', 'objects', 'detection', 'segmentation', 'recognition',
         'classification', 'localization', 'tracking', 'pose', 'depth',
         'stereo', '2d', '3d', 'volume', 'volumetric', 'voxel', 'voxels',
         'scan', 'scans', 'ct', 'mri', 'pet', 'ultrasound', 'xray',
         'x-ray', 'radiograph', 'radiographic', 'radiology', 'radiological',
         'modality', 'modalities', 'multimodal', 'cross-modal',
         'preprocessing', 'postprocessing', 'pipeline', 'pipelines',
         'framework', 'frameworks', 'end-to-end', 'fully', 'automatic',
         'automated', 'semi-automatic', 'manual', 'bounding', 'box',
         'mask', 'masks', 'label', 'labels', 'ground', 'truth',
         'annotation', 'inter-rater', 'dice', 'iou', 'jaccard', 'f1',
         'precision', 'recall', 'accuracy', 'hausdorff', 'distance',
         'average', 'mean', 'texture', 'shape', 'appearance', 'intensity',
         'contrast', 'gradient', 'edge', 'boundary', 'region', 'area',
         'scale', 'multi-scale', 'resolution', 'upsampling', 'downsampling',
         'encoder', 'decoder', 'skip', 'connection', 'unet', 'resnet',
         'vgg', 'inception', 'densenet', 'efficientnet', 'vit',
         'pretrained', 'imagenet', 'transfer', 'learning', 'finetune'}
    )
    w1 -= stops
    w2 -= stops
    if not w1 or not w2:
        return {'word_overlap': 0.0, 'shared_phrases': [], 'level': 'Unknown'}
    
    overlap_ratio = len(w1 & w2) / min(len(w1), len(w2))
    
    # Find shared n-grams (n=5)
    def get_ngrams(text, n=5):
        words = normalize_title(text).split()
        return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    
    ngrams1 = set(get_ngrams(abs1))
    ngrams2 = set(get_ngrams(abs2))
    shared = list(ngrams1 & ngrams2)[:5]  # top 5
    
    # Classify level
    if overlap_ratio >= 0.70:
        level = 'Very High'
    elif overlap_ratio >= 0.45:
        level = 'High'
    elif overlap_ratio >= 0.25:
        level = 'Moderate'
    else:
        level = 'Low'
    
    return {
        'word_overlap': round(overlap_ratio, 3),
        'shared_phrases': shared,
        'level': level
    }


def author_overlap(authors1: list, authors2: list) -> dict:
    """
    Compare author lists.
    Returns: {'count': int, 'names': list, 'ratio': float, 'pattern': str}
    """
    def normalize_author(a: str) -> str:
        return a.lower().strip().replace('.', '')
    
    set1 = {normalize_author(a) for a in authors1}
    set2 = {normalize_author(a) for a in authors2}
    shared = set1 & set2
    
    ratio = len(shared) / min(len(set1), len(set2)) if min(len(set1), len(set2)) > 0 else 0.0
    
    if ratio >= 0.9:
        pattern = 'Identical authorship'
    elif ratio >= 0.6:
        pattern = 'Substantial overlap'
    elif ratio >= 0.3:
        pattern = 'Partial overlap'
    else:
        pattern = 'Minimal or no overlap'
    
    # Check first/last author
    f1 = normalize_author(authors1[0]) if authors1 else ''
    f2 = normalize_author(authors2[0]) if authors2 else ''
    l1 = normalize_author(authors1[-1]) if authors1 else ''
    l2 = normalize_author(authors2[-1]) if authors2 else ''
    
    notes = []
    if f1 and f1 == f2:
        notes.append('same first author')
    if l1 and l1 == l2 and l1 != f1:
        notes.append('same last author')
    
    return {
        'count': len(shared),
        'ratio': round(ratio, 3),
        'pattern': pattern,
        'notes': notes,
        'shared_names': list(shared)[:5]
    }


def assess_misconduct_risk(title_sim: float, abstract_info: dict,
                            author_info: dict, year_diff: int) -> dict:
    """
    Combine signals into a misconduct risk assessment.
    Returns: {'level': str, 'flags': list, 'color': str}
    """
    flags = []
    level = 'GREEN'
    
    abs_level = abstract_info.get('level', 'Unknown')
    abs_overlap = abstract_info.get('word_overlap', 0.0)
    author_ratio = author_info.get('ratio', 0.0)
    author_pattern = author_info.get('pattern', '')
    
    # RED FLAG conditions
    if abs_level == 'Very High' and author_ratio >= 0.5:
        flags.append('🔴 Very high abstract similarity + substantial author overlap → likely duplicate publication')
        level = 'RED'
    
    if title_sim >= 0.90 and author_ratio >= 0.5:
        flags.append('🔴 Near-identical title with same author group → possible verbatim duplicate')
        level = 'RED'
    
    # AMBER conditions
    if abs_level in ('High', 'Very High') and author_ratio >= 0.3 and level != 'RED':
        flags.append('🟡 High abstract similarity with author overlap → investigate for self-plagiarism or duplicate')
        level = 'AMBER'
    
    if title_sim >= 0.75 and abs_overlap >= 0.40 and level not in ('RED',):
        flags.append('🟡 Very similar title and high word overlap in abstract')
        if level == 'GREEN':
            level = 'AMBER'
    
    if abs_level == 'High' and author_ratio == 0.0 and level not in ('RED', 'AMBER'):
        flags.append('🟡 High abstract similarity from different authors — check for plagiarism of others\' work')
        level = 'AMBER'
    
    # Normal patterns
    if abs_level in ('Low', 'Moderate') and author_ratio >= 0.5:
        flags.append('🟢 Same author group, related topic — consistent with a research program')
    
    if not flags:
        flags.append('✅ No significant similarity signals detected')
    
    color_map = {'RED': '🔴', 'AMBER': '🟡', 'GREEN': '🟢'}
    return {
        'level': level,
        'color': color_map.get(level, '✅'),
        'flags': flags
    }


def deduplicate(articles: list) -> list:
    """
    Merge articles that appear to be the same paper across databases.
    Uses DOI as primary key, then title similarity as fallback.
    """
    unique = []
    doi_map = {}
    
    for art in articles:
        doi = art.get('doi', '').strip().lower()
        title = art.get('title', '')
        
        # Try DOI match first
        if doi:
            if doi in doi_map:
                # Merge source_db info
                idx = doi_map[doi]
                existing_sources = unique[idx].get('source_dbs', [unique[idx].get('source_db', '')])
                new_source = art.get('source_db', '')
                if new_source not in existing_sources:
                    existing_sources.append(new_source)
                unique[idx]['source_dbs'] = existing_sources
                # Fill in missing abstract
                if not unique[idx].get('abstract') and art.get('abstract'):
                    unique[idx]['abstract'] = art['abstract']
                continue
            else:
                doi_map[doi] = len(unique)
                art['source_dbs'] = [art.get('source_db', 'unknown')]
                unique.append(art)
                continue
        
        # No DOI: check title similarity against existing entries
        merged = False
        for i, existing in enumerate(unique):
            sim = title_similarity(title, existing.get('title', ''))
            if sim >= 0.85:
                # Likely same paper
                existing_sources = unique[i].get('source_dbs', [unique[i].get('source_db', '')])
                new_source = art.get('source_db', '')
                if new_source not in existing_sources:
                    existing_sources.append(new_source)
                unique[i]['source_dbs'] = existing_sources
                if not unique[i].get('abstract') and art.get('abstract'):
                    unique[i]['abstract'] = art['abstract']
                merged = True
                break
        
        if not merged:
            art['source_dbs'] = [art.get('source_db', 'unknown')]
            unique.append(art)
    
    return unique


def score_articles(target: dict, candidates: list) -> list:
    """
    Score all candidate articles against the target.
    Returns sorted list (highest risk first, then highest similarity).
    """
    scored = []
    target_authors = target.get('authors', [])
    target_abstract = target.get('abstract', '')
    target_title = target.get('title', '')
    target_year = target.get('year', 0)
    
    for art in candidates:
        t_sim = title_similarity(target_title, art.get('title', ''))
        abs_info = abstract_overlap(target_abstract, art.get('abstract', ''))
        auth_info = author_overlap(target_authors, art.get('authors', []))
        year_diff = abs((target_year or 0) - (art.get('year') or 0))
        risk = assess_misconduct_risk(t_sim, abs_info, auth_info, year_diff)
        
        art['_scores'] = {
            'title_similarity': round(t_sim, 3),
            'abstract': abs_info,
            'authors': auth_info,
            'year_diff': year_diff,
            'risk': risk
        }
        scored.append(art)
    
    # Sort: RED first, then AMBER, then by abstract overlap descending
    level_order = {'RED': 0, 'AMBER': 1, 'GREEN': 2}
    scored.sort(key=lambda x: (
        level_order.get(x['_scores']['risk']['level'], 3),
        -x['_scores']['abstract'].get('word_overlap', 0)
    ))
    
    return scored


def format_report_section(scored_articles: list, max_show: int = 10) -> str:
    """Format the scored articles into a readable report section."""
    lines = []
    for i, art in enumerate(scored_articles[:max_show], 1):
        s = art.get('_scores', {})
        risk = s.get('risk', {})
        abs_info = s.get('abstract', {})
        auth_info = s.get('authors', {})
        
        lines.append(f"\n### {i}. {art.get('title', 'Unknown Title')}")
        
        meta = []
        if art.get('authors'):
            meta.append(', '.join(art['authors'][:3]) + (' et al.' if len(art['authors']) > 3 else ''))
        if art.get('venue'):
            meta.append(art['venue'])
        if art.get('year'):
            meta.append(str(art['year']))
        if art.get('doi'):
            meta.append(f"DOI: {art['doi']}")
        if meta:
            lines.append('   ' + ' | '.join(meta))
        
        lines.append(f"   **Sources**: {', '.join(art.get('source_dbs', ['unknown']))}")
        lines.append(f"   **Title similarity**: {s.get('title_similarity', 0):.0%}")
        lines.append(f"   **Abstract overlap**: {abs_info.get('level', 'N/A')} ({abs_info.get('word_overlap', 0):.0%})")
        lines.append(f"   **Author overlap**: {auth_info.get('pattern', 'N/A')}")
        
        for flag in risk.get('flags', []):
            lines.append(f"   {flag}")
        
        if abs_info.get('shared_phrases'):
            lines.append(f"   **Shared phrases**: {' / '.join(abs_info['shared_phrases'][:2])}")
    
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deduplicate and score scientific article results')
    parser.add_argument('--input', required=True, help='JSON file with list of retrieved articles')
    parser.add_argument('--target', required=True, help='JSON file with target article metadata')
    parser.add_argument('--output', default='scored_results.json', help='Output file')
    args = parser.parse_args()
    
    with open(args.input) as f:
        raw_articles = json.load(f)
    
    with open(args.target) as f:
        target = json.load(f)
    
    print(f"Input: {len(raw_articles)} articles from various databases")
    deduped = deduplicate(raw_articles)
    print(f"After deduplication: {len(deduped)} unique articles")
    
    scored = score_articles(target, deduped)
    
    with open(args.output, 'w') as f:
        json.dump(scored, f, indent=2, default=str)
    
    print(f"\nTop results:")
    print(format_report_section(scored, max_show=5))
    print(f"\nFull scored results saved to: {args.output}")
