from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User

# from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User   <- 이것도 되긴하는데 이렇게 안 씀
        model = get_user_model()
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # model = User   <- 이것도 되긴하는데 이렇게 안 씀
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)