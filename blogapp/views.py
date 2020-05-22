from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects    #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):   #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #객체.delete()하면 데이터베이스에서 지우는거임
    return redirect('/blog/'+str(blog.id))    #위에 있는 것 다 처리한 다음에 URL로 넘겨라   #blog.id는 int형인데 url은 항상 str형이기때문에 str형변환해줘야함
    
