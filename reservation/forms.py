from django import forms


class SearchRoomForm(forms.Form):
    
    location = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs=
                                {'class': 'form-control',
                                "placeholder": "Enter Location"})
                               )
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))