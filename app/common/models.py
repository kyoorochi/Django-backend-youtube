from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 생성된 일시 (고정)
    updated_at = models.DateTimeField(auto_now=True) # 데이터가 업데이트 된 일시 (업데이트 할 때마다 계속 갱신됨)

    class Meta:
        abstract = True # DB에 테이블을 추가하지 않는다.