from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm

def index(requests):
    if requests.method=="POST":
        form=ListForm(requests.POST)
        
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(requests,"list.html",{"all_items":all_items})
    else:
        all_items = List.objects.all
        return render(requests,"list.html",{"all_items":all_items})
    
def delete(request,list_id):
    item =List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')


def complete(requests,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')

def incomplete(requests,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')

def edit(requests,list_id):
    if requests.method=="POST":
        item=List.objects.get(pk=list_id)
        form=ListForm(requests.POST , instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(requests,"edit.html",{"item":item})
  