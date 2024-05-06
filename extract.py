import PyPDF2

pdf_path = './pdf_downloads/1of2021.pdf'

with open(pdf_path, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    text_content = ''
    for page in pdf_reader.pages:
        text_content += page.extract_text()

print(text_content)

