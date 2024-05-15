from django import forms
from .models import RegisterReservation, RegisterAppointment

## Registra Reserva do item   
class RegisterReservationForm(forms.ModelForm):
    booking_date = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    booking_time = forms.TimeField(
        input_formats=['%H:%M'], 
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
    )  

    class Meta:
        model = RegisterReservation
        fields = ['name', 'email', 'phone', 'booking_date', 'booking_time']
        exclude = ('item','create_at')
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'



## Registra Agendamentos
class RegisterAppointment(forms.ModelForm):
    booking_date = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    booking_time = forms.TimeField(
        input_formats=['%H:%M'], 
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
    )  

    class Meta:
        model = RegisterAppointment
        fields = ['name', 'email', 'phone', 'booking_date', 'booking_time', 'comments']
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'