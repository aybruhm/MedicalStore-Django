from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,\
    AuthenticationForm


# class NoteCreateForm(forms.ModelForm):
#     """"
#     This class creates a note.
#     """
#     class Meta:
#         model = Note
#         fields = ['title', 'thought']
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control user_input',
#                 'id': 'validationCustomUsername',
#                 'aria-describedby': 'inputGroupPrepend',
#                 'required': "true",
#                 }
#             ),
#             'thought': forms.Textarea(attrs={
#                 'class': 'form-control edit_textarea',
#                 'id': 'editThought',
#                 'rows': '3',
#                 }
#             )
#         }

class CreateUserForm(UserCreationForm):
    """
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given 
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword2',
            'required': 'true',
            }
        ),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        ),
    }


class LogUserForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with no privileges, from the given 
    username and password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        )
    )


# class UpdateProfileForm(forms.ModelForm):
#     """
#     This form updates a user profile, from the given 
#     bio and profile_picture fields.
#     """
#     profile_picture = forms.FileField()
#     class Meta:
#         model = Profile
#         fields = ['bio', 'profile_picture']
#         widgets = {
#             'bio': forms.Textarea(attrs={
#                 'class': 'form-control edit_textarea',
#                 'id': 'editBio',
#                 'rows': '3',
#             }
#         )
#     }


class UpdateUserForm(forms.ModelForm):
    """
    This form updates a user, from the given 
    username field.
    """
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    }