from django_tables2 import RequestConfig
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib import messages
from django.conf import settings

from .forms import QueryToolbarForm, DataDictUpdateForm
from .models import DataDict
from .tables import DataDictTable


@xframe_options_sameorigin
@login_required
def index(request):
    global querytoolbar_form
    if request.method == 'GET':
        # 如果时区为空，则默认系统设置时区
        querytoolbar_form = QueryToolbarForm()
    elif request.method == 'POST':
        querytoolbar_form = QueryToolbarForm(request.POST)
    queryset = DataDict.objects.all()
    if querytoolbar_form.is_valid():
        type = querytoolbar_form.cleaned_data["type"]
        name = querytoolbar_form.cleaned_data["name"]
        code = querytoolbar_form.cleaned_data["code"]
        if type:
            queryset = queryset.filter(type__contains=type)
        if name:
            queryset = queryset.filter(name__contains=(name))
        if code:
            queryset = queryset.filter(code__contains=(code))
    table = DataDictTable(queryset.values())
    RequestConfig(request, paginate={'per_page': settings.PAGE_NUM}).configure(table)
    return render(request, "queryMain.html",
                  context={"table": table, "Form": querytoolbar_form,
                           "formUrl": "dataDictionaryApp:index", "formAddUrl": "dataDictionaryApp:add"})

@xframe_options_sameorigin
@login_required
def vaild(request):
    if request.method == "POST":
        selectCode = request.POST['selectCode']
        selectName = request.POST['selectName']
        if selectName or selectCode:
            dataTypesObj = DataDict.objects.filter(code__in=(selectCode), name__in=(selectName)).values()
        else:
            # 查询全部数据
            dataTypesObj = DataDict.objects.all().values()
        return HttpResponse(request, content={"values": dataTypesObj})
    else:
        return HttpResponse(request, content={"msg": "请求方法不支持"})


@xframe_options_sameorigin
@login_required
def delete(request, pk):
    try:
        DataDict.objects.filter(pk=pk).first().delete()  # 根据pk找到对象
        messages.add_message(request, messages.INFO, '字典{}删除成功！'.format(pk))
    except Exception as e:
        pass
    finally:
        return redirect('dataDictionaryApp:index')

@xframe_options_sameorigin
@login_required
def view(request, pk):
    # 放假渲染的html, 前端接受后直接弹框显示，避免新增。修改时候将页面覆盖
    if request.method == 'GET':
        queryset = DataDict.objects.filter(id=pk).first()  # 根据pk找到对象
        dataDictUpdate_form = DataDictUpdateForm(instance=queryset)

        return render(request, "viewUpdate.html",
                      context={"Form": dataDictUpdate_form, "pk": pk, "title": "修改数据字典",
                               "formUpdateUrl": "dataDictionaryApp:update", "type": True,
                               "formAddUrl": "dataDictionaryApp:add",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})

@xframe_options_sameorigin
@login_required
def update(request, pk):
    # 放假渲染的html, 前端接受后直接弹框显示，避免新增。修改时候将页面覆盖
    if request.method == 'GET':
        queryset = DataDict.objects.filter(id=pk).first()  # 根据pk找到对象
        dataDictUpdate_form = DataDictUpdateForm(instance=queryset)

        return render(request, "viewUpdate.html",
                      context={"Form": dataDictUpdate_form, "pk": pk, "title": "修改数据字典",
                               "formUpdateUrl": "dataDictionaryApp:update",
                               "formAddUrl": "dataDictionaryApp:add",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})
    elif request.method == 'POST':
        instance = DataDict.objects.get(id=pk)
        dataDictUpdate_form = DataDictUpdateForm(request.POST, instance=instance)
        if dataDictUpdate_form.is_valid():
            try:
                dataDictUpdate_form.instance.updatedUser = request.user.username
                dataDictUpdate_form.instance.createdUser = instance.createdUser
                dataDictUpdate_form.instance.createdDate = instance.createdDate
                dataDictUpdate_form.save()
                # messages.success(request, '字典{}更新成功！'.format(pk))
                messages.add_message(request, messages.INFO, '字典{}更新成功！'.format(pk))

                return redirect('dataDictionaryApp:index')
            except Exception as e:
                print("CodetypeUpdate--", e)
                return render(request, "viewUpdate.html",
                              context={"Form": dataDictUpdate_form, "msg": str(e), "title": "修改数据字典",
                               "formUpdateUrl": "dataDictionaryApp:CodetypeUpdate",
                               "formAddUrl": "dataDictionaryApp:addCodetype",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})
        else:
            return render(request, "viewUpdate.html",
                          context={"Form": dataDictUpdate_form, "title": "修改数据字典",
                               "formUpdateUrl": "dataDictionaryApp:update",
                               "formAddUrl": "dataDictionaryApp:add",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})


@xframe_options_sameorigin
@login_required
def add(request):
    # 放假渲染的html, 前端接受后直接弹框显示，避免新增。修改时候将页面覆盖
    if request.method == 'GET':
        dataDictUpdate_form = DataDictUpdateForm()
        return render(request, "viewUpdate.html",
                      context={"Form": dataDictUpdate_form, "title": "新增数据字典",
                               "formUpdateUrl": "dataDictionaryApp:update",
                               "formAddUrl": "dataDictionaryApp:add",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})
    elif request.method == "POST":
        dataDictUpdate_form = DataDictUpdateForm(request.POST)
        if dataDictUpdate_form.is_valid():
            try:
                dataDictUpdate_form.instance.createdUser = request.user.username
                instance = dataDictUpdate_form.save()
                # messages.success(request, '字典{}新增成功！'.format(instance.name))
                messages.add_message(request, messages.INFO, '字典{}新增成功！'.format(instance.name))

                return redirect('dataDictionaryApp:index')
            except Exception as e:
                print("addCodetype", e)
                return render(request, "viewUpdate.html",
                              context={"Form": dataDictUpdate_form, "msg": str(e), "title": "新增数据字典",
                               "formUpdateUrl": "dataDictionaryApp:update",
                               "formAddUrl": "dataDictionaryApp:add",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})
        else:
            return render(request, "viewUpdate.html",
                          context={"Form": dataDictUpdate_form, "title": "新增数据字典",
                               "formUpdateUrl": "dataDictionaryApp:update",
                               "formAddUrl": "dataDictionaryApp:add",
                               'FormCancel': "dataDictionaryApp:index", "col": 3,})