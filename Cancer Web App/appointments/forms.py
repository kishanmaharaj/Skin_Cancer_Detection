from django.forms import ModelForm, DateInput
from .models import Event
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
      'end_time': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
    }
    fields = ['title', 'description', 'start_time', 'end_time']


  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%d/%m/%Y %H:%M',)
    self.fields['end_time'].input_formats = ('%d/%m/%Y %H:%M',)
