from collections import OrderedDict

from django import forms
from .models import DataDict


class QueryToolbarForm(forms.Form):
    type = forms.CharField(
        label='字典类型',
        required=False,
        # min_length=3,
        initial='',
        widget=forms.TextInput(attrs={"class": "form-control input-sm", "placeholder": "请双击选择字典类型"}),
        # error_messages={
        #     "required": "字典类型不能为空",
        #     "min_length": "字典类型最小长度为3位",
        # },
    )
    name = forms.CharField(
        label="字典名称",
        required=False,
        # min_length=6,
        initial='',
        # error_messages={
        #     "min_length": "字典名称最小长度为6位",
        #     "required": "字典名称不能为空",
        # },
        widget=forms.TextInput(attrs={"class": "form-control input-sm", "placeholder": "请输入字典名称"}),
    )

    code = forms.CharField(
        label="字典代码",
        required=False,
        # min_length=6,
        initial='',
        # error_messages={
        #     "min_length": "字典代码最小长度为6位",
        #     "required": "字典代码不能为空",
        # },
        widget=forms.TextInput(attrs={"class": "form-control input-sm", "placeholder": "请输入字典代码"}),
    )

    class Meta:
        model = DataDict
        fields = ['type', 'name', 'code']


class DataDictUpdateForm(forms.ModelForm):
    code = forms.CharField(
        label='*字典代码',
        required=True,
        min_length=3,
        initial='',
        widget=forms.TextInput(attrs={
            "class": "form-control input-sm",
            "placeholder": "请填写代码(数字字母下划线)",
            "onkeyup": "this.value=this.value.replace(/[^\w_]/g,'');"}),
        error_messages={
            "required": "代码不能为空",
            "min_length": "代码最小长度为3位",
        },
    )

    enableTime = forms.DateTimeField(
        label='*生效时间',
        required=True,
        widget=forms.DateTimeInput(attrs={"class": "form-control input-sm selectpicker", "placeholder": "请填写生效时间"}),
        error_messages={
            "required": "生效时间不能为空",
        },
    )

    disableTime = forms.DateTimeField(
        label='*失效时间',
        required=True,
        widget=forms.DateTimeInput(attrs={"class": "form-control input-sm selectpicker", "placeholder": "请填写失效时间"}),
        error_messages={
            "required": "失效时间不能为空",
        },
    )

    class Meta:
        # 自定义使用哪个模型和哪些字段来创建和更新用户
        model = DataDict
        fields = ['type', 'code', 'name', 'value', 'enableTime', 'disableTime', 'invildId', 'remark', ]
