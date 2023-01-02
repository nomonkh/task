from django import forms
from .models import TaskModel, ExecutorModel


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = ['time_taken', 'time_of_day', 'name_of_task', 'status', 'confirmation', 'executor']

        widgets = {
            'time_taken': DateInput()
        }


class TaskUpdateForm(forms.ModelForm):
    # time_taken = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = TaskModel
        fields = ['confirmation', 'status']


class ExecutorForm(forms.ModelForm):
    class Meta:
        model = ExecutorModel
        fields = ['first_name', 'second_name', 'third_name', 'phone', 'sector']