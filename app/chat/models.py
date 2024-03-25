from django.db import models
from common.models import CommonModel

# Create your models here.
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # SET_NULL - sender null 값으로 두겠다는 뜻. 1번 -> 계정삭제 -> null
    sender = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True) # 유저계정이 삭제되면 채팅은 남기되 발신자는 알 수 없음 처리
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)