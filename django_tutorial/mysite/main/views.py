from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import hotel ,desc,rats,price,tora,address
from .forms import CreateNewList
# Create your views here.

def index(response,id):
  h= hotel.objects.get(id=id)
  
  if response.method == "POST":
      if response.POST.get("create"):  
        d = response.POST.get("new")
       
        if len(d)>5:
          h.desc_set.create(description=d)
        else:
         print("invalid")
  return render(response, "main/list.html", {"h":h})

  if len(r)>5:
          h.rats_set.create(ratings=r)
  else:
         print("invalid")
  return render(response, "main/list.html", {"h":h})


def home(response):
 return render(response, "main/home.html", {})



def detail(response, id):
    h = hotel.objects.get(id=id)
    return render(response, "main/book.html", {"h":h})

def create(response):
  if response.method =="POST":
     form = CreateNewList(response.POST)

     if form.is_valid():
        n=form.cleaned_data["name"]
        t = hotel(name=n)
        t.save()
      
     return HttpResponseRedirect("form/%i" %t.id)
  else:
    form = CreateNewList()
  return render(response, "main/create.html", {"form":form})
  
 
 