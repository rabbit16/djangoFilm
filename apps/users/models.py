from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager as _UserManager, AbstractUser

# Create your models here.
from administer.models import Movie_type, Studio, Seat


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
    birthday = models.DateTimeField(verbose_name="生日", help_text="生日", default=timezone.now)
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'

    def __str__(self):
        return self.name

class Ticket(models.Model):
    Ticket_id = models.IntegerField(max_length=20,help_text="电影票id",verbose_name="电影票id")
    Seat_id = models.IntegerField(max_length=20, help_text="座位id", verbose_name="座位id")
    Seat_name = models.IntegerField(max_length=20, help_text="座位名称", verbose_name="座位名称")
    Studio_id = models.IntegerField(max_length=20, help_text="演播厅id", verbose_name="演播厅id")
    Studio_name = models.IntegerField(max_length=20, help_text="演播厅名称", verbose_name="演播厅名称")
    Movie_name = models.CharField(max_length=20, verbose_name='电影名' , help_text="电影名")
    Movie_time = models.DateTimeField(verbose_name="电影时间", help_text="电影时间")
    s_user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="电影票的价格", help_text="电影票的价格")
    class Meta:
        db_table = 'tb_Ticket'
        verbose_name = '电影票'

    def __str__(self):
        return self.Ticket_id

class Movie(models.Model):
    Movie_id = models.CharField(max_length=20, help_text="电影id", verbose_name="电影id")
    Movie_name = models.CharField(max_length=20, verbose_name='电影名', help_text="电影名")
    Movie_time = models.CharField(max_length=20, verbose_name="电影上映时间", help_text="电影上映时间")
    Movie_img = models.CharField(max_length=100, verbose_name="电影上映时间", help_text="电影上映时间")
    m_movietype = models.ManyToManyField(Movie_type)

    class Meta:
        db_table = 'tb_Movie'
        verbose_name = '电影'


class Times(models.Model):  # 电影场次
    S_user = models.ForeignKey(User, on_delete=models.CASCADE)
    S_studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    S_seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    S_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    session = models.IntegerField(verbose_name="场次", help_text="场次")

    class Meta:
        db_table = "tb_session"
        verbose_name = "电影场次"

