from django.db import models


class BaseModels(models.Model):
    createdDate = models.DateTimeField("创建时间", auto_now_add=True, null=True, blank=True, editable=False)
    updatedDate = models.DateTimeField("更新时间", auto_now=True, null=True, blank=True, editable=False)
    createdUser = models.CharField("创建者", max_length=100, null=True, blank=True, editable=False)
    updatedUser = models.CharField("更新者", max_length=100, null=True, blank=True, editable=False)
    remark = models.CharField("备注", max_length=100, null=True, blank=True, editable=True)

    class Meta:
        abstract = True


# Create your models here.
class DataDict(BaseModels):
    type = models.CharField("字典类型", max_length=100, null=False, blank=False, editable=True)
    name = models.CharField("字典名称", default="", max_length=100, null=False, blank=False, editable=True)
    code = models.CharField("字典代码", default="", max_length=100, null=False, blank=False, editable=True)
    value = models.CharField("字典值", default="", max_length=100, null=False, blank=False, editable=True)
    enableTime = models.DateTimeField("生效时间", null=True, blank=False, editable=True)
    disableTime = models.DateTimeField("失效时间", null=True, blank=False, editable=True)
    invildId = models.BooleanField("状态", default=True, null=False, blank=False, editable=True)

    class Meta:
        db_table = "datadict"
        ordering = ["type", "name", "code", "value", "invildId", "enableTime", "disableTime", "remark",]
