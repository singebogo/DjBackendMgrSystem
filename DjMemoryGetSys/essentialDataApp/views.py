from django_tables2 import RequestConfig
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib import messages
from django.conf import settings

from .forms import QueryToolbarForm, EssentialDataUpdateForm, EssentialDataAddForm
from .models import CodeType
from .tables import EssentialDataTable

# Create your views here.
@xframe_options_sameorigin
@login_required
def index(request):
    global querytoolbar_form
    if request.method == 'GET':
        # 如果时区为空，则默认系统设置时区
        querytoolbar_form = QueryToolbarForm()
    elif request.method == 'POST':
        querytoolbar_form = QueryToolbarForm(request.POST)
    queryset = CodeType.objects.all()
    if querytoolbar_form.is_valid():
        name = querytoolbar_form.cleaned_data["name"]
        code = querytoolbar_form.cleaned_data["code"]
        if name:
            queryset = queryset.filter(name__contains=(name))
        if code:
            queryset = queryset.filter(code__contains=(code))
    table = EssentialDataTable(queryset.values())
    RequestConfig(request, paginate={'per_page': settings.PAGE_NUM}).configure(table)
    return render(request, "queryMain.html",
                  context={"table": table, "Form": querytoolbar_form,
                           "formUrl": "essentialDataApp:index", "formAddUrl": "essentialDataApp:add"})

@xframe_options_sameorigin
@login_required
def vaild(request):
    if request.method == "POST":
        selectCode = request.POST['selectCode']
        selectName = request.POST['selectName']
        if selectName or selectCode:
            dataTypesObj = CodeType.objects.filter(code__in=(selectCode), name__in=(selectName)).values()
        else:
            # 查询全部数据
            dataTypesObj = CodeType.objects.all().values()
        return HttpResponse(request, content={"values": dataTypesObj})
    else:
        return HttpResponse(request, content={"msg": "请求方法不支持"})


@xframe_options_sameorigin
@login_required
def delete(request, pk):
    try:
        CodeType.objects.filter(code=pk).first().delete()  # 根据pk找到对象
        messages.add_message(request, messages.INFO, '字典{}删除成功！'.format(pk))
    except Exception as e:
        pass
    finally:
        return redirect('essentialDataApp:index')

@xframe_options_sameorigin
@login_required
def view(request, pk):
    # 放假渲染的html, 前端接受后直接弹框显示，避免新增。修改时候将页面覆盖
    if request.method == 'GET':
        queryset = CodeType.objects.filter(code=pk).first()  # 根据pk找到对象
        form = EssentialDataUpdateForm(instance=queryset)

        return render(request, "viewUpdate.html",
                      context={"Form": form, "pk": pk, "title": "修改数据",
                               "formUpdateUrl": "essentialDataApp:update", "type": True,
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})

@xframe_options_sameorigin
@login_required
def update(request, pk):
    # 放假渲染的html, 前端接受后直接弹框显示，避免新增。修改时候将页面覆盖
    if request.method == 'GET':
        queryset = CodeType.objects.filter(code=pk).first()  # 根据pk找到对象
        form = EssentialDataUpdateForm(instance=queryset)

        return render(request, "viewUpdate.html",
                      context={"Form": form, "pk": pk, "title": "修改数据",
                               "formUpdateUrl": "essentialDataApp:update",
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})
    elif request.method == 'POST':
        instance = CodeType.objects.get(code=pk)
        form = EssentialDataUpdateForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.instance.updatedUser = request.user.username
                form.instance.createdUser = instance.createdUser
                form.instance.createdDate = instance.createdDate
                form.save()
                # messages.success(request, '字典{}更新成功！'.format(pk))
                messages.add_message(request, messages.INFO, '{}更新成功！'.format(pk))

                return redirect('essentialDataApp:index')
            except Exception as e:
                print("--", e)
                return render(request, "viewUpdate.html",
                              context={"Form": form, "msg": str(e), "title": "修改数据",
                               "formUpdateUrl": "essentialDataApp:update",
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})
        else:
            return render(request, "viewUpdate.html",
                          context={"Form": form, "title": "修改数据",
                               "formUpdateUrl": "essentialDataApp:update",
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})


@xframe_options_sameorigin
@login_required
def add(request):
    # 放假渲染的html, 前端接受后直接弹框显示，避免新增。修改时候将页面覆盖
    if request.method == 'GET':
        form = EssentialDataAddForm()
        return render(request, "viewUpdate.html",
                      context={"Form": form, "title": "新增数据",
                               "formUpdateUrl": "essentialDataApp:update",
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})
    elif request.method == "POST":
        form = EssentialDataAddForm(request.POST)
        if form.is_valid():
            try:
                form.instance.createdUser = request.user.username
                instance = form.save()
                # messages.success(request, '字典{}新增成功！'.format(instance.name))
                messages.add_message(request, messages.INFO, '{}新增成功！'.format(instance.name))

                return redirect('essentialDataApp:index')
            except Exception as e:
                return render(request, "viewUpdate.html",
                              context={"Form": form, "msg": str(e), "title": "新增数据",
                               "formUpdateUrl": "essentialDataApp:update",
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})
        else:
            return render(request, "viewUpdate.html",
                          context={"Form": form, "title": "新增数据",
                               "formUpdateUrl": "essentialDataApp:update",
                               "formAddUrl": "essentialDataApp:add",
                               'FormCancel': "essentialDataApp:index", "col": 3,})


