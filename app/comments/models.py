from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # User : Comment = 1 : N
    # User -> Comment, Comment, Comment.. (가능)
    # Comment -> User, User, User... (불가능)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Video : Comment = 1 : N
    # Video -> Comment, Comment, Comment... (가능)
    # Comment -> Video(잇섭), Video(영알남), Video(아로치카) (불가능)

    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    # 대댓글
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)