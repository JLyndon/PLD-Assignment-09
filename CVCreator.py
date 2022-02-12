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
        # Header == Display the User's ID picture and Name
        self.image("ID_2x2.jpg", 160, 11, 37, 35)
        self.set_font("helvetica", "B", 31)
        for i in range(1,2):
            self.cell(0, 10, "", border=False, ln=True)
        self.cell(40)
        self.set_xy(35,20)
        self.cell(100, 12, usrDetails[0]['name'], border=False, ln=True, align="C")
        self.ln(5)

# Start of the 'Content' Segment
    def rsme_crrobj(self):
        # Formatted subheader for Career Objectives
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(140, 6, content_hdr[6], border=False, ln=True, align="C", fill=True)
        self.ln(4)
    
    def crrobj_cntnt(self):
        # Uses JSON Content for Displaying the Objective
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        self.set_x(20)
        self.multi_cell(133,4, usrDetails[1]['objective'])
        self.ln()

    def rsme_personal(self):
        # Formatted subhead for Personal Information
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[0], border=False, ln=True, align="C", fill=True)
        self.ln(2)

    def personal_cntnt(self):
        # Text Configurations
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        # Lists all needed dict_keys
        infoCateg = list(usrDetails[1]['personalInfo'].keys())
        maxPersonal = len(infoCateg)

        for i in range(maxPersonal): # Iteration of Similar Outputs - Uses the number of keys as range
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
        # Formatted subhead for Contact Info
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[1], border=False, ln=True, align="C", fill=True)
        self.ln(2)
    
    def contact_cntnt(self):
        # Manual Setup -- Uses JSON Contents for Display by accessing dict with dict_keys
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
        # Formatted subhead for Educational Background
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[2], border=False, ln=True, align="C", fill=True)
        self.ln(5)

    def educ_cntnt(self):
        # Uses JSON Contents for Display -- iteration (For Loops)
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        self.set_x(35)
        self.cell(25, 4, "Tertiary", border=False, ln=False)
        self.cell(16, 4, "", border=False, ln=False, align="C")
        educCateg = list(usrDetails[1]['education']['Tertiary'].values())
        maxEduc = len(educCateg)

        for i in range(maxEduc):
            if i == 0:
                self.cell(40, 4, educCateg[i], border=False, ln=True)
            else:
                self.set_x(76) 
                self.cell(40, 4, educCateg[i], border=False, ln=True) 
        self.ln(2)

        self.set_x(35)
        self.cell(25, 4, "Secondary", border=False, ln=False)
        self.cell(16, 4, "", border=False, ln=False, align="C")
        educCateg_hs_sen = list(usrDetails[1]['education']['High School']['Senior Level'].values())
        maxEduc_s = len(educCateg_hs_sen)

        for i in range(maxEduc_s):
            if i == 0:
                self.cell(40, 4, educCateg_hs_sen[i], border=False, ln=True)
            else:
                self.set_x(76) 
                self.cell(40, 4, educCateg_hs_sen[i], border=False, ln=True) 
        self.ln(3)

        educCateg_hs_jr = list(usrDetails[1]['education']['High School']['Junior Level'].values())
        maxEduc_j = len(educCateg_hs_jr)

        for i in range(maxEduc_j):
            self.set_x(76) 
            self.cell(40, 4, educCateg_hs_jr[i], border=False, ln=True) 
        self.ln(2)

        self.set_x(35)
        self.cell(25, 4, "Primary", border=False, ln=False)
        self.cell(16, 4, "", border=False, ln=False, align="C")
        educCateg_prm = list(usrDetails[1]['education']['Elementary'].values())
        maxEduc_prm = len(educCateg_prm)

        repeatnum = 0
        for i in range(maxEduc_prm): # Continuous format regardless of numbers of info batches entered
            if i == 0:
                self.cell(40, 4, educCateg_prm[i], border=False, ln=True)
            elif i <= 2:
                self.set_x(76) 
                self.cell(40, 4, educCateg_prm[i], border=False, ln=True)
                if repeatnum == 2:
                    self.ln(3)
                    repeatnum = 0
            elif i > 2:
                self.set_x(76) 
                self.cell(40, 4, educCateg_prm[i], border=False, ln=True)
                if repeatnum == 3:
                    self.ln(3)
                    repeatnum = 0
            repeatnum  += 1
        self.ln(3)

    def rsme_skillst(self):
        # Formatted subhead for Skill Sets
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[3], border=False, ln=True, align="C", fill=True)
        self.ln(4)

    def skill_cntnt(self):
        # Double column format, determines the greater value set and add empty fillers to the lower value set.
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        self.set_x(16)
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
                    self.set_x(22)
                    self.cell(97, 5, usrDetails[1]["skills"]["Technical"][i], ln=False)
                    self.cell(30, 5, Valuepr_skill[i], ln=True)

            else:
                maxRange = prsnlSkills
                filler_number = prsnlSkills - techSkills
                Valuepr_skill = usrDetails[1]['skills']['Technical']
                for i in range(filler_number):
                    Valuepr_skill.append(empty_filler)

                for i in range(maxRange):
                    self.set_x(22)
                    self.cell(97, 5, Valuepr_skill[i], ln=False)
                    self.cell(30, 5, usrDetails[1]["skills"]["Personal"][i], ln=True)
        self.ln(4)

    def rsme_achvmnt(self):
        # Formatted subhead for Achievements
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[4], border=False, ln=True, align="C", fill=True)
        self.ln(3)

    def achvment_cntnt(self):
        # Simple For-Loop Iteration for easier display
        self.set_font("helvetica", "", 9)
        self.set_text_color(0,0,0)
        maxAchvment = len(usrDetails[1]['achvment'])
        for i in range(maxAchvment):
            self.set_x(20)
            self.cell(20, 5, usrDetails[1]['achvment'][i], ln=True)
        self.ln(5)

    def rsme_ref(self):
        # Formatted subhead for References
        self.set_fill_color(45,45,45)
        self.set_text_color(255,255,255)
        self.set_font("helvetica", "", 8)
        self.cell(0, 5, content_hdr[5], border=False, ln=True, align="C", fill=True)
        self.ln(3)
    
    def ref_cntnt(self):
        # Simple cell display
        self.set_font("helvetica", "I", 9)
        self.set_text_color(0,0,0)
        self.set_x(20)
        self.cell(20, 5, usrDetails[1]['reference'])
        self.ln(5)

# File Detection and Handling
fileName = "RELLEVE_json.json"

try:
    verifyData = os.path.exists(fileName)
    if verifyData == True:
        print("\33[92mWait a moment.. Creating your file :)\33[0m")
except Exception as e:
    print(e, "\33[91mPlease include the JSON file to your current directory :(\33[0m")

with open(fileName, "r") as jsFile:
    usrDetails = json.load(jsFile)

content_hdr = ["PERSONAL PARTICULARS", "CONTACT INFORMATION", "EDUCATIONAL BACKGROUND", "SKILL SETS", "ACHIEVEMENTS", "REFERENCES", "CAREER OBJECTIVES"]

content_sep = ":"

# PDF Properties -- to be filled by data from JSON file
pdf = PDF("P", "mm", (210,305))
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

# Call for Final Output 
pdf.output("RELLEVE_JO-LYNDON.pdf")