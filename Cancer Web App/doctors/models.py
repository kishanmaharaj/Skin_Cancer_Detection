from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
#from django.urls import reverse

# Create your models here.

specialties = (
    ('select', 'Select'),
    ('aerospace_medicine', 'Aerospace Medicine'),
    ('allergies', 'Allergy and Immunology'),
    ('anaesthesia', 'Anaesthesia'),
    ('bariatric', 'Bariatric Surgery'),
    ('cardiologyInterventional', 'Cardiology - Interventional'),
    ('cardiologyNonInterventional', 'Cardiology - Non Interventional'),
    ('cardiologyVascular', 'Cardiothoracic And Vascular Surgery'),
    ('spinal', 'Centre For Spinal Diseases'),
    ('haematology&BMT', 'Clinical Haematology And BMT'),
    ('corneal', 'Corneal Transplant'),
    ('cmc', 'Critical Care Medicine'),
    ('dermatology', 'Dermatology And Cosmetology'),
    ('ent', 'Ear Nose Throat Head And Neck Surgery'),
    ('emergencyMedicine', 'Emergency Medicine'),
    ('endocrinology', 'Endocrinology'),
    ('generalSurgery', 'General Surgery'),
    ('infectius', 'Infectious Diseases'),
    ('internalMedicine', 'Internal Medicine'),
    ('ivf', 'In-Vitro Fertilisation (IVF)'),
    ('labMed', 'Laboratory Medicine'),
    ('liver', 'Liver Transplant & Hepatic Surgery'),
    ('maxillofacial', 'Maxillofacial Surgery'),
    ('medGas', 'Medical Gastroenterology'),
    ('medicalOncology', 'Medical Oncology'),
    ('minInvasiceGynecology', 'Minimally Invasive Gynecology'),
    ('neonatology', 'Neonatology'),
    ('nephrology', 'Nephrology'),
    ('neuroMod', 'Neuro Modulation'),
    ('diet', 'Nutrition & Dietetics'),
    ('neurology', 'Neurology'),
    ('neurosurgery', 'Neurosurgery'),
    ('obstetricsGynecology', 'Obstetrics And Gynecology'),
    ('ophthalmology', 'Ophthalmology'),
    ('orthpedics', 'Orthopedics & Joint Replacement'),
    ('painManage', 'Pain Management'),
    ('pediatric', 'Pediatric Surgery'),
    ('physio', 'Physiotherapy'),
    ('plastic', 'Plastic Surgery'),
    ('psych', 'Psychiatry'),
    ('pulmonology', 'Pulmonology'),
    ('renal', 'Renal Transplant'),
    ('reproductive&ivf', 'Reproductive Medicine & IVF'),
    ('rheumatology', 'Rheumatology'),
    ('robotic', 'Robotic Surgery'),
    ('skinCancer', 'Skin Cancer'),
    ('urology', 'Urology'),
    ('vascular', 'Vascular and endovascular surgery'),
)


class Doctor(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default='Username')
    email = models.EmailField(default='123@gmail.com')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    specialization = models.CharField(max_length=60, choices=specialties, default='select')

    def __str__(self):
        return self.name
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.save()
'''

'''
class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)



    def __str__(self):
        return self.name
'''
