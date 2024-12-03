from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    email_address = forms.EmailField(label='Ваш email', max_length=150)
    phone = forms.CharField(label='Номер телефона', max_length=15)
    experience = forms.CharField(label='Опыт работы', widget=forms.Textarea)