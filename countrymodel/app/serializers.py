from rest_framework import serializers
from .models import Country, User, Blog
from .models import SampleModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_of_birth', 'bio', 'country']

    def get_country(self, obj):
        expand = self.context.get('expand', {})
        if 'country' in expand:
            return CountrySerializer(obj.country).data
        return obj.country.id if obj.country else None


class BlogSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_created_by(self, obj):
        expand = self.context.get('expand', {})
        if 'created_by' in expand:
            return UserSerializer(obj.created_by).data
        return obj.created_by.id

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = '__all__'