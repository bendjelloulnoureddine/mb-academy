from django import forms 

from contact.models import Contact

class ContactModelForm(forms.ModelForm):
    name = forms.CharField(
                    label="Nom Complet", 
                    widget=forms.TextInput(
                                attrs={
                                   "class": "form-control",
                                }
                        )
                    )

    title = forms.CharField(
                    label="Objet", 
                    widget=forms.TextInput(
                                attrs={
                                   "class": "form-control",
                                }
                        )
                    )

    email = forms.EmailField(
                    label="Email", 
                    widget=forms.TextInput(
                                attrs={
                                   "class": "form-control",
                                   "type": "email"
                                }
                        )
                    )

    description = forms.EmailField(
                    label="Votre Message", 
                    widget=forms.Textarea(
                                attrs={
                                   "class": "form-control",
                                   "type": "email"
                                }
                        )
                    )
    class Meta:
        model   = Contact
        # exclude = ('email',) 
        fields = [
                'name',
                'title',
                'email',
                'description'
                ]        
