from django.shortcuts import render
from details.models import Movies
from details.form import movieform


def base(request):
    return render(request,'base.html')


def home(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        i=request.FILES['i']
        b= Movies.objects.create(name=t,description=a,year=p,images=i)
        b.save()
        return addmovies(request)
    return render(request, 'home.html')

def addmovies(request):
    k= Movies.objects.all()
    return render(request, 'addmovies.html',{'b':k})

def moviedetail(request,p):
    b=Movies.objects.get(id=p)
    return render(request,'movie.html',{'b':b})

def moviedelete(request,p):
    b = Movies.objects.get(id=p)
    b.delete()
    return addmovies(request)




def movieedit(request,p):
    b = Movies.objects.get(id=p)
    if (request.method=="POST"):
        form= movieform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return addmovies(request)

    form=movieform(instance=b)
    return render(request,'edit.html',{'form':form})

