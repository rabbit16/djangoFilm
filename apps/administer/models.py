from django.db import models
from django.utils import timezone
from users.models import User
from users.models import Movie

class Ticket(models.Model):
    Ticket_id = models.IntegerField(max_length=20,help_text="电影票id",verbose_name="电影票id")
    Seat_id = models.IntegerField(max_length=20, help_text="座位id", verbose_name="座位id")
    Seat_name = models.IntegerField(max_length=20, help_text="座位名称", verbose_name="座位名称")
    Studio_id = models.IntegerField(max_length=20, help_text="演播厅id", verbose_name="演播厅id")
    Studio_name = models.IntegerField(max_length=20, help_text="演播厅名称", verbose_name="演播厅名称")
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

class Movie_type(models.Model):  # 电影标签
    Romance = models.CharField(max_length=20, help_text="爱情片", verbose_name="爱情片")
    Drama = models.CharField(max_length=20, help_text="剧情片", verbose_name="剧情片")
    Comedy = models.CharField(max_length=20, help_text="喜剧片", verbose_name="喜剧片")
    Ethics = models.CharField(max_length=20, help_text="伦理片", verbose_name="伦理片")
    Literature= models.CharField(max_length=20, help_text="文艺片", verbose_name="文艺片")
    Music = models.CharField(max_length=20, help_text="音乐片", verbose_name="音乐片")
    Animation = models.CharField(max_length=20, help_text="动漫片", verbose_name="动漫片")
    Martial_arts = models.CharField(max_length=20, help_text="武侠片", verbose_name="武侠片")
    costume = models.CharField(max_length=20, help_text="古装片", verbose_name="古装片")
    horror = models.CharField(max_length=20, help_text="恐怖片", verbose_name="恐怖片")
    thriller = models.CharField(max_length=20, help_text="惊悚片", verbose_name="惊悚片")
    Crime = models.CharField(max_length=20, help_text="犯罪片", verbose_name="犯罪片")
    Suspense = models.CharField(max_length=20, help_text="悬疑片", verbose_name="悬疑片")
    Documentary = models.CharField(max_length=20, help_text="纪录片", verbose_name="纪录片")
    War = models.CharField(max_length=20, help_text="战争片", verbose_name="战争片")
    Science= models.CharField(max_length=20, help_text="科幻片", verbose_name="科幻片")



    class Meta:
        db_table = "tb_movie_type"
        verbose_name = "电影标签"
