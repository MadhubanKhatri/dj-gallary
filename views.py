from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Post
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        all_posts = Post.objects.all().order_by('-id')
        params = {"posts": all_posts}
        return render(request, self.template_name, params)


class UploadView(TemplateView):
    template_name = 'upload.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        img_title = request.POST['title']
        imgName = request.FILES['img_name']
        add_img = Post(title=img_title, img_field=imgName)
        add_img.save()
        messages.success(request, 'Image Added Succefully.')
        # print(imgName, title)
        return render(request, self.template_name)


class DeleteView(TemplateView):
    def get(self, request, id):
        delete_post = Post.objects.get(id=id)
        delete_post.delete()
        messages.success(request, 'Image Deleted Succefully.')
        return redirect('/')