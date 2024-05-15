from django.db import models

from essentialDataApp.models import BaseModels, CodeType

# Create your models here.
class DataDict(BaseModels):
    type = models.ForeignKey(CodeType, on_delete=models.CASCADE)
    name = models.CharField("字典名称", default="", max_length=100, null=False, blank=False, editable=True)
    code = models.CharField("字典代码", default="", max_length=100, null=False, blank=False, editable=True)
    value = models.CharField("字典值", default="", max_length=100, null=False, blank=False, editable=True)
    invildId = models.BooleanField("状态", default=True, null=False, blank=False, editable=True)

    class Meta:
        db_table = "datadict"
        verbose_name = '基础配置字典'
        ordering = ["type", "name", "code", "value", "invildId", "enableTime", "disableTime", "remark",]
        unique_together = ['type','code']

    def __str__(self):
        return "%s - %s ( %s )" % (self.type, self.name, self.code)