from django.shortcuts import render

# Create your views here.
def home(request):
    resdic={}
    resdic["name"]="Shreya"
    resdic["age"]=15
    return render(request,"index.html",resdic)
