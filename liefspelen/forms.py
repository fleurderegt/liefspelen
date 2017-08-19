from django import forms

from .models import Game, Season, Environment

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('title', 'text','categories','tags','seasons','environments','min_age','max_age','min_players','max_players', 'materials')

class SearchForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('title', 'text','categories','tags','seasons','environments','min_age','max_age','min_players','max_players', 'materials', 'image')  