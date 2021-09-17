from django import forms
from django.forms import fields
from .models import MPjKnr
 
class KintaiForm(forms.ModelForm):
    class Meta:
        model = MPjKnr
        fields = ('pj_no', 'pj_nm', 'pj_st_time', 'rst_st_time', 'rst_ed_time', 'pj_ed_time', 'act_hrs', )

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)

    #    self.fields['name'].widget.attrs['class']='form-control col-9'