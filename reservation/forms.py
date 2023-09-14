from django import forms

from reservation.models import Reservation


class SearchRoomForm(forms.Form):
    
    location = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs=
                                {'class': 'form-control',
                                "placeholder": "Enter Location"})
                               )
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    
class ReserveRoomModelForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ("check_in", "check_out", "adults", "children")
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # 'adults': forms.Select(attrs={'class': 'form-select'}),
            # "children": forms.Select(attrs = {"class": "form-select"}),
        }