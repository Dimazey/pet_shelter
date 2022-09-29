from django import forms

class GetToHomeForm(forms.Form):
    pk = forms.IntegerField(disabled=True, widget=forms.HiddenInput())
    pet_name = forms.CharField(label='Кличка животного', max_length=100, disabled=True)
    name = forms.CharField(label='Ваше Имя', max_length=120)
    name.widget.attrs.update({'class': 'form-control', 'required': 'required'})
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    message.widget.attrs.update({'class': 'form-control', 'required': 'required'})
    email = forms.EmailField(label='Адрес электронной почты')
    email.widget.attrs.update({'class': 'form-control', 'required': 'required'})




