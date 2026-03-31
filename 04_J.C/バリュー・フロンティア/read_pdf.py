import sys
try:
    import PyPDF2
except ImportError:
    print("PyPDF2 is not installed.")
    sys.exit(1)

pdf_path = sys.argv[1]
with open(pdf_path, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    for i, page in enumerate(reader.pages):
        print(f"--- Page {i+1} ---")
        print(page.extract_text())
