from django.db import models
from django.utils import timezone
from users.models import User
from users.models import Movie

class Problems(models.Model):
    Problems_id = models.IntegerField(max_length=20,help_text="问题id",verbose_name="问题id")
    Problems_contain = models.CharField(max_length=20, verbose_name='问题内容' , help_text="问题内容")
    class Meta:
        db_table = 'tb_problems'
        verbose_name = '问题咨询'
