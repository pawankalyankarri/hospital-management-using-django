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
        return self.doc_spe
    
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