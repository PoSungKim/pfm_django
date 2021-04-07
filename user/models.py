from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='유저명')

    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')

    register_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록시간')

    # Admin 페이지에서 class가 문자열로 변환됐을 때, 어떻게 표현이 될지 설정
    def __str__(self):
        return self.username

    class Meta:  # table명
        db_table = 'User'
        verbose_name = "서비스 사용자"
        verbose_name_plural = "서비스 사용자"
