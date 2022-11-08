from django import forms
from .models import Note
# creating a form
class NoteForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Note

        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'formfield',
            'placeholder': 'Note Title',
            }),
            'description': forms.Textarea(attrs={
            'class': 'formfield',
            'placeholder': 'Note Description',
            'rows' : 25,
            'cols' : 60,
            }),
}
