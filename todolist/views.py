from django.shortcuts import render , HttpResponse , redirect
import pymongo as py
from django.template import loader
from django.http import HttpResponse
from django.template import loader




def home(request):
    return render(request , "html_home.html")
# Create your views here.

def sign(request):
    return render(request , "signup.html")

def sign_up(request):
    name = request.POST.get('s_name', "defalt")
    pas = request.POST.get('s_password', "defalt")
    if (name == "" or pas == ""):
        return HttpResponse("name or what to do cannot be empty")
    client = py.MongoClient("mongodb://localhost:27017")
    db = client["todoproject"]
    collection = db["password_manager"]
    collection.insert_one({"name":name , "password":pas}) 
    return render(request , "html_home.html")
    
def adding(request):
    todo = request.POST.get('todo', "defalt")
    name = request.POST.get('name', "defalt")
    pas = request.POST.get('password', "defalt")
    if (name == "" or todo == ""):
        return HttpResponse("name or what to do cannot be empty")
    client = py.MongoClient("mongodb://localhost:27017")
    db = client["todoproject"]
    collect = db["password_manager"]
    all_data = collect.find({"name":name} , {"_id" : 0 , "password" : 1})
    for list1 in all_data:
        for password in list1.values():
            if(password == pas):
                client = py.MongoClient("mongodb://localhost:27017")
                db = client["todoproject"]
                collection = db["todolist"]
                idd = collection.count_documents({})
                collection.insert_one({"_id": idd+1 , "Name" : name ,"password":pas,"todo" : todo})
                print(request.POST.get('todo', "defalt"))
                
                response = redirect(".")
                return response
    return HttpResponse("Incorrect password or name kindly check")

def return_list(request):
    return render(request , "return_list.html")

def returning(request):
    
    client = py.MongoClient("mongodb://localhost:27017")
    db = client["todoproject"]
    collection = db["todolist"]
    name = request.POST.get("name" , "defalt")
    pas = request.POST.get('password', "defalt")
    if (name == "" or pas == ""):
        return HttpResponse("name or what to do cannot be empty")
    all_data = collection.find({"Name": name , "password" : pas} , {"_id": 0  ,"todo": 1})
    
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
    
    client = py.MongoClient("mongodb://localhost:27017")
    db = client["todoproject"]
    collect = db["password_manager"]
    all_data = collect.find({} , {"_id" : 0 , "password" : 1})
    for list1 in all_data:
        for password in list1.values():
            if(password == pas): 
    
                return render(request ,"return_list.html", context)
    return HttpResponse("No data Exist with given password")   
   