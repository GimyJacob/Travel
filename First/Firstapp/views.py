from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Person


# Create your views here.
# def demo(request):
#    return render(request,'home..html')
def about(request):
    ob=Place.objects.all()
    obj=Person.objects.all()
    return render(request,'index.html',{'result':ob, 'result1':obj})
# def contact(request):
#     return HttpResponse('haii in contact')
# def demo(request):
#     nam="india"
#     return render(request,'home..html',{'obj':nam})