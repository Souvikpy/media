from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from myapp.utilities import store_Image
# Create your views here.

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Sovik"
    return render(request,"myapp/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"post_demo.html")


def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="FeMale"
        else:
            gender="Male"
        send_mail("Thanks For Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(first_name,last_name),
        "sumon.bhattacharjee93@gmail.com",[email,],fail_silently=True)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,password,phno,gender,date,month,year))
    return render(request,"myapp/registration.html")


def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("Food")
        languages=request.POST.getlist("lang")
        return HttpResponse("<h1>{}{}<h1>".format(foods,languages))
    return render(request,'multiselect.html')

from django.core.files.storage import FileSystemStorage

def img(request):
    return render(request,"img.html")

def img_dis(request):
    file_url= False
    if request.method=="POST" and request.FILES:
        image=request.FILES['Souvik']
        print(image)
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)
                
    return render(request,"img_display.html",context={'file_url':file_url})

from myapp import forms
def builtin(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)#im creating a form instance with the data filled the all the firlds will get th
        #the specified value
        if form.is_valid():
            #cleaned_data is varible in form instance that holds the dictonary containing the data that we 
            #have filled
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            image=form.cleaned_data.get('image')
            store_image(image)
            data=form.cleaned_data
            return render(request,"display_data.html",context=data)
    form=forms.SampleForm()
    return render(request,"builtin.html",{'form':form})