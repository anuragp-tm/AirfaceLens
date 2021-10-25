from fpdf import FPDF
import os
from detect_and_read_text import read_text_from_image,read_easyocr_text
result=read_text_from_image
target_file_path='resources/templates/txt/image_text.txt'
target_pdf_dir='resources/templates/pdf'
with open(target_file_path, "w+") as f:
        f.write(result)


# save FPDF() class into
# a variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)




# insert the texts in pdf
with open(target_file_path, "r") as f:
 for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

# save the pdf with name .pdf
pdf.output(os.path.join(target_pdf_dir,'image_text.pdf'))
f.close()

