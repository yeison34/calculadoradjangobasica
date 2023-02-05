from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def operar(request):
    num1=int(request.GET["numero1"])
    num2=int(request.GET["numero2"])
    op=int(request.GET["op"])
    print(num1)
    resultado=0
    if(op==1):
        resultado=(num1+num2)
    
    if(op==2):
        resultado=(num1-num2)    
    
    if(op==3):
        resultado=(num1*num2)    
        
    if(op==4):
        resultado=(num1/num2)   
    
    mensaje={
            "resultado":resultado
    }
    
    
    return render(request,"index.html",mensaje)  