from pathlib import Path
from PyPDF2 import PdfReader
path = Path(r"C:\Users\reddy\portFolio\Resumes\Naveen_python_developer.pdf")
print("exists", path.exists())
if path.exists():
    reader = PdfReader(str(path))
    print("pages", len(reader.pages))
    for i, page in enumerate(reader.pages[:8], 1):
        text = page.extract_text() or ""
        print(f"--- PAGE {i} ---")
        print(text[:6000])
        print()
