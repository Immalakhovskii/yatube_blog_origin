from django.http import HttpResponse

def index(request):
    return HttpResponse('Это самое начало Yatube')

def group_posts(request, slug):
    return HttpResponse(f'Страница группы {slug}')
