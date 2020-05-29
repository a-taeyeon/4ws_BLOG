from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .form import BlogPost

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
    
def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = blogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  #post는 blog형 객체
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    #2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(reqeust, 'new.html', {'form':form})