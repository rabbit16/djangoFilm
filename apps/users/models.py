from django.db import models
from django.utils import timezone

class Users:
    Users_id = models.CharField(max_length=20,help_text="用户id",verbose_name="用户id")
    Users_name = models.CharField(max_length=20, verbose_name='用户昵称' , help_text="用户昵称")
    Name = models.CharField(max_length=20, verbose_name='真实名称', help_text="真实名称")
    Users_sex = models.BooleanField(verbose_name="性别", help_text="性别", default=True)
    Users_email = models.CharField(max_length=20, verbose_name='用户邮箱', help_text="用户邮箱")
    Users_password = models.CharField(max_length=20, verbose_name='用户密码', help_text="用户密码")
    mobile = models.CharField(max_length=20, verbose_name='电话号码', help_text="电话号码")
    registration_date = models.CharField(max_length=20, verbose_name='注册日期', help_text="注册日期")
    ticketmanager = models.BooleanField(verbose_name="票务管理员", help_text="票务管理员", default=False)
    supermanager = models.BooleanField(verbose_name="超级管理员", help_text="超级管理员", default=False)
    buymanager = models.BooleanField(verbose_name="售票员", help_text="售票员", default=False)

    class Meta:
        db_table = 'tb_Users'
        verbose_name = '用户'
class Movie:
    Movie_id = models.CharField(max_length=20,help_text="电影id",verbose_name="电影id")
    Movie_name = models.CharField(max_length=20, verbose_name='电影名' , help_text="电影名")
    Movie_time = models.CharField(max_length=20, verbose_name="电影时间",help_text="电影时间")

    class Meta:
        db_table = 'tb_Movie'
        verbose_name = '电影'

