from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models.user import UserModel

class UserModelCreationForm(UserCreationForm):
    required_css_class = 'required'
    class Meta():
        model = UserModel
        fields = ('email',"first_name","last_name",)

class UserModelChangeForm(UserChangeForm):
    class Meta():
        model = UserModel
        fields = ('email',)