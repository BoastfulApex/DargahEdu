from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    lang = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    new_phone = models.CharField(max_length=500, null=True, blank=True)
    otp = models.CharField(max_length=500, null=True, blank=True)


class Cource(models.Model):
    name_lat = models.CharField(max_length=500, null=True, blank=True)
    name_kril = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField(default=0)
    price_3_month = models.IntegerField(default=0)
    price_6_month = models.IntegerField(default=0)
    price_9_month = models.IntegerField(default=0)
    price_12_month = models.IntegerField(default=0)
    description_lat = models.TextField(max_length=10000, null=True, blank=True)
    description_kril = models.TextField(max_length=10000, null=True, blank=True)
    test_channel = models.CharField(max_length=500, null=True, blank=True)
    channel = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_lat
    
    @property
    def ImageURL(self):
        try:
            return self.image.url
        except:
            return ''


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    to_date = models.DateField(null=True)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    

class Slider(models.Model):
    name_lat = models.CharField(max_length=500, null=True, blank=True)
    name_kril = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True)
    video = models.FileField(null=True)
    description_lat = models.TextField(max_length=10000, null=True, blank=True)
    description_kril = models.TextField(max_length=10000, null=True, blank=True)


class FAQ(models.Model):
    question_lat = models.TextField(max_length=10000, null=True, blank=True)
    question_kril = models.TextField(max_length=10000, null=True, blank=True)
    answer_lat = models.TextField(max_length=10000, null=True, blank=True)
    answer_kril = models.TextField(max_length=10000, null=True, blank=True)


class Comment(models.Model):
    customer_lat = models.TextField(max_length=10000, null=True, blank=True)
    customer_kril = models.TextField(max_length=10000, null=True, blank=True)
    comment_lat = models.TextField(max_length=10000, null=True, blank=True)
    comment_kril = models.TextField(max_length=10000, null=True, blank=True)


class Teacher(models.Model):
    name_lat = models.CharField(max_length=500, null=True, blank=True)
    name_kril = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True)
    description_lat = models.TextField(max_length=10000, null=True, blank=True)
    description_kril = models.TextField(max_length=10000, null=True, blank=True)

