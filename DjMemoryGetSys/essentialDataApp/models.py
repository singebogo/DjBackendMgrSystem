from django.db import models

class BaseModels(models.Model):
    createdDate = models.DateTimeField("创建时间", auto_now_add=True, null=True, blank=True, editable=False)
    updatedDate = models.DateTimeField("更新时间", auto_now=True, null=True, blank=True, editable=False)
    createdUser = models.CharField("创建者", max_length=100, null=True, blank=True, editable=False)
    updatedUser = models.CharField("更新者", max_length=100, null=True, blank=True, editable=False)
    enableTime = models.DateTimeField("生效时间", null=True, blank=False, editable=True)
    disableTime = models.DateTimeField("失效时间", null=True, blank=False, editable=True)
    remark = models.CharField("备注", max_length=100, null=True, blank=True, editable=True)

    class Meta:
        abstract = True


# Create your models here.
class CodeType(BaseModels):
    code = models.CharField("代码", max_length=30, null=False, primary_key=True)
    name = models.CharField("名称", max_length=100, null=False, blank=False)
    invildId = models.BooleanField("状态", default=True, null=False, blank=False, editable=True)

    class Meta:
        verbose_name = '基础配置类型'
        db_table = 'codetype'

    def __str__(self):
        return "%s ( %s )" % (self.name, self.code)
