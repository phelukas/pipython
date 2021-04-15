from rest_framework import serializers
from core.models import Post as Posts


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'

    def to_representation(self, instance):
        representation = {
            'Conteúdo': instance.conteudo,
            'Autor': instance.criado_por.formt_nome,
            'Data da criação': instance.formt_criacao
        }
        return representation


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ('conteudo', 'criado_por',)

    def to_representation(self, instance):
        representation = {
            'Conteúdo': instance.conteudo,
            'Autor': instance.criado_por.formt_nome,
        }
        return representation


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

    def to_representation(self, instance):
        representation = {
            'Conteúdo': instance.conteudo,
            'Autor': instance.criado_por.formt_nome,
        }
        return representation
