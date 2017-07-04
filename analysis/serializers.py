from rest_framework import serializers

from analysis.models import Analysis, Vector, MessGroese


class VectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vector
        fields = '__all__'


class MessgroesseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessGroese
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):
    vectors = VectorSerializer(many=True, read_only=True)
    messgroesen = MessgroesseSerializer(many=True, read_only=True)

    class Meta:
        model = Analysis
        fields = '__all__'
