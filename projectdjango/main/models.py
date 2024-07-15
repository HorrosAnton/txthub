from django.db import models


class Articles(models.Model):
    title = models.TextField("Название")
    urls_site = models.TextField("Ссылка")

    def __str__(self):
        return self.urls_site

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"