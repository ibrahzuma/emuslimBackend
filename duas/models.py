from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Dua(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='duas')
    short_name_en = models.CharField(max_length=255, verbose_name="Short Name (ENG)")
    short_name_ar = models.CharField(max_length=255, verbose_name="Short Name (AR)")
    full_dua_en = models.TextField(verbose_name="Full Dua (ENG)")
    full_dua_ar = models.TextField(verbose_name="Full Dua (AR)")

    def __str__(self):
        return self.short_name_en
