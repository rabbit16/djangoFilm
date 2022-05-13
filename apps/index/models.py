from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager as _UserManager, AbstractUser

# Create your models here.

class UserManager(_UserManager):
    def create_superuser(self, username, password, email=None, **extra_fields):
        super().create_superuser(username=username, email=email, password=password, **extra_fields)

class User(AbstractUser):
    objects = UserManager()
    REQUIRED_FIELDS = ['mobile']
    name = models.CharField(max_length=20,
                            help_text="用户真实姓名",
                            verbose_name="用户真实姓名",
                            error_messages={"message": "名字格式出错"}
                            )
    ticketManager = models.BooleanField(verbose_name="票务管理员", help_text="票务管理员", default=False)
    buyManager = models.BooleanField(verbose_name="售票员", help_text="售票员", default=False)
    mobile = models.CharField(max_length=11, verbose_name='手机号', help_text="手机号", unique=True,
                              error_messages={'unique': "该手机号已注册"})
    email_ac = models.BooleanField(default=False, verbose_name="邮箱状态")
    registration_data = models.DateTimeField(verbose_name="注册时间",
                                             help_text="注册时间",
                                             default=timezone.now
                                             )
    sex = models.BooleanField(verbose_name="性别", help_text="性别", default=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'

    def __str__(self):
        return self.name




