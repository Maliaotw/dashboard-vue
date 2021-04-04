from django.db import models
import uuid


# Create your models here.

class Asset(models.Model):
    """資產信息表"""

    id = models.UUIDField(verbose_name='資產編號', default=uuid.uuid4, primary_key=True)
    category = models.ForeignKey("Category", verbose_name='類型', on_delete=models.CASCADE)
    busline = models.ForeignKey('Busline', verbose_name='業務線', on_delete=models.CASCADE)
    remarks = models.TextField(verbose_name="備註", blank=True)

    class Meta:
        verbose_name_plural = "資產信息表"

    def __str__(self):
        return "%s" % (self.id)


class Category(models.Model):
    """分類"""

    name = models.CharField(max_length=255, verbose_name='名稱')

    class Meta:
        verbose_name_plural = "類型"

    def __str__(self):
        return "%s" % (self.name)


class Busline(models.Model):
    """業務線"""

    name = models.CharField(max_length=255, verbose_name='名稱')

    class Meta:
        verbose_name_plural = "業務線"

    def __str__(self):
        return "%s" % (self.name)



