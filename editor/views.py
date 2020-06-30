import json
import os
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from .models import ArticleContent
from django.http import HttpResponseRedirect
from django.urls import reverse

def handle_uploaded_file(f):
    print("f:", f.name)
    with open(os.path.join(settings.MEDIA_ROOT, 'images/{0}'.format(f.name)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return f.name, f.size


def upload_images(request):
    if request.method == 'POST':
        image_name, image_size = handle_uploaded_file(request.FILES['image'])
        return JsonResponse(
            {'file': {'url': '/media/images/{0}'.format(image_name), 'name': image_name, 'size': image_size},
             'success': 1}, safe=False)


def create_content(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        print(data)

        ac = ArticleContent()
        ac.content = data
        ac.save()

        print("src_result",ac.id)

        return JsonResponse({"message":"successful", "url":"/", "status":"201", "src_id":ac.id})

        # return HttpResponseRedirect(reverse("editor:display_content"))

        # return render(request, 'editor/content_detail.html', {'article_content': ac})


    if request.method == 'GET':
        print("this is editor get")
        return render(request, 'editor/create_content.html', {"message": "successful", "url": "/", "status": "200"})


def display_content(request, src_id=1):

    if request.method =='POST':
        print("wwwwwwwwwwwwwwwww")
        return render(request, 'editor/content_detail.html', {})
        # article = ArticleContent.objects.filter(content__contains={'time':c_time})
        # article_content = get_object_or_404(ArticleContent, pk=src_id)
        # print("article_content query",article_content)

    else:
        print("hahahahahah")
        article_content = get_object_or_404(ArticleContent, pk=src_id)
        return render(request, 'editor/content_detail.html')


def display_contents(request):
    if request.method == 'GET':
        article_content = ArticleContent.objects.all()
        return render(request, 'articles/article_list.html', {'articles': article_content})
    else:
        pass