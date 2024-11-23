from django import forms


# Set the label for the 'name' field
class CreateNewList(forms.Form):
    name = forms.CharField(label="NAME ", max_length=200)
    



