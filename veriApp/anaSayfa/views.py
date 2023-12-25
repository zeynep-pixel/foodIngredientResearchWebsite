from django.shortcuts import render
from django.http import HttpResponse
import json

with open("anaSayfa/db.json") as json_file:
    db =json.load(json_file)

def home(request):
   
    Sections = db["Main"]            
    return render(request, "anaSayfa.html",{'sections': Sections,  })

def sutUrunlerı(request):
   SutUrunlerı = db["Main"][0]["SütÜrünleri"]
   Sutler = db["Main"][0]["SütÜrünleri"][0]["Sütler"]
   Yogurtlar = db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"]
   
   return render(request, "sutUrunlerı.html", {'products': SutUrunlerı , 'sutler': Sutler,  'yogurtlar': Yogurtlar })

def sutler(request):
   SutUrunlerı = db["Main"][0]["SütÜrünleri"]
   Sutler = db["Main"][0]["SütÜrünleri"][0]["Sütler"]
   if request.method == "POST":
        fruits=request.POST.getlist("fruits")
        Sutler=[]
        i = 0
        #append methodu ile veriler eklendi
        if fruits==["Laktozsuz"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["laktoz"] == False:
             Sutler.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
            i = i + 1

        if fruits==["Vegan"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["vegan"] == True:
             Sutler.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
            i = i + 1

        if fruits==["Laktozsuz","Vegan"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if (db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["laktoz"] == False and db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["vegan"] == True) :
             Sutler.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
            i = i + 1
   return render(request, "sutler.html",{'products': SutUrunlerı , 'sutler': Sutler})

def laktozsuzSut(request):
   Sutler = db["SütÜrünleri"][0]["all"]

   return render(request, "laktozsuzSut.html", {'sutler': Sutler})

def glutensizSut(request):
   Sutler = db["SütÜrünleri"][0]["all"]

   return render(request, "glutensizSut.html", {'sutler': Sutler})


def baklagıller(request):
    return HttpResponse("liste")

def atıstırmalıklar(request):
    return HttpResponse("liste")

def makarnalar(request):
    return HttpResponse("liste")

