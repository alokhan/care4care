from django import forms
from django.utils.translation import ugettext_lazy as _
from main.models import User

from django.forms.extras import SelectDateWidget
import datetime

class CareRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label=_("Prénom"),)
    last_name = forms.CharField(label=_("Nom de famille"),)
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Mot de passe"))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Mot de passe (à nouveau)"))

    birth_date = forms.DateField(label=_("Date de naissance (DD/MM/YYYY)"),
                                 widget=SelectDateWidget(years=range(datetime.date.today().year-100, \
                                                                     datetime.date.today().year)),
                                 initial=datetime.date.today())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'languages', \
         'how_found', 'birth_date', 'phone_number', 'mobile_number', 'address', 'city', 'postal_code', 'country']


    def clean_username(self):
        """
        Validate that the username DoesNotExist
        """
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("Cet utilisateur existe déjà dans notre système. Veuillez utiliser utiliser le formulaire 'Mot de passe perdu' si vous êtes déjà enregistré."))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Les mots de passe ne sont pas identiques."))
        return self.cleaned_data

class ProfileManagementForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'address', 'city', 'languages', 'country']
