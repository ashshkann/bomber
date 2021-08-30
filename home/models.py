from django.db import models

# Create your models here.
class header_site(models.Model):
    title_logo = models.CharField(max_length=20, verbose_name = "logo")
    title_text = models.TextField(verbose_name = "title text")
    title_about = models.TextField(verbose_name = "about text")
    title_background_image = models.ImageField(verbose_name = "background image")
    title_image = models.ImageField(verbose_name = "logo image")

    class Meta:
        verbose_name = 'header'
        verbose_name_plural = 'headers'
    def __str__(self):
        return self.title_logo

class about_site(models.Model):
    about_text = models.TextField()
    about_title_text1 = models.CharField(max_length=50, verbose_name = "title1")
    about_shourt_text1 = models.TextField(verbose_name = "text1")
    about_title_text2 = models.CharField(max_length=50, verbose_name = "title2")
    about_shourt_text2 = models.TextField(verbose_name = "text2")
    about_title_text3 = models.CharField(max_length=50, verbose_name = "title3")
    about_shourt_text3 = models.TextField(verbose_name = "text3")
    about_title_text4 = models.CharField(max_length=50, verbose_name = "title4")
    about_shourt_text4 = models.TextField(verbose_name = "text4")
    about_title_text5 = models.CharField(max_length=50, verbose_name = "title5")
    about_shourt_text5 = models.TextField(verbose_name = "text5")
    bout_title_text6 = models.CharField(max_length=50, verbose_name = "title6")
    about_shourt_text6 = models.TextField(verbose_name = "text6")

    class Meta:
        verbose_name = 'body'
        verbose_name_plural = 'bodys'
    def __str__(self):
        return self.about_title_text1

class copy_right(models.Model):
    copy_right_text = models.CharField(max_length=30, verbose_name="copy right")

    def __str__(self):
        return self.copy_right_text
