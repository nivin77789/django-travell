from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1=Destination()
    dest2=Destination()
    
    dest1.name="Kerala"
    dest1.img="packag1.jpg"
    dest1.desc="City of gods ,gold and a place where you can feewl the beauty of nature"
    dest1.price=200
    
    dest2.name="Karnataka"
    dest2.img="packag2.jpg"
    dest2.desc="Village of gods and a place where you can feewl the beauty of nature"
    dest2.price=500
    
    dests=[dest1,dest2]
    return render(request,'index.html',{'dests':dests})