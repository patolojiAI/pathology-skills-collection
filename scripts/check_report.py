#!/usr/bin/env python3
"""
Single Pathology Report Checker

Analyzes a single pathology report against CAP/ICCR guidelines using either
Claude API or a local LLM via Ollama/LM Studio.

Usage:
    # With Claude (default)
    python check_report.py "Check this breast report" < report.txt
    python check_report.py --file report.txt "Check for CAP compliance"

    # With Ollama (local, private)
    python check_report.py --provider ollama "Check this report" < report.txt
    python check_report.py --provider ollama --model llama3.1:70b --file report.txt

    # With LM Studio (local, private)
    python check_report.py --provider lmstudio "Check this report" < report.txt
    python check_report.py --provider lmstudio --model "qwen2.5-3b-instruct" < report.txt

    # List available models
    python check_report.py --provider lmstudio --list-models
    python check_report.py --provider ollama --list-models

    # Output to file
    python check_report.py "Check compliance" < report.txt > result.txt

Arguments:
    prompt              The instruction/prompt for analysis
    --file, -f          Path to report file (alternative to stdin)
    --provider, -p      LLM provider: 'anthropic' (default), 'ollama', or 'lmstudio'
    --model, -m         Model name (auto-detected if not specified for local providers)
    --list-models       List available models for the selected provider and exit
    --ollama-url        Ollama API base URL (default: http://localhost:11434/v1)
    --lmstudio-url      LM Studio API base URL (default: http://localhost:1234/v1)
    --tumor-type        Tumor type hint: breast, colorectal, pancreas, gastric
    --json              Output raw JSON instead of formatted text
    --quiet, -q         Suppress progress messages (only output result)

Environment:
    ANTHROPIC_API_KEY   Required for Claude provider
    LLM_PROVIDER        Default provider (anthropic/ollama/lmstudio)
    OLLAMA_MODEL        Default Ollama model
    OLLAMA_URL          Default Ollama URL
    LMSTUDIO_URL        Default LM Studio URL
    LMSTUDIO_MODEL      Default LM Studio model
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, Any, List

# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-20250514"
DEFAULT_OLLAMA_MODEL = "llama3.1:70b"
DEFAULT_OLLAMA_URL = "http://localhost:11434/v1"
DEFAULT_LMSTUDIO_URL = "http://localhost:1234/v1"


# ============================================================================
# MODEL DISCOVERY
# ============================================================================

def list_available_models(base_url: str, provider: str, quiet: bool = False) -> List[str]:
    """Query the /v1/models endpoint to list available models."""
    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package not installed.", file=sys.stderr)
        print("Install with: pip install openai", file=sys.stderr)
        sys.exit(1)

    try:
        client = OpenAI(base_url=base_url, api_key="not-needed")
        models_response = client.models.list()
        model_ids = [m.id for m in models_response.data]
        return model_ids
    except Exception as e:
        if not quiet:
            print(f"Warning: Could not list models from {base_url}: {e}", file=sys.stderr)
        return []


def auto_select_model(base_url: str, provider: str, quiet: bool = False) -> Optional[str]:
    """Auto-detect and select a model from the local server.

    Returns the model ID if exactly one model is loaded,
    prompts the user to choose if multiple are available,
    or returns None if no models are found.
    """
    models = list_available_models(base_url, provider, quiet)

    if not models:
        return None

    if len(models) == 1:
        if not quiet:
            print(f"Auto-detected model: {models[0]}", file=sys.stderr)
        return models[0]

    # Multiple models available
    if not quiet:
        print(f"\nMultiple models available in {provider}:", file=sys.stderr)
        for i, model_id in enumerate(models, 1):
            print(f"  {i}. {model_id}", file=sys.stderr)
        print(f"\nUsing first available model: {models[0]}", file=sys.stderr)
        print(f"Tip: Use -m <model-name> to select a specific model.\n", file=sys.stderr)

    return models[0]


# ============================================================================
# REFERENCE FILE LOADING
# ============================================================================

def get_skill_dir() -> Path:
    """Get the skill directory (parent of scripts/)."""
    return Path(__file__).parent.parent


def load_skill_file() -> str:
    """Load the main SKILL.md file."""
    skill_path = get_skill_dir() / "SKILL.md"
    if skill_path.exists():
        return skill_path.read_text(encoding="utf-8")
    return ""


def load_reference_file(tumor_type: str) -> str:
    """Load the appropriate reference file for the tumor type."""
    reference_map = {
        "pancreas": "diagnosis/exocrine_pancreas.md",
        "breast": "diagnosis/breast_invasive_carcinoma.md",
        "colorectal": "diagnosis/colorectal_resection.md",
        "gastric": "diagnosis/gastric_carcinoma.md",
        "stomach": "diagnosis/gastric_carcinoma.md",
    }

    filename = reference_map.get(tumor_type.lower() if tumor_type else "")
    if not filename:
        # Load all reference files if tumor type not specified
        refs = []
        ref_dir = get_skill_dir() / "references" / "diagnosis"
        if ref_dir.exists():
            for ref_file in ref_dir.glob("*.md"):
                refs.append(f"# {ref_file.stem}\n\n{ref_file.read_text(encoding='utf-8')}")
        return "\n\n---\n\n".join(refs)

    ref_path = get_skill_dir() / "references" / filename
    if ref_path.exists():
        return ref_path.read_text(encoding="utf-8")
    return ""


def load_staging_reference() -> str:
    """Load the TNM stage calculator reference file."""
    staging_path = get_skill_dir() / "references" / "staging" / "tnm_stage_calculator.md"
    if staging_path.exists():
        return staging_path.read_text(encoding="utf-8")
    return ""


# ============================================================================
# PROMPT TEMPLATE
# ============================================================================

ANALYSIS_PROMPT = """You are a pathology report compliance checker. Analyze the following surgical pathology cancer report against CAP (College of American Pathologists) and ICCR (International Collaboration on Cancer Reporting) guidelines.

<skill_instructions>
{skill_content}
</skill_instructions>

<reference_guidelines>
{reference_content}
</reference_guidelines>

<staging_reference>
{staging_content}
</staging_reference>

<pathology_report>
{report_text}
</pathology_report>

<user_instruction>
{user_prompt}
</user_instruction>

Analyze this report following the user's instruction. Provide a comprehensive response that includes:

1. **Compliance Assessment**: Score (0-100) and status
2. **Missing Elements**: List any critical, major, or minor gaps
3. **Present Elements**: Key findings extracted from the report
4. **Cross-Validation**: Check pT vs size, pN vs node count, margins vs R classification
5. **Staging Verification**: Compare reported stage with calculated stage (AJCC 8th)
6. **Quality Metrics**: Completeness, clarity, consistency scores
7. **Summary**: Brief narrative of findings and recommendations

Respond in the same language as the pathology report (English or Turkish).
"""


# ============================================================================
# LLM CLIENTS
# ============================================================================

def create_anthropic_client():
    """Create Anthropic client."""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package not installed.", file=sys.stderr)
        print("Install with: pip install anthropic", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    return anthropic.Anthropic(api_key=api_key)


def create_openai_compatible_client(base_url: str):
    """Create OpenAI-compatible client for Ollama or LM Studio."""
    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package not installed.", file=sys.stderr)
        print("Install with: pip install openai", file=sys.stderr)
        sys.exit(1)

    return OpenAI(base_url=base_url, api_key="not-needed")


def call_anthropic(client, model: str, prompt: str, quiet: bool = False) -> str:
    """Call Anthropic API."""
    if not quiet:
        print(f"Analyzing with {model}...", file=sys.stderr)

    response = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def call_local_llm(client, model: str, prompt: str, quiet: bool = False) -> str:
    """Call local LLM via OpenAI-compatible API (Ollama or LM Studio)."""
    if not quiet:
        print(f"Analyzing with {model} (local)...", file=sys.stderr)

    response = client.chat.completions.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ============================================================================
# MAIN ANALYSIS
# ============================================================================

def analyze_report(
        report_text: str,
        user_prompt: str,
        provider: str = "anthropic",
        model: Optional[str] = None,
        ollama_url: str = DEFAULT_OLLAMA_URL,
        lmstudio_url: str = DEFAULT_LMSTUDIO_URL,
        tumor_type: Optional[str] = None,
        quiet: bool = False
) -> str:
    """Analyze a pathology report using the specified provider."""

    # Load skill and references
    if not quiet:
        print("Loading skill and references...", file=sys.stderr)

    skill_content = load_skill_file()
    reference_content = load_reference_file(tumor_type)
    staging_content = load_staging_reference()

    if not skill_content:
        print("Warning: SKILL.md not found", file=sys.stderr)

    # Build prompt
    full_prompt = ANALYSIS_PROMPT.format(
        skill_content=skill_content,
        reference_content=reference_content,
        staging_content=staging_content,
        report_text=report_text,
        user_prompt=user_prompt
    )

    # Call LLM
    if provider == "anthropic":
        client = create_anthropic_client()
        model = model or DEFAULT_ANTHROPIC_MODEL
        return call_anthropic(client, model, full_prompt, quiet)

    elif provider == "ollama":
        client = create_openai_compatible_client(ollama_url)
        if not model:
            model = auto_select_model(ollama_url, provider, quiet) or DEFAULT_OLLAMA_MODEL
        return call_local_llm(client, model, full_prompt, quiet)

    elif provider == "lmstudio":
        client = create_openai_compatible_client(lmstudio_url)
        if not model:
            model = auto_select_model(lmstudio_url, provider, quiet)
            if not model:
                print("Error: No models loaded in LM Studio.", file=sys.stderr)
                print("Open LM Studio → Local Server tab → Load a model → Start Server", file=sys.stderr)
                sys.exit(1)
        return call_local_llm(client, model, full_prompt, quiet)

    else:
        print(f"Error: Unknown provider '{provider}'", file=sys.stderr)
        sys.exit(1)


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Analyze a pathology report against CAP/ICCR guidelines",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check report with Claude (requires ANTHROPIC_API_KEY)
  python check_report.py "Check this breast report for compliance" < report.txt

  # Check report with local Ollama
  python check_report.py --provider ollama "Check for CAP compliance" < report.txt

  # Check report with LM Studio
  python check_report.py --provider lmstudio "Check for CAP compliance" < report.txt

  # List available models
  python check_report.py --provider lmstudio --list-models
  python check_report.py --provider ollama --list-models

  # Specify model explicitly
  python check_report.py -p lmstudio -m "qwen2.5-3b-instruct" < report.txt

  # Specify model and output to file
  python check_report.py -p ollama -m qwen2.5:32b --file report.txt > result.txt

  # Generate synoptic template
  python check_report.py "Generate CAP synoptic template" < report.txt

  # Quiet mode (only output, no progress messages)
  python check_report.py -q "Check compliance" < report.txt
"""
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        default="Check this pathology report for CAP/ICCR compliance and identify any missing or incomplete elements.",
        help="Instruction/prompt for analysis"
    )

    parser.add_argument(
        "--file", "-f",
        type=str,
        help="Path to report file (alternative to stdin)"
    )

    parser.add_argument(
        "--provider", "-p",
        type=str,
        default=os.environ.get("LLM_PROVIDER", "anthropic"),
        choices=["anthropic", "ollama", "lmstudio"],
        help="LLM provider (default: anthropic, or LLM_PROVIDER env var)"
    )

    parser.add_argument(
        "--model", "-m",
        type=str,
        default=os.environ.get("OLLAMA_MODEL") or os.environ.get("LMSTUDIO_MODEL"),
        help="Model name (auto-detected from server if not specified for local providers)"
    )

    parser.add_argument(
        "--list-models",
        action="store_true",
        help="List available models for the selected provider and exit"
    )

    parser.add_argument(
        "--ollama-url",
        type=str,
        default=os.environ.get("OLLAMA_URL", DEFAULT_OLLAMA_URL),
        help=f"Ollama API base URL (default: {DEFAULT_OLLAMA_URL})"
    )

    parser.add_argument(
        "--lmstudio-url",
        type=str,
        default=os.environ.get("LMSTUDIO_URL", DEFAULT_LMSTUDIO_URL),
        help=f"LM Studio API base URL (default: {DEFAULT_LMSTUDIO_URL})"
    )

    parser.add_argument(
        "--tumor-type", "-t",
        type=str,
        choices=["breast", "colorectal", "pancreas", "gastric"],
        help="Tumor type hint (auto-detected if not specified)"
    )

    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Request JSON output format"
    )

    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress messages"
    )

    args = parser.parse_args()

    # Handle --list-models
    if args.list_models:
        if args.provider == "anthropic":
            print("Model listing not supported for Anthropic. Available models:")
            print(f"  {DEFAULT_ANTHROPIC_MODEL}")
            sys.exit(0)

        base_url = args.lmstudio_url if args.provider == "lmstudio" else args.ollama_url
        models = list_available_models(base_url, args.provider)

        if not models:
            print(f"No models found. Is {args.provider} running?", file=sys.stderr)
            if args.provider == "ollama":
                print("Start with: ollama serve", file=sys.stderr)
            else:
                print("Open LM Studio → Local Server → Load a model → Start Server", file=sys.stderr)
            sys.exit(1)

        print(f"Available models ({args.provider}):")
        for model_id in models:
            print(f"  {model_id}")
        sys.exit(0)

    # Read report text
    if args.file:
        report_path = Path(args.file)
        if not report_path.exists():
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        report_text = report_path.read_text(encoding="utf-8")
    elif not sys.stdin.isatty():
        report_text = sys.stdin.read()
    else:
        print("Error: No report provided. Use --file or pipe via stdin.", file=sys.stderr)
        print("Example: python check_report.py 'Check compliance' < report.txt", file=sys.stderr)
        sys.exit(1)

    if not report_text.strip():
        print("Error: Empty report provided.", file=sys.stderr)
        sys.exit(1)

    # Modify prompt for JSON output if requested
    user_prompt = args.prompt
    if args.json:
        user_prompt += "\n\nReturn the analysis as a structured JSON object."

    # Analyze
    try:
        result = analyze_report(
            report_text=report_text,
            user_prompt=user_prompt,
            provider=args.provider,
            model=args.model,
            ollama_url=args.ollama_url,
            lmstudio_url=args.lmstudio_url,
            tumor_type=args.tumor_type,
            quiet=args.quiet
        )
        print(result)

    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()