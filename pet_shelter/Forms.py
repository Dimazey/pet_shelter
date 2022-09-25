from django import forms

class GetToHomeForm(forms.Form):
    pk = forms.IntegerField(disabled=True, widget=forms.HiddenInput())
    pet_name = forms.CharField(label='Кличка животного', max_length=100, disabled=True)
    name = forms.CharField(label='Ваше Имя', max_length=120)
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    email = forms.EmailField(label='Адрес электронной почты')



    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

