from django.db import models

class Line2(models.Model):
    name = models.CharField(max_length=50)
    stations = models.TextField()            # 역 목록
    description = models.TextField()         # 설명

    def __str__(self):  #admin에서 글 제목을 표시
        return self.name
# Create your models here.