from django.forms import ModelForm

from apps.models import Email


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']