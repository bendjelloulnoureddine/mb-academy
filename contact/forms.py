from django import forms 

from contact.models import Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model   = Contact
        # exclude = ('email',) 
        fields = [
                'name',
                'title',
                'email',
                'description'
                ]        
