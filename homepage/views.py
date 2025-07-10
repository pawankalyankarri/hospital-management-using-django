from django.shortcuts import render,redirect
from django.views import View
from .models import Doctors,Patients
# Create your views here.
img = [{'img':'heart1.png','text':'Heart & Minimally Invasive Cardiac Surgery'},{'img':'gastic.webp','text':'Gastroenterology & Invasive GI Surgery'},{'img':'neurology.jpg','text':'Neruology & Endoscopic Spine Centre'},{'img':'kidney.jpeg','text':'Kidney Care & Renal Transplantation'},{'img':'cancer.avif','text':'Cancer,Hematology & Bone Marrow Transplantation'},{'img':'orthopedic.jpg','text':'Orthopedics & and Joint Replacement Surgery'},{'img':'ambulence.jpg','text':'24/7 Empergency and Trauma Care'},{'img':'robotic joint.png','text':'Robotic Joint Replacement Surgery'},{'img':'lungs.jpg','text':'Interventional Pulmonology & Critical Care'},{'img':'liver.jpg','text':'Liver,HPB & Liver Transplantation'}]
doc_names = [{'img':'doc1.jpg'},{'img':'doc2.jpg'},{'img':'doc3.jpg'}]
cardiology = ['heartattack','heart','chest pain','heart strock','heart pain']
neurology = ["epilepsy", "multiple sclerosis", "Parkinson's disease", "brain tumors", "cerebral palsy", "Alzheimer","dementia"]
dermatology = ['eczema', 'psoriasis', 'acne', 'moles', 'fungal infections','itch','skin allergy']
all_diseases = {'cardiology':cardiology,'neurology':neurology,'dermatology':dermatology}

class Home(View):
    def get(self,req):
        
        return render(req,'home/home.html',{'images':img,'doc_names':doc_names})
    
class Patientop(View):
    def get(self,req):
        doc_obj = Doctors.objects.all()
        return render(req,'home/patientop.html',{'doc_obj':doc_obj})
    def post(self,req):
        print(req.POST)
        
        #'name': ['hari'], 'age': ['2'], 'gender': ['other'], 'address': ['hyderabad'], 'disease': ['Cardiology'], 'mobile': ['987654321'], 'payment': ['on']}>
        pname = req.POST['name']
        page = int(req.POST['age'])
        pgender = req.POST['gender']
        paddress = req.POST['address']
        pdisease = req.POST['disease']
        pmobile = req.POST['mobile']
        if 'payment' in req.POST:
            if pdisease in cardiology:
                doc_info = Doctors.objects.get(doc_spe = 'cardiology')
                Patients.objects.create(pat_name = pname,pat_age = page,pat_gender = pgender,pat_address = paddress,pat_mobile= pmobile,pat_problem = pdisease,doctor_id = doc_info)
            elif pdisease in neurology:
                doc_info = Doctors.objects.get(doc_spe = 'neurology')
                Patients.objects.create(pat_name = pname,pat_age = page,pat_gender = pgender,pat_address = paddress,pat_mobile= pmobile,pat_problem = pdisease,doctor_id = doc_info)
            elif pdisease in dermatology:
                doc_info = Doctors.objects.get(doc_spe = 'dermatology')
                Patients.objects.create(pat_name = pname,pat_age = page,pat_gender = pgender,pat_address = paddress,pat_mobile= pmobile,pat_problem = pdisease,doctor_id = doc_info)
            
                
                
        return redirect('patientopurl')
    
class AddDoctor(View):
    def get(self,req):
        return render(req,'home/doctors.html')
    def post(self,req):
        print(req.POST)
        dname = req.POST['dname']
        dmobile = req.POST['dmobile']
        dgender = req.POST['gender']
        dage = int(req.POST['dage'])
        dspec = req.POST['dspec']
        Doctors.objects.create(doc_name = dname,doc_spe = dspec,doc_mobile = dmobile,doc_gender = dgender,doc_age = dage)
        return redirect('adddoctorurl')
    
class Appointments(View):
    def get(self,req):
        docs = Doctors.objects.all()
        # docAndDis = []
        # for doc in docs:
        #     for disease in all_diseases:
        #         if doc.doc_spe == disease:
        #             docAndDis.append(doc.doc_spe+)
                    
        return render(req,'home/appointments.html',{'docs':docs,'all_diseases':all_diseases})