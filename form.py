from django import forms
from .views import *


class postform(forms.ModelForm):
    model='Post'
    fields={"title","authore","body","image"}