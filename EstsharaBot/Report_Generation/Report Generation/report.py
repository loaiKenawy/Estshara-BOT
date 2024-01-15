import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import date 

# Load the data from the JSON file
with open('data_lungs.json') as f:
    data = json.load(f)

# Extract the relevant data fields
patient_name = data['patient']['name']
patient_age = data['patient']['age']
patient_gender = data['patient']['gender']
today_time = date.today()


# Create a new PDF document
pdf_canvas = canvas.Canvas('medical_report_lungs.pdf', pagesize=letter)

# Add the logo to the document
pdf_canvas.drawImage('images\Estsharabot.jpeg', 50, 680, width=90, height=90)

# Add the patient name and age to the document
pdf_canvas.setFont('Helvetica-Bold', 18)
pdf_canvas.drawCentredString(300, 700, 'Medical Report')
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.drawRightString(550, 650, f'Date: {today_time}')

# Add the patient information section to the document
pdf_canvas.setFillColor(colors.darkgreen)
pdf_canvas.setFont('Helvetica-Bold', 14)
pdf_canvas.drawString(50, 600, 'Patient Information')

# Patient Informations from json file
pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(50, 570, 'Name:')
pdf_canvas.drawString(200, 570, patient_name)

pdf_canvas.drawString(50, 550, 'Age:')
pdf_canvas.drawString(200, 550, str(patient_age))

pdf_canvas.drawString(50, 530, 'Gender:')
pdf_canvas.drawString(200, 530, str(patient_gender))


# Medical History Variables from Json
medical_Condition = data['medical_history']['medical_condition_before']
medicine = data['medical_history']['medications_or_supplements']
surgiries = data['medical_history']['Surgeries_or_Hospitalizations']
allergies = data['medical_history']['Allergies_to_medications']
fasmily_history = data['medical_history']['family_history']
smoke = data['medical_history']['Smoking']
alcholes = data['medical_history']['Drinking_Alcholes']
others = data['medical_history']['Other']


# Add the medical history section to the document
pdf_canvas.setFillColor(colors.darkgreen)
pdf_canvas.setFont('Helvetica-Bold', 14)
pdf_canvas.drawString(50, 500, 'Medical History')

pdf_canvas.setFont('Helvetica', 12)
pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 480, '- Diagnosed with medical condition before :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(290, 480, medical_Condition)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 455, '- Taking any medications or supplements :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(287, 455, medicine)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 430, '- Surgeries or Hospitalizations in the past :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(287, 430, surgiries)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 405, '- Allergies to medications or other substances :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(311, 405, allergies)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 380, '- A family history of any medical conditions :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(293, 380, fasmily_history)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 355, '- Smoking :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(120, 355, smoke)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 330, '- Drinking Alcholes :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(167, 330, alcholes)

pdf_canvas.setFillColorRGB(0, 0, 0)
pdf_canvas.drawString(57, 305, '- Other things the Patient say :')
pdf_canvas.setFillColor(colors.firebrick)
pdf_canvas.drawString(222, 305, others)
pdf_canvas.setFillColorRGB(0, 0, 0)


################################################################################################

# which section

form = data['predicted_form']

if form == "Brain":


    ## Brain form variables from json file
    headache_value = data['Brain_form']['Headache']
    seizures_value = data['Brain_form']['Seizures']
    Vomiting_and_Drowsiness = data['Brain_form']['Vomiting_and_Drowsiness']
    Mental_or_Behavioral = data['Brain_form']['Mental_or_Behavioral_changes']
    Vision_or_Speech = data['Brain_form']['Vision_or_Speech_Problems']

    space = 10
    # Cancer Questions place
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 14)
    pdf_canvas.drawString(50, 280, 'Cancer Survey')
    pdf_canvas.setFont('Helvetica-Bold', 10)
    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(52, 260, 'Brain Cancer Prediction Questions :')

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 240-space, '- Headache :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(143, 240-space, headache_value)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 210-space, '- Seizures :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(134, 210-space, seizures_value)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 180-space, '- Vomiting and Drowsiness :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(222, 180-space, Vomiting_and_Drowsiness)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 150-space, '- Mental or Behavioral changes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(245, 150-space, Mental_or_Behavioral)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 120-space, '- Vision or Speech Problems :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(233, 120-space, Vision_or_Speech)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    # Create a new page in the PDF document
    pdf_canvas.showPage()

    ## Image variables from json file

    cancer = data['image_model']['cancer_type']
    cancer_accuracy = data['image_model']['cancer_accuracy']
    cancer_notes = data['image_model']['notes']

    # Add content to the new page
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 16)
    pdf_canvas.drawString(50, 710, 'X-Ray Image')
    pdf_canvas.setFont('Helvetica', 14)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawImage('images\\brain_glioma_0009.jpg', 55, 430, width=300, height=250)
    pdf_canvas.drawString(55, 380, '- Cancer Type :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(155, 380, cancer)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(55, 350, '- Accuracy :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(135, 350, cancer_accuracy)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(55, 320, '- Notes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(115, 320, cancer_notes)
    pdf_canvas.setFillColorRGB(0, 0, 0)


    # Save the PDF document
    pdf_canvas.save()

elif form == "Kidney":

    ## Breast form variables from json file
    back_lump = data['Kidney_form']['back_lump']
    urine_blood = data['Kidney_form']['urine_blood']
    back_pain = data['Kidney_form']['back_pain']
    kidney_appetite_loss = data['Kidney_form']['kidney_appetite_loss']
    kidney_weight_loss = data['Kidney_form']['kidney_weight_loss']
    kidney_tiredness = data['Kidney_form']['kidney_tiredness']
    kidney_fever = data['Kidney_form']['kidney_fever']
    dark_pee = data['Kidney_form']['dark_pee']
    Kidney_blood_pressure = data['Kidney_form']['Kidney_blood_pressure']
    Kidney_high_temp = data['Kidney_form']['Kidney_high_temp']
    testicles_viens = data['Kidney_form']['testicles_viens']
    swollen_glands = data['Kidney_form']['swollen_glands']
    Kidney_bone_pain = data['Kidney_form']['Kidney_bone_pain']
    Kidney_fatigue = data['Kidney_form']['Kidney_fatigue']
    testicle_swelling = data['Kidney_form']['testicle_swelling']
    leg_swelling = data['Kidney_form']['leg_swelling']
    Kidney_anemia = data['Kidney_form']['Kidney_anemia']

    space = 10
    # Cancer Questions place
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 14)
    pdf_canvas.drawString(50, 280, 'Cancer Survey')
    pdf_canvas.setFont('Helvetica-Bold', 10)
    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(52, 260, 'Kidney Cancer Prediction Questions :')

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 240-space, '- Back lump :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(153, 240-space, back_lump)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 210-space, '- Urine blood :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(147, 210-space, urine_blood)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 180-space, '- Back pain :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(160, 180-space, back_pain)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 150-space, '- Kidney appetite loss :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(174, 150-space, kidney_appetite_loss)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 120-space, '- kidney weight loss :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(160, 120-space, kidney_weight_loss)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.showPage()

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 750-space, '- Kidney tiredness :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(222, 750-space, kidney_tiredness)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 720-space, '- Kidney fever :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(148, 720-space, kidney_fever)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 690-space, '- Dark pee :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(175, 690-space, dark_pee)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 660-space, '- Kidney blood pressure :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(200, 660-space, Kidney_blood_pressure)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 630-space, '- Kidney high temp :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 630-space, Kidney_high_temp)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 600-space, '- Testicles viens :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 600-space, testicles_viens)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 570-space, '- Swollen glands :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(175, 570-space, swollen_glands)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 540-space, '- Kidney bone pain :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(200, 540-space, Kidney_bone_pain)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 510-space, '- Kidney fatigue :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 510-space, Kidney_fatigue)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 480-space, '- Testicle swelling :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 480-space, testicle_swelling)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 450-space, '- Leg swelling :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 450-space, leg_swelling)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 420-space, '- Kidney anemia :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 420-space, Kidney_anemia)
    pdf_canvas.setFillColorRGB(0, 0, 0)
    ## Image variables from json file

    cancer = data['image_model']['cancer_type']
    cancer_accuracy = data['image_model']['cancer_accuracy']
    cancer_notes = data['image_model']['notes']

    # Add content to the new page
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 16)
    pdf_canvas.drawString(50, 360, 'X-Ray Image')
    pdf_canvas.setFont('Helvetica', 14)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawImage('images\\brain_glioma_0009.jpg', 55, 80, width=300, height=250)
    pdf_canvas.drawString(365, 250, '- Cancer Type :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(465, 250, cancer)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(365, 210, '- Accuracy :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(445, 210, cancer_accuracy)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(365, 170, '- Notes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(422, 170, cancer_notes)
    pdf_canvas.setFillColorRGB(0, 0, 0)


    # Save the PDF document
    pdf_canvas.save()

elif form == "Breast":

    ## Breast form variables from json file
    breast_lump = data['Breast_form']['breast_lump']
    breast_skin = data['Breast_form']['breast_skin']
    thick_or_swell = data['Breast_form']['thick_or_swell']
    irritaion_dimpling = data['Breast_form']['irritaion_dimpling']
    Redness_skin = data['Breast_form']['Redness_skin']
    alternation_in_appearance = data['Breast_form']['alternation_in_appearance']
    breast_pain = data['Breast_form']['breast_pain']
    nipple_discharge = data['Breast_form']['nipple_discharge']
    Dimpling = data['Breast_form']['Dimpling']
    Nipple_retraction = data['Breast_form']['Nipple_retraction']
    swollen_lumph_nodes = data['Breast_form']['swollen_lumph_nodes']
    Growing_veins = data['Breast_form']['Growing_veins']
    Sunken_nipple = data['Breast_form']['Sunken_nipple']

    space = 10
    # Cancer Questions place
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 14)
    pdf_canvas.drawString(50, 280, 'Cancer Survey')
    pdf_canvas.setFont('Helvetica-Bold', 10)
    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(52, 260, 'Breast Cancer Prediction Questions :')

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 240-space, '- Breast Lump :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(153, 240-space, breast_lump)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 210-space, '- Breast Skin :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(147, 210-space, breast_skin)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 180-space, '- Thick or Swell :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(160, 180-space, thick_or_swell)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 150-space, '- Irritaion Dimpling :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(174, 150-space, irritaion_dimpling)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 120-space, '- Redness Skin :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(160, 120-space, Redness_skin)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.showPage()

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 750-space, '- Alternation in appearance :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(222, 750-space, alternation_in_appearance)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 720-space, '- Breast pain :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(148, 720-space, breast_pain)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 690-space, '- Nipple discharge :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(175, 690-space, nipple_discharge)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 660-space, '- Swollen lumph nodes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(200, 660-space, swollen_lumph_nodes)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 630-space, '- Growing veins :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 630-space, Growing_veins)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 600-space, '- Sunken nipple :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(164, 600-space, Sunken_nipple)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    ## Image variables from json file

    cancer = data['image_model']['cancer_type']
    cancer_accuracy = data['image_model']['cancer_accuracy']
    cancer_notes = data['image_model']['notes']

    # Add content to the new page
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 16)
    pdf_canvas.drawString(50, 550, 'X-Ray Image')
    pdf_canvas.setFont('Helvetica', 14)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawImage('images\\brain_glioma_0009.jpg', 55, 280, width=300, height=250)
    pdf_canvas.drawString(55, 240, '- Cancer Type :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(155, 240, cancer)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(55, 210, '- Accuracy :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(135, 210, cancer_accuracy)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(55, 180, '- Notes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(115, 180, cancer_notes)
    pdf_canvas.setFillColorRGB(0, 0, 0)


    # Save the PDF document
    pdf_canvas.save()
    
elif form == "oralForm":
    print("Oral")
elif form == "Lungs":

    ## Lungs form variables from json file
    coughing = data['Lungs_form']['coughing']
    chest_pain = data['Lungs_form']['chest_pain']
    shortness_breath = data['Lungs_form']['shortness_breath']
    wheezing = data['Lungs_form']['wheezing']
    coughing_blood = data['Lungs_form']['coughing_blood']
    feel_tired = data['Lungs_form']['feel_tired']
    lung_weight_loss = data['Lungs_form']['lung_weight_loss']
    pneumonia = data['Lungs_form']['pneumonia']
    lung_high_temp = data['Lungs_form']['lung_high_temp']
    ache = data['Lungs_form']['ache']
    muscle_ache = data['Lungs_form']['muscle_ache']
    change_appearance = data['Lungs_form']['change_appearance']
    swallowing = data['Lungs_form']['swallowing']
    swelling_face_neck = data['Lungs_form']['swelling_face_neck']
    lung_loss_appetite = data['Lungs_form']['lung_loss_appetite']
    lung_bone_pain = data['Lungs_form']['lung_bone_pain']
    yellow_skin = data['Lungs_form']['yellow_skin']
    yellow_eyes = data['Lungs_form']['yellow_eyes']
    weakness_arm_leg = data['Lungs_form']['weakness_arm_leg']
    arm_leg_numbness = data['Lungs_form']['arm_leg_numbness']
    dizziness = data['Lungs_form']['dizziness']
    mouth_dryness = data['Lungs_form']['mouth_dryness']

    space = 10
    # Cancer Questions place
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 14)
    pdf_canvas.drawString(50, 280, 'Cancer Survey')
    pdf_canvas.setFont('Helvetica-Bold', 10)
    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(52, 260, 'Kidney Cancer Prediction Questions :')

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 240-space, '- Coughing :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(140, 240-space, coughing)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 210-space, '- Chest pain :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(145, 210-space, chest_pain)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 180-space, '- Shortness breath :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(177, 180-space, shortness_breath)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 150-space, '- wheezing :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(138, 150-space, wheezing)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 120-space, '- Coughing blood :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(170, 120-space, coughing_blood)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.showPage()

    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(70, 750-space, '- Feel tired :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(138, 750-space, feel_tired)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 720-space, '- Lung weight loss :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(175, 720-space, lung_weight_loss)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 690-space, '- Pneumonia :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(147, 690-space, pneumonia)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 660-space, '- Lung high temp :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(168, 660-space, lung_high_temp)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 630-space, '- ache :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(115, 630-space, ache)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 600-space, '- Muscle ache :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(158, 600-space, muscle_ache)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 570-space, '- Change appearance :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(195, 570-space, change_appearance)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 540-space, '- Swallowing :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(145, 540-space, swallowing)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 510-space, '- Swelling face neck :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(185, 510-space, swelling_face_neck)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 480-space, '- Lung loss appetite :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(183, 480-space, lung_loss_appetite)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 450-space, '- Lung bone pain :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(170, 450-space, lung_bone_pain)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 420-space, '- Yellow skin :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(145, 420-space, yellow_skin)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 390-space, '- Yellow eyes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(149, 390-space, yellow_eyes)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 360-space, '- Weakness arm leg :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(186, 360-space, weakness_arm_leg)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 330-space, '- Arm leg numbness :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(186, 330-space, arm_leg_numbness)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 300-space, '- Dizziness :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(140, 300-space, dizziness)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawString(70, 270-space, '- Mouth Dryness :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(167, 270-space, mouth_dryness)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    # Create a new page in the PDF document
    pdf_canvas.showPage()

    ## Image variables from json file

    cancer = data['image_model']['cancer_type']
    cancer_accuracy = data['image_model']['cancer_accuracy']
    cancer_notes = data['image_model']['notes']

    # Add content to the new page
    pdf_canvas.setFillColor(colors.darkgreen)
    pdf_canvas.setFont('Helvetica-Bold', 16)
    pdf_canvas.drawString(50, 710, 'X-Ray Image')
    pdf_canvas.setFont('Helvetica', 14)

    pdf_canvas.setFillColorRGB(0, 0, 0)
    pdf_canvas.drawImage('images\\brain_glioma_0009.jpg', 55, 430, width=300, height=250)
    pdf_canvas.drawString(55, 380, '- Cancer Type :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(155, 380, cancer)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(55, 350, '- Accuracy :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(135, 350, cancer_accuracy)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    pdf_canvas.drawString(55, 320, '- Notes :')
    pdf_canvas.setFillColor(colors.firebrick)
    pdf_canvas.drawString(115, 320, cancer_notes)
    pdf_canvas.setFillColorRGB(0, 0, 0)

    # Save the PDF document
    pdf_canvas.save()
elif form == "lymphForm":
    print("Lymph")
