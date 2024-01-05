from django.shortcuts import render
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Who', ' Pilot', '123'],
        'obj':{
            'car': 'AUDI',
            'age': '20',
            'hobby': 'serial killer'
        }
    }
    return render(request,'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
