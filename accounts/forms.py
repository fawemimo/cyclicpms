from django import forms
from .models import User, OtpCode


class HRMRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "class": "form-control",
            }
        )
    )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ["email","password"]

    def __init__(self, *args, **kwargs):
        super(HRMRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Enter Email Address"
        # self.fields["username"].widget.attrs["placeholder"] = "Enter Username"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super(HRMRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        email = cleaned_data.get("email")
        if password != password2:
            raise forms.ValidationError("Password does not match!")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Check Error"
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone_number")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


# for otpcode forms


class OtpCodeForm(forms.ModelForm):
    otp = forms.CharField(
        max_length=6, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "OTP code"})
    )

    class Meta:
        model = OtpCode
        fields = ("otp",)
        widgets = {
            "otp": forms.TextInput(attrs={"class": "form-control", "placeholder": "OTP code"}),
        }


# for login form


user_type_choices = ((1, "is_employee"), (2, "is_admin"), (3, "is_ceo"), (4, "is_accountant"), (5, "is_auditor"))


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"type": "email", "class": "form-control", "placeholder": "email"})
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={"type": "password", "class": "form-control", "placeholder": "Password"})
    )


class UserConfirmForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("user_type",)


# for users to update their profile pics
# class ProfileUpdateForm(forms.ModelForm):
#     user = forms.CharField( max_length=100, required=True, widget=forms.TextInput(attrs={'type':'hidden'}))
#     class Meta:
#         model = Profile
#         fields = ('user','image','date_updated')
