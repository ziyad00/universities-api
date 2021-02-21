from rest_framework import serializers
from .models import QA, Answer
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class TagsField(serializers.Field):
    """ custom field to serialize/deserialize TaggableManager instances.
    """
    def to_representation(self, value):
        """ in drf this method is called to convert a custom datatype into a primitive,
        serializable datatype.

        In this context, value is a plain django queryset containing a list of strings.
        This queryset is obtained thanks to get_tags() method on the Task model.

        Drf is able to serialize a queryset, hence we simply return it without doing nothing.
        """
        return value

    def to_internal_value(self, data):
        """ this method is called to restore a primitive datatype into its internal
        python representation.

        This method should raise a serializers.ValidationError if the data is invalid.
        """
        return data

class AnswerSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True, source='user.id')
    #user = UserSerializer()  # May be an anonymous user.
    #user = serializers.Field(source='user.username')

    class Meta:
        model=Answer
        fields='__all__'
        #exclude = ('user',)



class QASerializer(TaggitSerializer, serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)

    #comments = serializers.StringRelatedField(many=True)
    answers = AnswerSerializer(many=True, read_only=True)
    #tags = TagsField(source="get_tags")
    tags = TagListSerializerField()

    #def create(self, validated_data):
        # using "source=get_tags" drf "thinks" get_tags is a real field name, so the
        # return value of to_internal_value() is used a the value of a key called "get_tags" inside validated_data dict. We need to remove it and handle the tags manually.
        #tags = validated_data.pop("get_tags")
        #qa = QA.objects.create(**validated_data)
        #qa.tags.add(*tags)

        #return qa
        
    class Meta:
        model=QA
        fields='__all__'
        #fields= ('id','user','image','description','created')
        #exclude = ('users_like', 'total_likes')
        #read_only_fields = ('users_like', 'total_likes')