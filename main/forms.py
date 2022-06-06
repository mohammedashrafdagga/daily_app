from django import forms
from.models import DailyNotes


class DailyNotesForm(forms.ModelForm):

    class Meta:
        model = DailyNotes
        fields = ['title', 'descriptions', 'note_image', 'bacground_image']
