from django.forms import ModelForm
from users.models import CustomUser

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_pic', 'username')
