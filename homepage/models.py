from django.db import models

# Create your models here.

    
    
class Doctors(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=30)
    doc_spe = models.CharField(max_length=40)
    doc_gender = models.CharField(max_length=10)
    doc_mobile = models.CharField(max_length=17)
    doc_age = models.IntegerField()
    doc_img = models.ImageField(upload_to='images/',null=True)
       
    def __str__(self):
        return self.doc_name
    
    
    


class Doc_slots(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot1 = models.TimeField()
    slot2 = models.TimeField()
    slot3 = models.TimeField()
    slot4 = models.TimeField()
    slot5 = models.TimeField()
    slot6 = models.TimeField()
    slot7 = models.TimeField()
    slot8 = models.TimeField()
    slot9 = models.TimeField()
    slot1 = models.TimeField()
    slot10 = models.TimeField()
    slot11 = models.TimeField()
    slot12 = models.TimeField()
    slot13 = models.TimeField()
    slot14 = models.TimeField()
    slot15 = models.TimeField()
    doc_id = models.ForeignKey(Doctors,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.doc_id.doc_spe
    
    
class SlotsAppointments(models.Model):
    doc_id = models.ForeignKey(Doctors,on_delete=models.SET_NULL,null=True)
    slot_date = models.DateField(null=True)
    slot1 = models.TextField(default='')
    slot2 = models.TextField(default='')
    slot3 = models.TextField(default='')
    slot4 = models.TextField(default='')
    slot5 = models.TextField(default='')
    slot6 = models.TextField(default='')
    slot7 = models.TextField(default='')
    slot8 = models.TextField(default='')
    slot9 = models.TextField(default='')
    slot10 = models.TextField(default='')
    slot11 = models.TextField(default='')
    slot12 = models.TextField(default='')
    slot13 = models.TextField(default='')
    slot14 = models.TextField(default='')
    slot15 = models.TextField(default='')
    
    
    
    
class Patients(models.Model):
    pat_id = models.AutoField(primary_key=True)
    pat_name = models.CharField(max_length=30)
    pat_age = models.IntegerField()
    pat_gender = models.CharField(max_length=15)
    pat_address = models.CharField(max_length=50)
    pat_mobile = models.CharField(max_length=17)
    pat_problem = models.CharField(max_length=30,null=True)
    doctor_id = models.ForeignKey(Doctors,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.pat_name