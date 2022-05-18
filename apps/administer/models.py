from django.db import models
from django.utils import timezone

class Ticket:
    Ticket_id = models.CharField(max_length=20,help_text="电影票id",verbose_name="电影票id")
    Movie_id = models.CharField(max_length=20, help_text="电影id", verbose_name="电影id")
    Seat_id = models.CharField(max_length=20, help_text="座位id", verbose_name="座位id")
    Studio_id = models.CharField(max_length=20, help_text="演播厅id", verbose_name="演播厅id")
    Movie_name = models.CharField(max_length=20, verbose_name='电影名' , help_text="电影名")
    Movie_time = models.CharField(max_length=20, verbose_name="电影时间",help_text="电影时间")
    s_user = models.ForeignKey('User', on_delete=models.CASCADE)
    class Meta:
        db_table = 'tb_Ticket'
        verbose_name = '电影票'
class Session:
    S_user = models.ManyToManyField('Users')
    S_studio=models.ManyToManyField('Studio')
    S_seat = models.ManyToManyField('Seat')
    S_movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
class Seat:
    Seat_id = models.CharField(max_length=20, help_text="座位id", verbose_name="座位id")
    mark = models.BooleanField(verbose_name="占用情况", help_text="占用情况", default=False)
    #fk连接studio
    #Fk连接用户
    s_stu = models.ForeignKey('Studio', on_delete=models.CASCADE)
    s_user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    class Meta:
        db_table = 'tb_Seat'
        verbose_name = '座位'

class Studio:
    Studio_id = models.CharField(max_length=20,help_text="演播厅id",verbose_name="演播厅id")
    Studio_name= models.CharField(max_length=20, help_text="演播厅名称", verbose_name="演播厅名称")
    Studio_type = models.CharField(max_length=20, help_text="演播厅类型", verbose_name="演播厅类型")
    Seating = models.CharField(max_length=20, help_text="座位个数", verbose_name="座位个数")

    class Meta:
        db_table = 'tb_Studio'
        verbose_name = '演播厅'
