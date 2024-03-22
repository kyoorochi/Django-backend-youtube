from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

# User : FK
# Video : FK
# Reaction : Like, Dislike, Cancel -> choice
class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = 1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    
    @staticmethod # ORM depth2
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )

        return reactions