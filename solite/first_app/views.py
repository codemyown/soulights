from django.shortcuts import render
from django.http import HttpResponse
from .models.contact import Contact
from .models.blog import Blog
from .models.course import Course
from .models.review import Review
from .models.contact_us import ContactUs
from .models.plain import Plain


# Create your views here.

def index(request):

    review = Review.get_all_reviews()
    blog = Blog.get_all_blogs()
    course = Course.get_all_course()
    plain = Plain.get_all_plains()
    data = {
        'blog':blog,
        'course':course,
        'review':review,
        'plain':plain
    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        my_contact = Contact(name = name,email = email,message = message)
        my_contact.save()
        
    return render(request,"index.html",data)


def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        my_contact = ContactUs(first_name = name,email = email,phone_no = number,message = message)
        my_contact.save()
        
        
    return render(request,"contact.html")



def blog(request):
    blog = Blog.get_all_blogs()
    
    return render(request,"blog.html")