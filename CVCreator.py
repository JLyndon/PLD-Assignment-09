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
        self.set_font("helvetica", "B", 23)
        for i in range(1,2):
            self.cell(0, 10, "", border=False, ln=True)
        self.cell(40)
        self.set_xy(35,20)
        self.cell(100, 12, usrDetails[0]['name'], border=False, ln=True, align="C")
        self.ln(7)

    def rsme_crrobj(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(140, 6, content_hdr[6], border=False, ln=True, align="C", fill=True)
        self.ln(4)
    
    def crrobj_cntnt(self):
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        self.set_x(20)
        self.multi_cell(133,4,"To find a position where I am able to transmit my knowledge gained through my chosen course. In addition to grow and seek experience of the field I am pursuing.")
        self.ln()

    def rsme_personal(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[0], border=False, ln=True, align="C", fill=True)
        self.ln(2)

    def personal_cntnt(self):
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        infoCateg = list(usrDetails[1]['personalInfo'].keys())
        maxPersonal = len(infoCateg)

        for i in range(maxPersonal):
            if i % 2 == 0:
                self.set_x(20)
                self.cell(20, 4, infoCateg[i], border=False, ln=False)
                self.cell(6, 4, content_sep, border=False, ln=False, align="C")
                self.cell(35, 4, usrDetails[1]['personalInfo'][infoCateg[i]], border=False, ln=False)
            else:
                self.cell(33, 4, infoCateg[i], border=False, ln=False, align="R")
                self.cell(6, 4, content_sep, border=False, ln=False, align="C")
                self.cell(35, 4, usrDetails[1]['personalInfo'][infoCateg[i]], border=False, ln=True)
        self.ln(3)

    def rsme_contact(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[1], border=False, ln=True, align="C", fill=True)
        self.ln(2)
    
    def contact_cntnt(self):
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        self.set_x(20)
        self.cell(25, 4, "Current Address", border=False, ln=False)
        self.cell(6, 4, content_sep, border=False, ln=False, align="C")
        self.cell(40, 4, usrDetails[1]['contact']['Current Address'], border=False, ln=True)
        self.set_x(20)
        self.cell(25, 4, "Mobile No.", border=False, ln=False)
        self.cell(6, 4, content_sep, border=False, ln=False, align="C")
        self.cell(35, 4, usrDetails[1]['contact']['Mobile Number'], border=False, ln=False) 

        self.cell(33, 4, "Residence No.", border=False, ln=False, align="R")
        self.cell(6, 4, content_sep, border=False, ln=False, align="C")
        self.cell(35, 4, usrDetails[1]['contact']['Residence Number'], border=False, ln=True)       

        self.set_x(20)
        self.cell(25, 4, "Email Address", border=False, ln=False)
        self.cell(6, 4, content_sep, border=False, ln=False, align="C")
        self.cell(40, 4, usrDetails[1]['contact']['Email Address'], border=False, ln=True) 

        self.ln(3)

    def rsme_educ(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[2], border=False, ln=True, align="C", fill=True)
        self.ln(5)

    def educ_cntnt(self):
        self.set_font("helvetica", "", 8)
        self.set_text_color(0,0,0)
        self.set_x(35)
        self.cell(25, 4, "Tertiary", border=False, ln=False)
        self.cell(16, 4, "", border=False, ln=False, align="C")
        self.cell(40, 4, usrDetails[1]['education']['Tertiary']['Major'], border=False, ln=True)
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Tertiary']['University'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Tertiary']['Location'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Tertiary']['Year'], border=False, ln=True) 
        self.ln(2)

        self.set_x(35)
        self.cell(25, 4, "Secondary", border=False, ln=False)
        self.cell(16, 4, "", border=False, ln=False, align="C")
        self.cell(40, 4, usrDetails[1]['education']['High School']['Senior Level']['Strand'], border=False, ln=True)
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['High School']['Senior Level']['School'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['High School']['Senior Level']['Location'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['High School']['Senior Level']['Year'], border=False, ln=True)
        self.ln(3)
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['High School']['Junior Level']['School'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['High School']['Junior Level']['Location'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['High School']['Junior Level']['Year'], border=False, ln=True)
        self.ln(2)

        self.set_x(35)
        self.cell(25, 4, "Primary", border=False, ln=False)
        self.cell(16, 4, "", border=False, ln=False, align="C")
        self.cell(40, 4, usrDetails[1]['education']['Elementary']['School_0'], border=False, ln=True)
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Elementary']['Location_0'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Elementary']['Year_0'], border=False, ln=True)
        self.ln(3) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Elementary']['School_1'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Elementary']['Location_1'], border=False, ln=True) 
        self.set_x(76) 
        self.cell(40, 4, usrDetails[1]['education']['Elementary']['Year_1'], border=False, ln=True) 
        self.ln(3)

    def rsme_skillst(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[3], border=False, ln=True, align="C", fill=True)
        self.ln(4)

    def skill_cntnt(self):
        self.set_font("helvetica", "", 8)
        self.set_text_color(0,0,0)
        self.set_x(20)
        self.cell(90, 5, "Technical Skills", ln=False)
        self.cell(20, 5, "Soft Skills", ln=True, align="R")
        prsnlSkills = len(usrDetails[1]['skills']['Personal'])
        techSkills = len(usrDetails[1]['skills']['Technical'])
        if techSkills == prsnlSkills:
            for i in range(techSkills):
                self.set_x(35)
                self.cell(90, 5, usrDetails[1]["skills"]["Technical"][i], ln=False)
                self.cell(20, 5, usrDetails[1]["skills"]["Personal"][i], ln=True)
        else:
            empty_filler = ""
            if techSkills > prsnlSkills:
                filler_number = techSkills - prsnlSkills
                maxRange = techSkills
                Valuepr_skill = usrDetails[1]['skills']['Personal']
                for i in range(filler_number):
                    Valuepr_skill.append(empty_filler)

                for i in range(maxRange):
                    self.set_x(35)
                    self.cell(90, 5, usrDetails[1]["skills"]["Technical"][i], ln=False)
                    self.cell(20, 5, Valuepr_skill[i], ln=True)

            else:
                maxRange = prsnlSkills
                filler_number = prsnlSkills - techSkills
                Valuepr_skill = usrDetails[1]['skills']['Technical']
                for i in range(filler_number):
                    Valuepr_skill.append(empty_filler)

                for i in range(maxRange):
                    self.set_x(35)
                    self.cell(90, 5, Valuepr_skill[i], ln=False)
                    self.cell(20, 5, usrDetails[1]["skills"]["Personal"][i], ln=True)
        self.ln(4)

    def rsme_achvmnt(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[4], border=False, ln=True, align="C", fill=True)
        self.ln(3)

    def achvment_cntnt(self):
        self.set_font("helvetica", "", 8)
        self.set_text_color(0,0,0)
        maxAchvment = len(usrDetails[1]['achvment'])
        for i in range(maxAchvment):
            self.set_x(20)
            self.cell(20, 5, usrDetails[1]['achvment'][i], ln=True)
        self.ln(5)

    def rsme_ref(self):
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[5], border=False, ln=True, align="C", fill=True)
        self.ln(5)
    
    def ref_cntnt(self):
        self.set_font("helvetica", "", 8)
        self.set_text_color(0,0,0)
        self.set_x(20)
        self.cell(20, 5, usrDetails[1]['reference'])
        self.ln(5)

content_hdr = ["PERSONAL PARTICULARS", "CONTACT INFORMATION", "EDUCATIONAL BACKGROUND", "SKILL SETS", "ACHIEVEMENTS", "REFERENCES", "CAREER OBJECTIVES"]

content_sep = ":"

fileName = "RELLEVE_json.json"

try:
    verifyData = os.path.exists(fileName)
except Exception as e:
    print(e)

with open(fileName, "r") as jsFile:
    usrDetails = json.load(jsFile)

pdf = PDF("P", "mm", "A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.marg_()
pdf.pg_header()
pdf.rsme_crrobj()
pdf.crrobj_cntnt()
pdf.rsme_personal()
pdf.personal_cntnt()
pdf.rsme_contact()
pdf.contact_cntnt()
pdf.rsme_educ()
pdf.educ_cntnt()
pdf.rsme_skillst()
pdf.skill_cntnt()
pdf.rsme_achvmnt()
pdf.achvment_cntnt()
pdf.rsme_ref()
pdf.ref_cntnt()

pdf.output("RELLEVE_JO-LYNDON.pdf")