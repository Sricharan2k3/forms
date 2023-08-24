from .models import Student
from django.core.validators import MinLengthValidator, EmailValidator, RegexValidator
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phoneNo']

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if len(name) <= 4:
    #         raise forms.ValidationError(
    #             "Name must have more than 4 characters.")
    #     return name

    phone_regex = r'^\d{10}$'

    name = forms.CharField(
        validators=[MinLengthValidator(limit_value=5, message="Hi")])

    email = forms.CharField(validators=[EmailValidator(message="Hello")])
    phoneNo = forms.IntegerField(validators=[
        RegexValidator(
            regex=phone_regex,
            message="Bye"
        )])
