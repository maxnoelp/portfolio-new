from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Name"},
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "E-Mail"},
        ),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Message"},
        ),
    )
