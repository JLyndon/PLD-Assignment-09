from fpdf import FPDF
import json, os

# ------------- CONTEXT ------------------
# Program: PDF Resume Creator
#     Create a python program that will create your personal resume in PDF format
#     All personal details are stored in a JSON file
#     Your program should read the JSON file and write the details in the PDF
#     The output file should be: LASTNAME_FIRSTNAME.pdf

class PDF(FPDF):
    def marg_(self):
        self.set_margins(15, 15, 15)

    def pg_header (self):
        self.image("ID_2x2.jpg", 160, 11, 37, 35)
        self.set_font("Arial", "B", 16)
        for i in range(1,2):
            self.cell(0, 10, "", border=False, ln=True)
        self.cell(40)
        self.cell(100, 12, "Jo Lyndon A. Relleve Jr.", border=True, ln=True, align="C")
        self.ln(20)

    def rsme_personal(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[0], border=True, ln=True, align="C", fill=True)
        self.ln(15)
    def rsme_contact(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[1], border=True, ln=True, align="C", fill=True)
        self.ln(15)
    def rsme_educ(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 6, content_hdr[2], border=True, ln=True, align="C", fill=True)
        self.ln(15)
    def rsme_skillst(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 6, content_hdr[3], border=True, ln=True, align="C", fill=True)
        self.ln(15)
    def rsme_achvmnt(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 6, content_hdr[4], border=True, ln=True, align="C", fill=True)
        self.ln(15)
    def rsme_ref(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 6, content_hdr[5], border=True, ln=True, align="C", fill=True)
        self.ln(15)

content_hdr = ["PERSONAL PARTICULARS", "CONTACT", "EDUCATIONAL BACKGROUND", "SKILL SETS", "ACHIEVEMENTS", "REFERENCES"]

fileName = "RELLEVE_json.json"

try:
    verifyData = os.path.exists(fileName)
except Exception as e:
    print(e)

with open(fileName, "r") as jsFile:
    usrDetails = json.load(jsFile)
    print(usrDetails)

pdf = PDF("P", "mm", "A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.marg_()
pdf.pg_header()
pdf.rsme_personal()
pdf.rsme_contact()
pdf.rsme_educ()
pdf.rsme_skillst()
pdf.rsme_achvmnt()
pdf.rsme_ref()

pdf.output("RELLEVE_JO LYNDON.pdf")