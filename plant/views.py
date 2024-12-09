from django.shortcuts import render
from plant.models import *
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from plant.forms import *
# Create your views here.
def view_plant(request):
    header = "Главная страница"
    context = {'header': header}
    return render(request, 'plant.html',context)

def view_plant_employee(request):
    header = "Работники"
    # employee = Employee.objects.all().order_by('id')
    employee = Employee.objects.select_related('brigade').all().order_by('id')
    # # создаем пагинатор
    posts_per_page = request.GET.get('posts_per_page', 3)
    paginator = Paginator(employee,posts_per_page)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page',1)

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    context = {'header': header, 'page_post': page_posts}
    return render(request, 'employee.html', context)

def spis(request):
    error = None
    good = None
    brigades =[]
    br = Brigade.objects.all().values_list('name', flat=True)
    for b in br:
        brigades.append(b)
    info = {'good': good, 'error': error, 'brigades': brigades}

    return render(request, 'registration_page.html', info)
def sign_up_by_plant(request):
    error = None
    brigades =[]
    positions=[]
    br = Brigade.objects.all().values_list('name', flat=True)
    for b in br:
        brigades.append(b)
    pos = Position.objects.all().values_list('name', flat=True)
    for p in pos:
        positions.append(p)
    info = {'good': None, 'error': None, 'brigades': brigades, 'positions': positions}
    if request.method == "POST":
        form = EmployeeRegistr(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            users = Employee.objects.all().values_list('name', flat=True)
            if username in users:
                error = 'Такой сотрудник уже существует.'
            else:
                position = form.cleaned_data['position']
                boss = form.cleaned_data['boss']
                brigade = form.cleaned_data['brigade']
                br = Brigade.objects.get(name=brigade).id
                print('выбор',str(br),error,username,users)
                Employee.objects.create(name=username, position=position, boss=boss, activ = True, brigade_id=br)
                good = f'Приветствуем, {username}!'
                info['good'] = good
                info['error'] = error
        else:
            error = 'Форма не валидна.'
        info['error'] = error
    else:
        form = EmployeeRegistr()
    info['form'] = form
    return render(request, 'registration_page.html',info)

def delete_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Employee, pk=pk)
        post.delete()
        return redirect('employee.html')

# def button_function(request):
#     if request.method == 'POST':
#         # Здесь вы можете выполнить необходимые действия
#         return HttpResponse('Кнопка нажата!')
#     return render(request, 'template.html')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST' and 'delete' in request.POST:
        employee.delete()
        return redirect('employee_main')
    return render(request, 'delete_employee.html', {'employee': employee})

def edit_employee1(request, pk):
    # def edit_employee(request, pk):

    error=None
    name='test'
    brigades =[]
    positions=[]
    br = Brigade.objects.all().values_list('name', flat=True)
    for b in br:
        brigades.append(b)
    pos = Position.objects.all().values_list('name', flat=True)
    for p in pos:
        positions.append(p)
    info = {'error': error, 'brigades': brigades, 'positions': positions }
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        # form = EmployeeForm(request.POST, instance=employee)
        form = EmployeeForm(request.POST)
        #         # print(employee.brigade)
        # employee.save()
        # employee.brigade = form.brigade
        if form.is_valid():
            # info['name']=employee.name
            # name=employee.name
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            boss = form.cleaned_data['boss']
            brigade = form.cleaned_data['brigade']

            br = Brigade.objects.get(name=brigade).id
            employee.objects.update(name=name, position=position, boss=boss, activ=True, brigade_id=br)
            # employee = Employee.objects.get(pk=pk)
            print(employee.name)
            # employee.name = 'Jane Doe'
            # employee.position = 'Marketing Manager'

            # employee.name = name
            # employee.position = position
            # employee.boss = boss
            # # employee.activ = True
            # employee.brigade_id = br
            # employee.save()
            # print(employee.brigade)
            # form.save()
        else:
            print('Форма не валидна.')
            error= 'Форма не валидна.'
                        # return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    info['form'] = form
    info['name']=employee.name
    info['position']=employee.position
    info['boss'] = employee.boss
    info['selected_brigade']=employee.brigade
    # print(employee.brigade)

    return render(request, 'edit_employee.html', info)
def edit_employee(request, pk):
    error = None
    employee = get_object_or_404(Employee, pk=pk)
    brigades = Brigade.objects.all().values_list('name', flat=True)
    positions = Position.objects.all().values_list('name', flat=True)
    info = {'error': error, 'brigades': brigades, 'positions': positions}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print('форма валидна')
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            boss = form.cleaned_data['boss']
            brigade_name = form.cleaned_data['brigade']
            brigade = Brigade.objects.get(name=brigade_name).id
            # brigade = get_object_or_404(Brigade, name=brigade_name)

            employee.name = name
            employee.position = position
            employee.boss = boss
            employee.brigade_id = brigade
            # employee.activ = True
            employee.save()
        else:
            # info['error'] = form.errors
            print('Форма не валидна.',employee.brigade)
            error = 'Форма не валидна.'
            info['error'] = form.errors
            # print(form.errors)
    else:
        form = EmployeeForm(instance=employee)

    info['form'] = form
    info['name'] = employee.name
    info['position'] = employee.position
    info['boss'] = employee.boss
    info['selected_brigade'] = employee.brigade

    return render(request, 'edit_employee.html', info)

def view_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'view_employee.html', {'employee': employee})


def sign_up_by_plant2(request, pk):
    error = None
    brigades =[]
    positions=[]
    br = Brigade.objects.all().values_list('name', flat=True)
    for b in br:
        brigades.append(b)
    pos = Position.objects.all().values_list('name', flat=True)
    for p in pos:
        positions.append(p)
    info = {'good': None, 'error': None, 'brigades': brigades, 'positions': positions}
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            # users = Employee.objects.all().values_list('name', flat=True)
            # if username in users:
            #     error = 'Такой сотрудник уже существует.'
            # else:
            position = form.cleaned_data['position']
            boss = form.cleaned_data['boss']
            brigade = form.cleaned_data['brigade']
            br = Brigade.objects.get(name=brigade).id
            print('выбор',str(br),error,username,users)
                # Employee.objects.create(name=username, position=position, boss=boss, activ = True, brigade_id=br)
            # good = f'Приветствуем, {username}!'
            #     info['good'] = good
            info['error'] = error
        else:
            error = 'Форма не валидна.'
        info['error'] = error
    else:
        form = EmployeeRegistr()
    info['form'] = form
    info['name']=employee.name
    info['position']=employee.position
    info['boss'] = employee.boss
    info['selected_brigade']=employee.brigade
    return render(request, 'edit_employee.html',info)