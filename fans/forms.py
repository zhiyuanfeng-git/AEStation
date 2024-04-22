from django.forms import ModelForm,Form,FileField
from .models import FansModel

class FansForm(ModelForm):
    class Meta:
        model = FansModel
        fields = ("email","first_name","middle_name","last_name",)

class UploadForm(Form):
    pass