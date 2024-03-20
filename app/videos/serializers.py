from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer

class VideoSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
        # depty = 1 # 이건 비번(hash)까지 노출시키니 테스트때 말고는 절대 사용금물, 배포때는 삭제하자