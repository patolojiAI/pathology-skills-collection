"""
Shared multi-format file processing for pathology skills.

This package provides unified file reading capabilities across all pathology skills
in the collection, supporting text, Excel, CSV, PDF, and image formats.
"""

from .file_readers import (
    read_file_content,
    read_text_file,
    read_excel,
    read_csv,
    read_pdf,
    read_image,
    detect_excel_mode,
)

__version__ = "1.0.0"
__all__ = [
    "read_file_content",
    "read_text_file",
    "read_excel",
    "read_csv",
    "read_pdf",
    "read_image",
    "detect_excel_mode",
]
