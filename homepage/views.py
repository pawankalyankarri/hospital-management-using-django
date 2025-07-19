from django.shortcuts import render, redirect
from django.views import View
from .models import Doctors, Patients
from datetime import datetime,timedelta


# Create your views here.
img = [
    {"img": "heart1.png", "text": "Heart & Minimally Invasive Cardiac Surgery"},
    {"img": "gastic.webp", "text": "Gastroenterology & Invasive GI Surgery"},
    {"img": "neurology.jpg", "text": "Neruology & Endoscopic Spine Centre"},
    {"img": "kidney.jpeg", "text": "Kidney Care & Renal Transplantation"},
    {"img": "cancer.avif", "text": "Cancer,Hematology & Bone Marrow Transplantation"},
    {"img": "orthopedic.jpg", "text": "Orthopedics & and Joint Replacement Surgery"},
    {"img": "ambulence.jpg", "text": "24/7 Empergency and Trauma Care"},
    {"img": "robotic joint.png", "text": "Robotic Joint Replacement Surgery"},
    {"img": "lungs.jpg", "text": "Interventional Pulmonology & Critical Care"},
    {"img": "liver.jpg", "text": "Liver,HPB & Liver Transplantation"},
]
doc_names = [{"img": "doc1.jpg"}, {"img": "doc2.jpg"}, {"img": "doc3.jpg"}]
cardiology = ["heartattack", "heart", "chest pain", "heart strock", "heart pain"]
neurology = [
    "epilepsy",
    "multiple sclerosis",
    "Parkinson's disease",
    "brain tumors",
    "cerebral palsy",
    "Alzheimer",
    "dementia",
]
ophthalmologist = [
    "Eyestrain",
    "Red Eyes",
    "Uveitis",
    "Night Blindness",
    "Colorblindness",
    "Blurred vision",
    "Dry Eyes",
    "Retinal Disorders",
    "Conjunctivitis",
    "Corneal Diseases",
    "Eyelid Problems",
]
gastroenterologist = [
    "Constipation",
    "Acid reflux",
    "Irritable bowel syndrome (IBS)",
    "Hemorrhoids",
    "acidity",
    "Diverticular disease",
    "Colitis",
    "Colon polyps and colon cancer",
    "Celiac disease",
    "Gastritis",
]
Hepatologist = [
    "Cirrhosis",
    "liver cancer",
    "Hepatitis",
    "Alcoholic Hepatitis",
    "ALD",
    "Fatty liver disease ",
    "Hepatitis (A, B, C, D, E)",
    "Wilson's disease",
]
Nephrologist = [
    "Glomerulonephritis",
    "Diagnosis",
    "Diabetes",
    "Kidney Stones",
    "Kidney Infections",
    "Nephrotic Syndrome",
    "Chronic Kidney Disease (CKD)",
    "Abrupt Kidney Impairment (AKI)",
    "Polycystic Kidney Disease (PKD)",
]
Orthopedist = [
    "Arthritis",
    "Fractures",
    "Bursitis",
    "Low Back Pain",
    "Foot Pain and Problems",
    "Hip Fracture",
    "Hand Pain and Problems",
    "Knee Pain and Problems",
    "Neck Pain and Problems",
    "Shoulder Pain and Problems",
]
Allergist = [
    "Rash",
    "Hair Dye Allergy",
    "Antibodies",
    "Wheat Allergy",
    "Dust Allergy",
    "food allergy",
     "Casein",
    
    "Allergens",
    "Egg Allergy",
    
]
dermatology = [
    "eczema",
    "psoriasis",
    "skin allergy",
    "acne",
    "moles",
    "fungal infections",
    "itch",
    
]
limited_all_diseases = {
    "cardiology": cardiology[:6],
    "neurology": neurology[:6],
    "dermatology": dermatology[:6],
    "Ophthalmologist": ophthalmologist[:6],
    "gastroenterologist": gastroenterologist[:6],
    "Hepatologist": Hepatologist[:6],
    "Nephrologist": Nephrologist[:6],
    "Orthopedist": Orthopedist[:6],
    "Allergist": Allergist[:6],
}
all_diseases = {
    "cardiology": cardiology,
    "neurology": neurology,
    "dermatology": dermatology,
    "Ophthalmologist": ophthalmologist,
    "gastroenterologist": gastroenterologist,
    "Hepatologist": Hepatologist,
    "Nephrologist": Nephrologist,
    "Orthopedist": Orthopedist,
    "Allergist": Allergist,
}

patient_reviews = [
    {
        "src": "https://www.youtube.com/embed/XWn8cil5Wrw?autoplay=1&controls=1",
        "name": "Sivaram",
        "review": "Very caring staff and excellent treatment. Felt safe and comfortable.",
    },
    {
        "src": "https://www.youtube.com/embed/39DMX-Hyl2Y?autoplay=1",
        "name": " Anjali P.",
        "review": "Clean hospital with friendly doctors. Great overall experience.",
    },
    {
        "src": "https://www.youtube.com/embed/N0X8y_4h8No?autoplay=1",
        "name": "Priya S.",
        "review": "Quick service and professional care. Highly recommended!",
    },
]


class Home(View):
    def get(self, req):

        return render(
            req,
            "home/home.html",
            {"images": img, "doc_names": doc_names, "reviews": patient_reviews},
        )


class Patientop(View):
    def get(self, req):
        # doc_obj = Doctors.objects.all()
        return render(req, "home/patientop.html", {"all_diseases": all_diseases})

    def post(self, req):
        print(req.POST)

        #'name': ['hari'], 'age': ['2'], 'gender': ['other'], 'address': ['hyderabad'], 'disease': ['Cardiology'], 'mobile': ['987654321'], 'payment': ['on']}>
        pname = req.POST["name"]
        page = int(req.POST["age"])
        pgender = req.POST["gender"]
        paddress = req.POST["address"]
        pdisease = req.POST["disease"]
        pmobile = req.POST["mobile"]
        if "payment" in req.POST:
            if pdisease in cardiology:
                doc_info = Doctors.objects.get(doc_spe="cardiology")
                Patients.objects.create(
                    pat_name=pname,
                    pat_age=page,
                    pat_gender=pgender,
                    pat_address=paddress,
                    pat_mobile=pmobile,
                    pat_problem=pdisease,
                    doctor_id=doc_info,
                )
            elif pdisease in neurology:
                doc_info = Doctors.objects.get(doc_spe="neurology")
                Patients.objects.create(
                    pat_name=pname,
                    pat_age=page,
                    pat_gender=pgender,
                    pat_address=paddress,
                    pat_mobile=pmobile,
                    pat_problem=pdisease,
                    doctor_id=doc_info,
                )
            elif pdisease in dermatology:
                doc_info = Doctors.objects.get(doc_spe="dermatology")
                Patients.objects.create(
                    pat_name=pname,
                    pat_age=page,
                    pat_gender=pgender,
                    pat_address=paddress,
                    pat_mobile=pmobile,
                    pat_problem=pdisease,
                    doctor_id=doc_info,
                )

        return redirect("patientopurl")


class AddDoctor(View):
    def get(self, req):
        return render(req, "home/doctors.html")

    def post(self, req):
        print(req.POST)
        # dname = req.POST["dname"]
        # dmobile = req.POST["dmobile"]
        # dgender = req.POST["gender"]
        # dage = int(req.POST["dage"])
        # dspec = req.POST["dspec"]
        # Doctors.objects.create(
        #     doc_name=dname,
        #     doc_spe=dspec,
        #     doc_mobile=dmobile,
        #     doc_gender=dgender,
        #     doc_age=dage,
        # )
        
        time = req.POST['time']
        time = datetime.strptime(time,'%H:%M')
        def generate_slots(start_time,slot_duration):
            slots = []
            current = start_time
            for _ in range(10):
                slot = current.strftime('%I:%M %p')
                slots.append(slot)
                current+=slot_duration
            return slots
        
        res = generate_slots(time,timedelta(minutes=20))
        print(res)
                
        
        
        
        
                
                
                
        
        return redirect("adddoctorurl")


class Appointments(View):
    def get(self, req):
        docs = Doctors.objects.all()
        # docAndDis = []
        # for doc in docs:
        #     for disease in all_diseases:
        #         if doc.doc_spe == disease:
        #             docAndDis.append(doc.doc_spe+)

        return render(
            req,
            "home/appointments.html",
            {"docs": docs, "all_diseases": limited_all_diseases},
        )


class OurDoctors(View):
    def get(self, req):
        docs = Doctors.objects.all()
        return render(req, "home/ourDoctors.html", {"docs": docs})
