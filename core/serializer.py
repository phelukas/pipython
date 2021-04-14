from rest_framework import serializers
from core.models import Post as Posts


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ('conteudo', 'criado_por',)


class PostCreateSerializer(serializers.ModelSerializer):

    criado_por = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Posts
        fields = ('conteudo', 'criado_por',)

    def create(self, validated_data):
        u = Posts.objects.create(
            criado_por=validated_data['criado_por'],
            conteudo=validated_data['conteudo']
        )
        u.save()
        return u
