from rest_framework import serializers

from kicker.models import KickerProfile, Team, Match


class KickerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = KickerProfile
        fields = ('kicker_display_name', 'goals', 'victorys', 'defeats', 'goals_against')


class TeamSerializer(serializers.ModelSerializer):
    kicker_profiles = KickerProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('team_name', 'kicker_profiles', 'victorys', 'defeats', 'goals', 'victory_percentage', 'goals_against')


class MatchSerializer(serializers.ModelSerializer):
    team_1 = TeamSerializer(many=False, read_only=True)
    team_2 = TeamSerializer(many=False, read_only=True)

    class Meta:
        model = Match
        fields = ('datum', 'team_1', 'team_2', 'goals_team_1', 'goals_team_2', 'winner', 'loser')
