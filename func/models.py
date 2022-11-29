from django.db import models

# Create your models here.
class Police_account(models.Model):
    name = models.CharField(max_length = 200,verbose_name = '交警用户账号名')
    password = models.CharField(max_length = 20,verbose_name = '交警用户密码')
    email = models.EmailField(verbose_name = '邮件',max_length = 200)
    age = models.IntegerField()
    sex_choice = (
		(0, '女'),
		(1, '男'),
	)
    sex = models.IntegerField(choices=sex_choice,default=1)
    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = '警员信息'
        verbose_name_plural = verbose_name



class Vedio(models.Model):
    vedio_name = models.CharField(verbose_name = '视频名称')
    vedio_path = models.FileField(upload_to = 'vedio/')
    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = '教育视频'
        verbose_name_plural = verbose_name


class Ticket(models.Model):
    location = models.CharField(max_length = 200,verbose_name = '位置')
    tickets_choice = (
		(0, '违停'),
		(1, '超速'),
        (2, '闯红灯')
	)
    tickets_class = models.IntegerField(choices=tickets_choice,default=0)
    car_photo = models.FileField(upload_to = 'ticket_photo/',verbose_name = '违章照片')
    punish = models.IntegerField(verbose_name = '惩罚分数')
    


class Brand(models.Model):
    btitle = models.CharField(max_length=30, verbose_name='品牌名称')
    logo_brand = models.ImageField(verbose_name='车标',upload_to='brand/',default='normal.png')
    is_delete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = '车辆品牌信息'
        verbose_name_plural = verbose_name


class CarInfo(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='品牌')
    ctitle = models.CharField(max_length=50,null=True, verbose_name='汽车名称')
    engineNo = models.CharField(max_length=100, verbose_name='发动机号',null=True)
    regist_date = models.DateField(verbose_name='上牌日期',null=True)
    picture = models.ImageField(verbose_name='图片',upload_to='img/cars',default='normal.png')
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)
    tickets = models.ForeignKey(Ticket,verbose_name = '罚单',on_delete=models.CASCADE,)
    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = '车辆表'
        verbose_name_plural = verbose_name


class User_account(models.Model):
    name = models.CharField(max_length = 200,verbose_name = '用户账号名')
    password = models.CharField(max_length = 20,verbose_name = '用户密码')
    email = models.EmailField(verbose_name = '邮件',max_length = 200)
    age = models.IntegerField()
    sex_choice = (
		(0, '女'),
		(1, '男'),
	)
    sex = models.IntegerField(choices=sex_choice,default=1)
    car_info = models.ForeignKey(CarInfo,verbose_name='车辆信息',on_delete=models.CASCADE,)

    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name





