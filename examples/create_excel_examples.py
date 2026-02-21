#!/usr/bin/env python3
"""
Create example Excel and CSV files for testing pathology skills.
Run this script to generate example batch files.
"""

import pandas as pd
from pathlib import Path

# Example directory
examples_dir = Path(__file__).parent

# Sample report texts
breast_report = """PATHOLOGY REPORT
Patient ID: EX-BR-001
Specimen: Left breast lumpectomy
DIAGNOSIS: Invasive ductal carcinoma, Grade 2, 2.3 cm
ER: Positive (95%), PR: Positive (80%), HER2: Negative (1+)
Margins: All negative
pT2 N0"""

colorectal_report = """PATHOLOGY REPORT
Patient ID: EX-CR-002
Specimen: Sigmoid colon resection
DIAGNOSIS: Adenocarcinoma, moderately differentiated, 3.5 cm
pT3 N1a (2/18 nodes positive)
Margins: Negative, CRM: Clear
LVI: Present, PNI: Absent
MMR: Proficient"""

pancreas_report = """PATHOLOGY REPORT
Patient ID: EX-PC-003
Specimen: Pancreaticoduodenectomy (Whipple)
DIAGNOSIS: Pancreatic ductal adenocarcinoma, 3.1 cm
Grade: Moderately differentiated
pT2 N1 (3/18 nodes positive)
All margins: Negative
LVI: Present, PNI: Present"""

gastric_report = """PATHOLOGY REPORT
Patient ID: EX-GA-004
Specimen: Total gastrectomy
DIAGNOSIS: Gastric adenocarcinoma, intestinal type (Lauren)
Tumor size: 4.2 cm
Grade: Moderately differentiated
pT3 N2 (5/22 nodes positive)
Margins: Negative
HER2: Negative"""

# Create Excel batch format (one report per row)
batch_data = {
    'report_text': [breast_report, colorectal_report, pancreas_report, gastric_report],
    'patient_id': ['EX-BR-001', 'EX-CR-002', 'EX-PC-003', 'EX-GA-004'],
    'tumor_type': ['breast', 'colorectal', 'pancreas', 'gastric']
}

df_batch = pd.DataFrame(batch_data)

# Save to Excel
excel_path = examples_dir / 'excel' / 'batch_reports.xlsx'
excel_path.parent.mkdir(exist_ok=True)
df_batch.to_excel(excel_path, index=False, engine='openpyxl')
print(f"✅ Created: {excel_path}")

# Save to CSV
csv_path = examples_dir / 'csv' / 'batch_reports.csv'
csv_path.parent.mkdir(exist_ok=True)
df_batch.to_csv(csv_path, index=False)
print(f"✅ Created: {csv_path}")

# Create Excel structured format (field-value pairs)
structured_data = {
    'Field': [
        'Patient ID',
        'Procedure',
        'Tumor Site',
        'Tumor Size',
        'Histologic Type',
        'Histologic Grade',
        'ER Status',
        'PR Status',
        'HER2 Status',
        'Ki-67',
        'Margins',
        'Lymphovascular Invasion',
        'Perineural Invasion',
        'pT Category',
        'pN Category',
        'Stage Group'
    ],
    'Value': [
        'EX-BR-001',
        'Left breast lumpectomy',
        'Upper outer quadrant',
        '2.3 cm',
        'Invasive ductal carcinoma',
        'Grade 2 (moderately differentiated)',
        'Positive (95%, strong)',
        'Positive (80%, moderate)',
        'Negative (IHC 1+)',
        '18%',
        'All negative (closest 3 mm)',
        'Not identified',
        'Not identified',
        'pT2',
        'pN0 (sentinel node negative)',
        'Stage IIA'
    ]
}

df_structured = pd.DataFrame(structured_data)

structured_path = examples_dir / 'excel' / 'structured_breast.xlsx'
df_structured.to_excel(structured_path, index=False, header=False, engine='openpyxl')
print(f"✅ Created: {structured_path}")

# Create template for batch processing
template_data = {
    'report_text': ['Paste full report text here', 'Another report here'],
    'patient_id': ['P001', 'P002'],
    'tumor_type': ['breast', 'colorectal']
}

df_template = pd.DataFrame(template_data)

template_path = examples_dir / 'excel' / 'template_batch.xlsx'
df_template.to_excel(template_path, index=False, engine='openpyxl')
print(f"✅ Created: {template_path}")

print("\n✅ All example files created successfully!")
print("\nUsage:")
print("  # Batch processing")
print("  python cli-tools/process_skill.py --skill compliance-checker examples/excel/batch_reports.xlsx")
print("\n  # Single structured report")
print("  python cli-tools/process_skill.py --skill breast-specialist examples/excel/structured_breast.xlsx")
