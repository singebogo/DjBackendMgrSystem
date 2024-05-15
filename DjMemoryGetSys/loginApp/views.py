from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import auth
from .forms import RegisterForm, LoginForm, User


def register(request):
    if request.method == "GET":
        register_form = RegisterForm()
        return render(request, "register.html", context={"register_form": register_form})
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]
            email = register_form.cleaned_data.get("email", "")
            # 创建用户
            user = User.objects.create_user(username, email, password)
            auth.login(request, user)
            obj = redirect(reverse('homeApp:home'), {"username": user.username})
            obj.set_signed_cookie('user', user.username)
            return obj
        else:
            return render(request, "register.html", {"register_form": register_form})


def login(request):
    if request.method == "GET":
        username = request.GET.get("username")
        login_form = LoginForm()
        return render(request, "login.html", context={"login_form": login_form})
    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 注意：验证用户名和密码是否正确放到forms中去验证了
            # login(request, request.user)  # 此处不能使用request.user,因为他还没有验证，是匿名用户
            # 所以需要在form中校验通过后传递过来user
            user = auth.authenticate(username=login_form.cleaned_data["user"], password=login_form.cleaned_data["password"])
            if user:
                # 使用auth.login方法加上sessioncookie
                auth.login(request, user)
                # 这段代码看不懂先往下面看
                # 如果校验通过则进去下一个页面,获取不到则默认跳转index的url
                if request.get_full_path() in ('/login/login', '/login/?next=/') or 'next=/home/index/' in request.get_full_path():
                    obj = redirect(reverse('homeApp:index'), (user))
                else:
                    obj = redirect(reverse('homeApp:home'), (user))
                # obj = render(request, "index.html", {"user": user})
                obj.set_signed_cookie('user', user)
                return obj
            else:
                return render(request, "login.html", {"login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})


def logout(request):
    auth.logout(request)
    obj = redirect(reverse('loginApp:login'))
    obj.delete_cookie('user')
    return obj
