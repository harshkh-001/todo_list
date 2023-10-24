from django.shortcuts import render , HttpResponse 
import pymongo as py
from django.template import loader
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request , "html_home.html")
# Create your views here.

def adding(request):
    todo = request.GET.get('todo', "defalt")
    name = request.GET.get('name', "defalt")
    if (name == "" or todo == ""):
        return HttpResponse("name or what to do cannot be empty")
    client = py.MongoClient("mongodb://localhost:27017")
    db = client["todoproject"]
    collection = db["todolist"]
    idd = collection.count_documents({})
    collection.insert_one({"_id": idd+1 , "Name" : name , "todo" : todo})
    print(request.GET.get('todo', "defalt"))
    return render(request , "html_home.html")


def return_list(request):
    return render(request , "return_list.html")

def returning(request):
    
    client = py.MongoClient("mongodb://localhost:27017")
    db = client["todoproject"]
    collection = db["todolist"]
    name = request.GET.get("name" , "defalt")
    
    all_data = collection.find({"Name": name} , {"_id": 0  ,"todo": 1})
    
    text = []
    count = 0
    list = []
    for todo_data in all_data:
        for x in todo_data.values():
        
        # mymember = todo_data.values()
            text.append(x)
        
            count = count + 1
           
        # template = loader.get_template('return_list.html')
    
    for z in range(1,count+1,1):
        list.append(z)
        
    context = {
        "variable" : z,
        "members" : text
    }
      
    return render(request ,"return_list.html", context)
         
   