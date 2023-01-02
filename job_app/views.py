from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import TaskModel, ExecutorModel
from .serializers import ExecutorSerializer, TaskSerializer, SingleTaskSerializer
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, ExecutorForm, TaskUpdateForm
import calendar
from datetime import datetime


@login_required
class TaskView(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/change_list_results.html'

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                # executor = request.data.pop('executor')
                # ExecutorModel.objects.create(**executor)
                TaskModel.objects.create(**request.data)
                return Response({'msg': 'true'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'msg': str(e)})

    def get(self, request):
        queryset = TaskModel.objects.all()
        return Response({'tasks': queryset})


@login_required
class SingleApiTask(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = SingleTaskSerializer

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'true'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'false'})


@login_required
def task_view_monday(request):
    return render(request, 'monday.html')


@login_required
def task_view_tuesday(request):
    return render(request, 'tuesday.html')


@login_required
def task_view_wednesday(request):
    return render(request, 'wednesday.html')


@login_required
def task_view_thursday(request):
    return render(request, 'thursday.html')


@login_required
def task_view_friday(request):
    return render(request, 'friday.html')


@login_required
def task_view_saturday(request):
    return render(request, 'saturday.html')


@login_required
def create_task(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")

    form = TaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
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

    data = TaskModel.objects.all()
    form_data = TaskForm()

    context = {
        "form": form,
        "time": data,
    }

    return render(request, 'create_task.html', context)


@login_required
def create_executor(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")

    form = ExecutorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        return redirect('job_app:executors_view')

    data = ExecutorModel.objects.all()
    form_data = ExecutorForm()

    context = {
        "form": form,
        "time": data,
    }

    return render(request, 'create_executor.html', context)


@login_required
def executors_view(request):
    users = ExecutorModel.objects.all()
    context = {
        "users": users
    }
    return render(request, 'executors.html', context)


@login_required
def del_user(request, pk):
    try:
        executor = ExecutorModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    executor.delete()
    return redirect('job_app:executors_view')


@login_required
def update_executor(request, pk):
    executor_info = get_object_or_404(ExecutorModel, id=pk)
    form = ExecutorForm(request.POST or None, request.FILES or None, instance=executor_info)
    print("^^^^^^^^^^^^^^^^^^^^^^^", form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

        account_info = obj
        return redirect('job_app:executors_view')
    form_data = ExecutorForm(
        initial={
            # 'email': account_info.email,
            'first_name': executor_info.first_name,
            'second_name': executor_info.second_name,
            'third_name': executor_info.third_name,
            'phone': executor_info.phone,
            'sector': executor_info.sector,
        }
    )
    context = {
        "form": form,
        "form_data": form_data
    }

    return render(request, 'update_executor.html', context)


@login_required
def update_task(request, pk):
    task_info = get_object_or_404(TaskModel, id=pk)
    form = TaskUpdateForm(request.POST or None, request.FILES or None, instance=task_info)
    print("^^^^^^^^^^^^^^^^^^^^^^^", form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
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
    form_data = TaskUpdateForm(
        initial={
            # 'email': account_info.email,
            'status': task_info.status,
            'confirmation': task_info.confirmation,
        }
    )
    context = {
        "form": form,
        "form_data": form_data
    }

    return render(request, 'update_task.html', context)

