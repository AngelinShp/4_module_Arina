from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField(verbose_name='Заголовок',  max_length=128) # charhield - текстовое поле
    description = models.TextField('Описание') #
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2) #digits - всего цифер; places - цифер после запятой
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_ add - время добавления автоматически
    updated_at = models.DateTimeField(auto_now=True) # auto_now - время изменения автоматически
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(verbose_name='Изображение', upload_to=)



    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date()==timezone.now().date():
            created_at_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; fond-weight: bold">Сегодня в {}</span>', created_at_time)

        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')