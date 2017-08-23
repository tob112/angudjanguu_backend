from rest_framework import serializers

from kicker.models import Playa, Team, Match


class PlayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playa
        fields = ('playa_name', 'goals', 'victorys', 'defeats', 'own_goals')


class TeamSerializer(serializers.ModelSerializer):
    playas = PlayaSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('team_name', 'playas', 'victorys', 'defeats', 'goals', 'victory_percentage', 'own_goals')


class MatchSerializer(serializers.ModelSerializer):
    team_1 = TeamSerializer(many=False, read_only=True)
    team_2 = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = Match
        fields = ('datum', 'team_1', 'team_2', 'goals_team_1', 'goals_team_2', 'winner', 'loser', 'excuse')
