from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from doctors.models import Doctor
from .models import Profile
'''
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
'''
'''
type = [
    ('select', 'Select'),
    ('dr', 'Doctor'),
    ('pt', 'Patient'),
]
'''

specialties = [
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
]

class UserRegisterForm(UserCreationForm):
    #type = forms.ChoiceField(label='Register As?', widget=forms.Select(), choices=type, initial='select')
    type = forms.ChoiceField(label='Specialization', widget=forms.Select(), choices=specialties, initial='select')
    name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        #model = Doctor
        #fields = ['type', 'name', 'username', 'email', 'password1', 'password2']
        fields = ['name', 'username', 'email', 'password1', 'password2', 'type']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #model = Doctor
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
