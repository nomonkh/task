from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.forms import AccountForm, AccountUpdateForm
from account.models import Account
from account.forms import RegisterForm, AccountAuthenticationForm
import calendar
from datetime import datetime


@login_required
def update_account(request):
    context = {}
    user_name = request.user
    print(request.user, '***************************')

    if not user_name.is_authenticated:
        return redirect('account:signin')

    account_info = get_object_or_404(Account, user_name=user_name)

    if str(account_info.user_name) != str(user_name):
        return HttpResponse('Sorry, it is not your account.')
    # return HttpResponse('1111')

    form = AccountForm(request.POST or None, request.FILES or None, instance=account_info)
    print("^^^^^^^^^^^^^^^^^^^^^^^", form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context['message'] = 'Updated Successfully!'
        account_info = obj
        if calendar.day_name[datetime.now().weekday()] == 'Monday':
            return redirect('job_app:task_monday')
        if calendar.day_name[datetime.now().weekday()] == 'Tuesday':
            return redirect('job_app:task_tuesday')
        if calendar.day_name[datetime.now().weekday()] == 'Wednesday':
            return redirect('job_app:task_wednesday')
        if calendar.day_name[datetime.now().weekday()] == 'Thursday':
            return redirect('job_app:task_thursday')
        if calendar.day_name[datetime.now().weekday()] == 'Friday':
            return redirect('job_app:task_friday')
        if calendar.day_name[datetime.now().weekday()] == 'Saturday':
            return redirect('job_app:task_saturday')
    form_data = AccountForm(
        initial={
            # 'email': account_info.email,
            'user_name': account_info.user_name,
        }
    )
    context = {
        "form": form,
        "form_data": form_data
    }

    return render(request, 'personal_info.html', context)

    # form = AccountForm(
    #     initial={
    #         # 'email': account_info.email,
    #         'user_name': account_info.user_name,
    #     }
    # )
    # # account = Account.objects.filter(id=user.id)
    # # context['account'] = account
    # context['form'] = form
    # # context['registration_form'] = form
    #
    # return render(request, 'personal_info.html', context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
            if calendar.day_name[datetime.now().weekday()] == 'Monday':
                return redirect('job_app:task_monday')
            if calendar.day_name[datetime.now().weekday()] == 'Tuesday':
                return redirect('job_app:task_tuesday')
            if calendar.day_name[datetime.now().weekday()] == 'Wednesday':
                return redirect('job_app:task_wednesday')
            if calendar.day_name[datetime.now().weekday()] == 'Thursday':
                return redirect('job_app:task_thursday')
            if calendar.day_name[datetime.now().weekday()] == 'Friday':
                return redirect('job_app:task_friday')
            if calendar.day_name[datetime.now().weekday()] == 'Saturday':
                return redirect('job_app:task_saturday')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'sign_up.html', context)


def authentication(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if calendar.day_name[datetime.now().weekday()] == 'Monday':
            return redirect('job_app:task_monday')
        if calendar.day_name[datetime.now().weekday()] == 'Tuesday':
            return redirect('job_app:task_tuesday')
        if calendar.day_name[datetime.now().weekday()] == 'Wednesday':
            return redirect('job_app:task_wednesday')
        if calendar.day_name[datetime.now().weekday()] == 'Thursday':
            return redirect('job_app:task_thursday')
        if calendar.day_name[datetime.now().weekday()] == 'Friday':
            return redirect('job_app:task_friday')
        if calendar.day_name[datetime.now().weekday()] == 'Saturday':
            return redirect('job_app:task_saturday')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if calendar.day_name[datetime.now().weekday()] == 'Monday':
                    return redirect('job_app:task_monday')
                if calendar.day_name[datetime.now().weekday()] == 'Tuesday':
                    return redirect('job_app:task_tuesday')
                if calendar.day_name[datetime.now().weekday()] == 'Wednesday':
                    return redirect('job_app:task_wednesday')
                if calendar.day_name[datetime.now().weekday()] == 'Thursday':
                    return redirect('job_app:task_thursday')
                if calendar.day_name[datetime.now().weekday()] == 'Friday':
                    return redirect('job_app:task_friday')
                if calendar.day_name[datetime.now().weekday()] == 'Saturday':
                    return redirect('job_app:task_saturday')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'sign_in.html', context)


def signout_view(request):
    logout(request)
    return redirect('account:signin')
