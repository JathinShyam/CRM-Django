from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = ('<span class="form-text text-muted"><small>Required. 150 characters or fewer. '
                                     'Letters, digits and @/./+/-/_ only.</small></span>')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = ('<ul class="form-text text-muted small"><li>Your password can\'t be too similar '
                                      'to your other personal information.</li><li>Your password must contain at '
                                      'least 8 characters.</li><li>Your password can\'t be a commonly used '
                                      'password.</li><li>Your password can\'t be entirely numeric.</li></ul>')

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = ('<span class="form-text text-muted"><small>Enter the same password as before, '
                                      'for verification.</small></span>')


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    email = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
                            label="")
    phone = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
                            label="")
    address = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
                              label="")
    city = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control"}),
                           label="")
    state = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "form-control"}),
                            label="")
    pincode = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={"placeholder": "Pincode", "class": "form-control"}),
                              label="")

    class Meta:
        model = Record
        exclude = ("user",)


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True, label="Subject")
    body = forms.CharField(widget=forms.Textarea, required=True, label="Body")
    recipient_email = forms.CharField(required=True, label="Recipient Email")
    attachment = forms.FileField(required=False, label="Attachment")

    def clean(self):
        cleaned_data = super().clean()
        attachment = cleaned_data.get("attachment")

        # Ensure that the attached file is not too large
        if attachment:
            max_size = 15 * 1024 * 1024  # 15 MB (adjust as needed)
            if attachment.size > max_size:
                raise forms.ValidationError("The attached file is too large. Maximum size is 5 MB.")

        return cleaned_data
    
    # forms.py


class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'type': 'search',
            'placeholder': 'Search',
            'aria-label': 'Search'
        })
    )