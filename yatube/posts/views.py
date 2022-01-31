from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Yatube main'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube',
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Yatube groups'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context, slug)
