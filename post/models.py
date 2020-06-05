from django.db import models

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
	title = models.CharField(max_length = 150, verbose_name="Başlık")
	content = models.TextField(verbose_name="İçerik")
	created_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi")
	def __str__(self):
		return self.title