from django.db import models
from django.utils import timezone
from users.models import User
from users.models import Movie

class Ticket(models.Model):
    Ticket_id = models.IntegerField(max_length=20,help_text="电影票id",verbose_name="电影票id")
    Seat_id = models.IntegerField(max_length=20, help_text="座位id", verbose_name="座位id")
    Studio_id = models.IntegerField(max_length=20, help_text="演播厅id", verbose_name="演播厅id")
    Movie_name = models.CharField(max_length=20, verbose_name='电影名' , help_text="电影名")
    Movie_time = models.DateTimeField(verbose_name="电影时间",help_text="电影时间")
    s_user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="电影票的价格", help_text="电影票的价格")
    class Meta:
        db_table = 'tb_Ticket'
        verbose_name = '电影票'

    def __str__(self):
        return self.Ticket_id
class Times(models.Model):  # 电影场次
    S_user = models.ForeignKey(User, on_delete=models.CASCADE)
    S_studio = models.ForeignKey('Studio', on_delete=models.CASCADE)
    S_seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    S_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    session = models.IntegerField(verbose_name="场次", help_text="场次")

    class Meta:
        db_table = "tb_session"
        verbose_name = "电影场次"

class Seat(models.Model):
    Seat_id = models.IntegerField(max_length=20, help_text="座位id", verbose_name="座位id")
    Seat_name = models.CharField(max_length=20, verbose_name="座位编号", help_text="座位编号")
    s_stu = models.ManyToManyField('Studio')
    class Meta:
        db_table = 'tb_Seat'
        verbose_name = '座位'
    def __str__(self):
        return self.Seat_id

class Studio(models.Model):
    Studio_id = models.CharField(max_length=20,help_text="演播厅id",verbose_name="演播厅id")
    Studio_name = models.CharField(max_length=20, help_text="演播厅名称", verbose_name="演播厅名称")
    Studio_type = models.CharField(max_length=20, help_text="演播厅类型", verbose_name="演播厅类型")
    Seating = models.CharField(max_length=20, help_text="座位个数", verbose_name="座位个数")
    class Meta:
        db_table = 'tb_Studio'
        verbose_name = '演播厅'
