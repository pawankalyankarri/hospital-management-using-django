from django.contrib import admin
from .models import Doctors,Patients,Doc_slots
# Register your models here.

admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Doc_slots)