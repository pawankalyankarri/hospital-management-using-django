from django.shortcuts import render,redirect
from django.views import View
from .models import Doctors,Patients
# Create your views here.
img = [{'img':'cardiology.jpg'},{'img':'dermatology.jpg'}]
doc_names = [{'img':'doc1.jpg'},{'img':'doc2.jpg'},{'img':'doc3.jpg'}]
cardiology = ['heartattack','heart','chest pain','heart strock','heart pain']
neurology = ["epilepsy", "multiple sclerosis", "Parkinson's disease", "brain tumors", "cerebral palsy", "Alzheimer","dementia"]
dermatology = ['eczema', 'psoriasis', 'acne', 'moles', 'fungal infections','itch','skin allergy']


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
    
# class Provides(View):
#     def get(self,req):
#         return render(req,'home/provides.html')