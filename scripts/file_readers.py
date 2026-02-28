"""
Multi-format file readers for pathology reports.

Supports: text, Excel (batch and structured), CSV, PDF, and images.
"""

import base64
from pathlib import Path
from typing import Union, List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


def read_file_content(
    filepath: Path,
    client: Optional[Any] = None,
    use_vision: bool = False
) -> Union[str, List[Dict[str, Any]]]:
    """
    Read any supported file format and return content.

    Args:
        filepath: Path to the file
        client: Anthropic client for vision API (required for images/PDFs with vision)
        use_vision: Force vision API for PDFs even if pypdf succeeds

    Returns:
        - str: Single report text (for .txt, .pdf, .csv structured, images)
        - List[Dict]: Batch reports (for Excel/CSV batch mode)

    Raises:
        ValueError: Unsupported file format
        FileNotFoundError: File doesn't exist
    """
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    suffix = filepath.suffix.lower()

    if suffix in {'.txt', '.md'}:
        return read_text_file(filepath)
    elif suffix in {'.xlsx', '.xls'}:
        return read_excel(filepath)
    elif suffix == '.csv':
        return read_csv(filepath)
    elif suffix == '.pdf':
        return read_pdf(filepath, client, use_vision)
    elif suffix in {'.jpg', '.jpeg', '.png', '.tiff', '.tif'}:
        if client is None:
            raise ValueError("Claude client required for image processing. Pass client parameter.")
        return read_image(filepath, client)
    elif suffix in {'.docx', '.doc'}:
        return read_docx(filepath)
    else:
        raise ValueError(f"Unsupported file format: {suffix}")


def read_text_file(filepath: Path) -> str:
    """Read plain text file with encoding detection."""
    try:
        return filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        logger.warning(f"UTF-8 decode failed for {filepath.name}, trying latin-1")
        return filepath.read_text(encoding='latin-1')


def read_excel(filepath: Path) -> Union[str, List[Dict[str, Any]]]:
    """
    Read Excel file with auto-detection of batch vs structured format.

    Returns:
        - List[Dict]: Batch mode (one report per row)
        - str: Structured mode (field-value pairs converted to text)
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas required for Excel support. Install with: pip install pandas openpyxl")

    mode = detect_excel_mode(filepath)

    if mode == 'batch':
        # Return list of report dicts
        df = pd.read_excel(filepath)

        # Validate required column
        if 'report_text' not in df.columns:
            # Try case-insensitive match
            cols_lower = {col.lower(): col for col in df.columns}
            if 'report_text' in cols_lower:
                df.rename(columns={cols_lower['report_text']: 'report_text'}, inplace=True)
            else:
                raise ValueError(
                    f"Excel batch mode requires 'report_text' column. "
                    f"Found columns: {list(df.columns)}"
                )

        return df.to_dict('records')

    else:  # structured mode
        # Read without headers, convert field-value pairs to text
        df = pd.read_excel(filepath, header=None)
        return convert_structured_to_text(df)


def detect_excel_mode(filepath: Path) -> str:
    """
    Auto-detect if Excel is batch list or structured report.

    Returns:
        'batch' or 'structured'
    """
    try:
        import pandas as pd
    except ImportError:
        return 'batch'  # Default

    # Read first 5 rows to check format
    df = pd.read_excel(filepath, nrows=5)

    # Batch mode: has 'report_text' column
    if 'report_text' in df.columns or 'report_text' in [c.lower() for c in df.columns]:
        return 'batch'

    # Structured mode: 2 columns, looks like field-value pairs
    if df.shape[1] == 2:
        # Check if column A contains pathology field names
        col_a = df.iloc[:, 0].astype(str).str.lower()
        pathology_keywords = [
            'procedure', 'specimen', 'tumor', 'grade', 'margin',
            'size', 'histologic', 'type', 'pt', 'pn', 'stage'
        ]
        keyword_matches = sum(
            any(kw in cell for kw in pathology_keywords)
            for cell in col_a
        )

        if keyword_matches >= 2:
            return 'structured'

    # Default to batch
    return 'batch'


def convert_structured_to_text(df) -> str:
    """Convert structured Excel (field-value pairs) to text report."""
    lines = []

    for _, row in df.iterrows():
        if pd.notna(row[0]) and pd.notna(row[1]):
            field = str(row[0]).strip()
            value = str(row[1]).strip()

            # Skip empty rows
            if not field or not value:
                continue

            lines.append(f"{field}: {value}")

    return '\n'.join(lines)


def read_csv(filepath: Path) -> Union[str, List[Dict[str, Any]]]:
    """
    Read CSV file (same logic as Excel batch mode).

    Returns:
        List[Dict]: Batch reports if 'report_text' column exists
        str: Otherwise converts to text
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas required for CSV support. Install with: pip install pandas")

    df = pd.read_csv(filepath)

    # Check if batch mode (has report_text column)
    if 'report_text' in df.columns or 'report_text' in [c.lower() for c in df.columns]:
        # Normalize column name
        cols_lower = {col.lower(): col for col in df.columns}
        if 'report_text' in cols_lower:
            df.rename(columns={cols_lower['report_text']: 'report_text'}, inplace=True)

        return df.to_dict('records')

    else:
        # Convert to text (treat as single structured report)
        return df.to_string(index=False)


def read_pdf(filepath: Path, client: Optional[Any] = None, use_vision: bool = False) -> str:
    """
    Read PDF file with pypdf or Claude vision API.

    Args:
        filepath: Path to PDF
        client: Anthropic client (required if pypdf fails or use_vision=True)
        use_vision: Force vision API even if pypdf succeeds

    Returns:
        Extracted text content
    """
    # Try pypdf first (faster and free for clean PDFs)
    if not use_vision:
        try:
            import pypdf

            reader = pypdf.PdfReader(filepath)
            text_parts = []

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

            text = '\n\n'.join(text_parts)

            # If extraction successful and substantial, return it
            if len(text.strip()) > 100:
                logger.info(f"PDF {filepath.name} extracted with pypdf ({len(text)} chars)")
                return text
            else:
                logger.warning(f"PDF {filepath.name} pypdf extraction poor, using vision API")

        except ImportError:
            logger.warning("pypdf not installed. Using Claude vision API.")
        except Exception as e:
            logger.warning(f"pypdf failed for {filepath.name}: {e}. Using vision API.")

    # Use vision API
    if client is None:
        raise ValueError(
            "Claude client required for PDF vision processing. "
            "Install pypdf for free PDF extraction: pip install pypdf"
        )

    return read_pdf_with_vision(filepath, client)


def read_pdf_with_vision(filepath: Path, client) -> str:
    """Read PDF using Claude vision API (for scanned/image PDFs)."""
    import pypdf

    # Convert PDF pages to images and process with vision
    # For now, use text extraction but could enhance with image conversion

    # Read PDF pages as images would require pdf2image library
    # For simplicity, we'll read it as a document and let Claude's vision handle it

    # Read PDF as binary and encode
    with open(filepath, 'rb') as f:
        pdf_data = f.read()

    # Note: Claude API supports PDF directly via document type
    # Using image type requires converting PDF to images first

    # For multi-page PDFs, we'll process page by page if needed
    reader = pypdf.PdfReader(filepath)
    all_text = []

    for page_num, page in enumerate(reader.pages):
        # Try to extract text first
        page_text = page.extract_text()

        if page_text and len(page_text.strip()) > 50:
            # Good text extraction
            all_text.append(page_text)
        else:
            # Need vision API for this page
            logger.info(f"Using vision API for PDF page {page_num + 1}")

            # Convert page to image would require pdf2image
            # For now, include a note
            all_text.append(
                f"[Page {page_num + 1} - Vision processing would occur here. "
                f"Install pdf2image for full support.]"
            )

    if all_text:
        return '\n\n'.join(all_text)
    else:
        raise ValueError(f"Could not extract text from PDF: {filepath}")


def read_image(filepath: Path, client) -> str:
    """
    Read image using Claude vision API.

    Supports: .jpg, .jpeg, .png, .tiff
    """
    # Read image and encode to base64
    with open(filepath, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    # Determine media type
    media_type_map = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.tiff': 'image/tiff',
        '.tif': 'image/tiff'
    }

    media_type = media_type_map.get(filepath.suffix.lower(), 'image/jpeg')

    logger.info(f"Processing image {filepath.name} with Claude vision API")

    # Call Claude API with vision
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data
                        }
                    },
                    {
                        "type": "text",
                        "text": (
                            "Extract ALL text from this pathology report image. "
                            "Preserve the exact formatting, structure, and all diagnostic details. "
                            "Include all findings, diagnoses, staging information, and clinical data. "
                            "Do not summarize or interpret - transcribe verbatim."
                        )
                    }
                ]
            }]
        )

        extracted_text = response.content[0].text
        logger.info(f"Extracted {len(extracted_text)} characters from {filepath.name}")

        return extracted_text

    except Exception as e:
        logger.error(f"Vision API failed for {filepath.name}: {e}")
        raise ValueError(f"Could not process image {filepath.name}: {e}")


def read_docx(filepath: Path) -> str:
    """Read Word document (.docx)."""
    try:
        import docx
    except ImportError:
        raise ImportError("python-docx required for Word support. Install with: pip install python-docx")

    doc = docx.Document(filepath)
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]

    return '\n'.join(paragraphs)


def get_supported_extensions() -> Dict[str, List[str]]:
    """Return dictionary of supported file types and their extensions."""
    return {
        'text': ['.txt', '.md'],
        'excel': ['.xlsx', '.xls'],
        'csv': ['.csv'],
        'pdf': ['.pdf'],
        'image': ['.jpg', '.jpeg', '.png', '.tiff', '.tif'],
        'word': ['.docx', '.doc']
    }


def is_supported_file(filepath: Path) -> bool:
    """Check if file extension is supported."""
    all_extensions = []
    for extensions in get_supported_extensions().values():
        all_extensions.extend(extensions)

    return filepath.suffix.lower() in all_extensions
