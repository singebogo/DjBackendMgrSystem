import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from .models import CodeType


class EssentialDataTable(tables.Table):
    id_select = tables.CheckBoxColumn(accessor="code", orderable=False, exclude_from_export=True)
    count = tables.Column(empty_values=(), verbose_name='#')
    actions = tables.Column(empty_values=(), verbose_name="操作", orderable=False, exclude_from_export=True)

    def render_count(self, value, record):
        perRow = (self.page.number-1) * self.paginator.per_page
        row_counter = getattr(self, 'row_counter', 0)
        if row_counter % self.paginator.per_page == 0:
            row_counter += perRow + 1
        else:
            row_counter += 1

        setattr(self, 'row_counter', row_counter)
        return format_html(
            '<a href= "' + reverse("essentialDataApp:view", args=[str(record['code'])]) + '">' + str(row_counter) + '</a>')
    
    class Meta:
        # 使用哪个模型
        model = CodeType
        # 表格中显示哪些字段
        fields = ['count', 'code', 'name', 'invildId','createdUser','updatedUser','createdDate','updatedDate']
        # 表格中字段显示顺序
        sequence = ['id_select'] + fields + ['actions']
        # 表格模板
        template_name = "django_tables2/bootstrap4.html"
        # 表格样式
        attrs = {"class": "table table-striped table-sm text-nowrap"}
        # 排序字段
        order_by_field = 'sort_by'  # default: sort

        page_field = 'page'

        filter = True


    # 自定义操作链接
    def render_actions(self, value, record):
        url = reverse("essentialDataApp:delete", args=[str(record['code'])])
        return format_html(
            '<a class="btn btn-sm badge badge-pill badge-warning ml-2" href= "' +
            reverse("essentialDataApp:update", args=[str(record['code'])]) + '">' + '编辑' + '</a>'
            + '<a href="javascript:void(0);" onclick="$(\'#myConfirm\').attr(\'url\', \''+url+'\'); $(\'#myConfirm\').modal(\'show\');return false"'
                                                                                              ' class="btn btn-sm badge badge-pill badge-danger ml-2">'
            + '删除' + '</a>'
        )
