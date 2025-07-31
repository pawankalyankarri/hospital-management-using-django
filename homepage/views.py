from django.shortcuts import render, redirect
from django.views import View
from .models import Doctors, Patients,Doc_slots,SlotsAppointments
from datetime import datetime,timedelta,date
from django.http import HttpResponse


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
hepatologist = [
    "Cirrhosis",
    "liver cancer",
    "Hepatitis",
    "Alcoholic Hepatitis",
    "ALD",
    "Fatty liver disease ",
    "Hepatitis (A, B, C, D, E)",
    "Wilson's disease",
]
nephrologist = [
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
orthopedist = [
    "Arthritis",
    "Fractures",
    "Bursitis",
    "Hip Fracture",
    "Low Back Pain",
    "Foot Pain and Problems",
    "Hand Pain and Problems",
    "Knee Pain and Problems",
    "Neck Pain and Problems",
    "Shoulder Pain and Problems",
]
allergist = [
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
    "ophthalmologist": ophthalmologist[:6],
    "gastroenterologist": gastroenterologist[:6],
    "hepatologist": hepatologist[:6],
    "nephrologist": nephrologist[:6],
    "orthopedist": orthopedist[:6],
    "allergist": allergist[:6],
}
all_diseases = {
    "cardiology": cardiology,
    "neurology": neurology,
    "dermatology": dermatology,
    "ophthalmologist": ophthalmologist,
    "gastroenterologist": gastroenterologist,
    "hepatologist": hepatologist,
    "nephrologist": nephrologist,
    "orthopedist": orthopedist,
    "allergist": allergist,
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
            elif pdisease in neurology:
                doc_info = Doctors.objects.get(doc_spe="neurology")
            elif pdisease in dermatology:
                doc_info = Doctors.objects.get(doc_spe="dermatology")
            elif pdisease in ophthalmologist:
                doc_info = Doctors.objects.get(doc_spe = 'ophthalmologist')
            elif pdisease in gastroenterologist:
                doc_info = Doctors.objects.get(doc_spe = 'gastroenterologist')
            elif pdisease in hepatologist:
                doc_info = Doctors.objects.get(doc_spe = 'hepatologist') 
            elif pdisease in nephrologist:
                doc_info = Doctors.objects.get(doc_spe = 'nephrologist')
            elif pdisease in orthopedist:
                doc_info = Doctors.objects.get(doc_spe = 'orthopedist')
            elif pdisease in allergist:
                doc_info = Doctors.objects.get(doc_spe = 'allergist')
                
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
      
        
        input_time = req.POST['time']
        time = datetime.strptime(input_time,'%H:%M')
        def generate_slots(start_time,slot_duration):
            slots = []
            current = start_time
            for _ in range(10):
                slot = current.time()
                slots.append(slot)
                current+=slot_duration
                
            current +=(timedelta(minutes=120))   
            for _ in range(5):
                slot = current.time()
                slots.append(slot)
                current+=slot_duration
                
            return slots
        
        res = generate_slots(time,timedelta(minutes=20))
        print(res)
       
        
        dname = req.POST["dname"]
        dmobile = req.POST["dmobile"]
        dgender = req.POST["gender"]
        dage = int(req.POST["dage"])
        dspec = req.POST["dspec"]
        d_img = req.FILES['doc_img']
        Doctors.objects.create(
            doc_name=dname,
            doc_spe=dspec,
            doc_mobile=dmobile,
            doc_gender=dgender,
            doc_age=dage,
            doc_img = d_img
            
        )
        doc_details = Doctors.objects.get(doc_mobile = dmobile)
        it = iter(res)
        Doc_slots.objects.create(
                  slot1 = next(it),
                  slot2 = next(it),
                  slot3 = next(it),
                  slot4 = next(it),
                  slot5 = next(it),
                  slot6 = next(it),
                  slot7 = next(it),
                  slot8 = next(it),
                  slot9 = next(it),
                  slot10 = next(it),
                  slot11 = next(it),
                  slot12 = next(it),
                  slot13 = next(it),
                  slot14 = next(it),
                  slot15 = next(it),
                  doc_id = doc_details
                  )
        SlotsAppointments.objects.create(doc_id = doc_details)
       
        
        return redirect("homeurl")


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
    

class DoctorSlots(View):
    def get(self,req,pk):
        doc_details = Doctors.objects.get(doc_id = pk)
        doc_slots_details = Doc_slots.objects.get(doc_id = doc_details)
        today_date = date.today()
        max_date = today_date+timedelta(days=30)
        date_min_max = {
            'min':today_date,
            'max':max_date
        }
        slots = [getattr(doc_slots_details,f'slot{i}').strftime('%I:%M %p') for i in range(1,16)]
        
        
        return render(req,'home/doc_slots.html',{'doc':doc_details,'slots':slots,'all_diseases':all_diseases,'date':date_min_max})
    
    def post(self,req,pk):
        # print(req.POST)
        # print(pk)
        slot_time_str = req.POST['slot']
        slot_time = datetime.strptime(slot_time_str,'%I:%M %p').time()
        date_str = req.POST['date']
        slot_date = datetime.strptime(date_str,'%Y-%m-%d').date()

        disease_type = req.POST['disease']
        #Doc_slots.objects.create(doc_id = pk)
        # here it for doctors object to assign foreign key values
        doc_details = Doctors.objects.get(doc_id = pk)
        docslots_details = Doc_slots.objects.get(doc_id = pk)
        
        
        
        
        
        
        print(req.POST)
        print('if before ',docslots_details)
        if not docslots_details:
            # Doc_slots.objects.create(doc_id = pk)
            # docslots_details = Doc_slots.objects.filter(doc_id = pk).first()
            print('doctor dont have slots you need to develop it')
        # print(docslots_details.slot1)
        print(docslots_details)
        for i in range(1,16):
            slot_no = f'slot{i}' # slot_no means slot1,slot2...etc
            slotTime = getattr(docslots_details,slot_no)
            if slotTime == slot_time:
                break
                
        slots_table_ddetails = SlotsAppointments.objects.filter(doc_id = pk)
        print('slotno',slot_no)
        print(slots_table_ddetails)
        if not(slots_table_ddetails):
            # here doctor don't have slots in slotsappointments table so we need to create that
            SlotsAppointments.objects.create(doc_id = doc_details,slot_date = slot_date)
            slots_table_ddetails = SlotsAppointments.objects.filter(doc_id = pk)
            print('doctor slots created')
        print('slots_table_ddetals',slots_table_ddetails)
        
        for i in slots_table_ddetails:
            # here if date is matched to user selected date then i check for slotno
            if i.slot_date == slot_date:
                print('date matched')
                print(i.slot_date)
                # here if the slot is not booked then only book slot 
                if getattr(i,slot_no) == 'booked':
                    print('it is already booked')
                    print('breaking')
                    #return render(req,'message.html',{'url':'appointmenturl+{pk}','msg':'already Booked Choose another time'})
                    # return redirect('doc_slots/{pk}')
                    return redirect(f'/doc_slots/{pk}/')
                else:
                    setattr(i,slot_no,'booked') # here i am booking slot 
                    i.save()    # here iam saving it
                    print('now booking')
                    print('breaking')
                    return HttpResponse('appointment booked')
            else:
                print('slots_table_ddetail date is not matched')
            
            
            
        # # matched_date = getattr(slots_table_ddetails,)
        # slot_date_check = SlotsAppointments.objects.filter(slot_date = slot_date)
        # #here i am checking wheathere there is not date in slots table then i am creating new record with new date
        # if not(slot_date_check): 
        #     doc_details = Doctors.objects.get(doc_id = pk)
        #     SlotsAppointments.objects.create(doc_id = doc_details,slot_date = slot_date)
        #     slot_date_check = SlotsAppointments.objects.filter(slot_date = slot_date)
        #     slots_table_ddetails = SlotsAppointments.objects.filter(doc_id = pk)
            
            
            
        # print('for loop')
        # slot_date_flag = True
        # book_flag = True
        # for i in slots_table_ddetails:
        #     if i.slot_date == slot_date:
        #         slot_date_flag = False
        #         print(slot_date,'date is mathched')
        #         if getattr(i,slot_no) != 'booked':
        #             book_flag = False
        #             print('not booked')
        #             setattr(i,slot_no,'booked')
                    
        #         else:
        #             print('booked')
                    
            
        #if slot_date_flag:
                   
                
                
                
                
                
                
                
        # if not(slots_table_ddetails):
        #     SlotsAppointments.objects.create()
        
        # print(req.POST)
        
        # print('slot detals',slots_table_ddetails.slot_date)
        # print('slot date check',slot_date_check)
        # if slots_table_ddetails.slot_date == slot_date:
        #     print('slot_date matched')
        #     if getattr(slots_table_ddetails,slot_no) != 'booked':
        #         setattr(slots_table_ddetails, slot_no, "booked")
        #         print('booking sucess')
        #     else:
        #         print('already booked')
        # else:
        #     setattr(slots_table_ddetails,'slot_date', date_str)
        #     setattr(slots_table_ddetails, slot_no, "booked")
        # slots_table_ddetails.save()
        
        # print(slot_date)
        # print(date_str)
        # print(slot_no)
        
                
        return redirect('patientopurl')
        