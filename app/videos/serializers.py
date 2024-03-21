from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):

    # Video:User -> Video(FK)라 User를 찾을 수 있음
    user = UserSerializer(read_only=True)    

    class Meta:
        model = Video
        fields = '__all__'        

class VideoDetailSerializer(serializers.ModelSerializer):

    # Video:User -> Video(FK)라 User를 찾을 수 있음
    user = UserSerializer(read_only=True)

    # Video:Comment -> Comment(FK)라 찾아야 하는 상황임
    # Reverse Accessor 를 사용(_set)해서 부모에 속한 자녀들을 모두 찾을 수 있다.
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'      