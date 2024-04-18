from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models.user import UserModel

class UserModelCreationForm(UserCreationForm):
    class Meta():
        model = UserModel
        fields = ('email',)

class UserModelChangeForm(UserChangeForm):
    class Meta():
        model = UserModel
        fields = ('email',)