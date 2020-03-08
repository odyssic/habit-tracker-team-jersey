from django import forms
from .models import User, Habit, Tracker


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('habit', 'goal', 'goal_units', 'timeframe')


class ProgressForm(forms.ModelForm):

    class Meta:
        model = Tracker
        fields = ('input_units',)
