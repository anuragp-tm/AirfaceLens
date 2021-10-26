from fpdf import FPDF
import os
from configobj import ConfigObj

config = ConfigObj('airface_config.ini')

from detect_and_read_text import textOutput

result=textOutput
imgName=config['IMAGE_NAME'].split(".")[0]
target_text_dir=config['TARGET_TXT_FILE_DIR']
target_text_file_path=os.path.join(target_text_dir, f"{imgName}.txt")
target_pdf_dir=config['TARGET_PDF_FILE_DIR']
target_pdf_file_path=os.path.join(target_pdf_dir, f"{imgName}.pdf")
with open(target_text_file_path, "w+") as f:
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
with open(target_text_file_path, "r") as f:
 for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

# save the pdf with name .pdf
pdf.output(target_pdf_file_path)
f.close()
