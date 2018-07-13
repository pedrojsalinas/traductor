from django import forms

class TraductorForm(forms.Form):
    texto = forms.CharField(widget=forms.Textarea(            attrs={
                'class':'form-control',
            }),required=True,label=None)
    idm = (('en', 'Ingles',), ('ja', 'Japones',),('de', 'Aleman'), ('es', 'Español'))
    idioma = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=idm)
