from django import forms
import datetime
class ImageForm(forms.Form):
    image = forms.ImageField()

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    image = forms.ImageField()
    price = forms.IntegerField()
    entering_date = forms.DateField(initial=datetime.date.today)