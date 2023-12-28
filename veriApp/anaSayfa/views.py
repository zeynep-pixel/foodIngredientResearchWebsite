from django.shortcuts import render
from django.http import HttpResponse
import json

with open("anaSayfa/db.json") as json_file:
    db =json.load(json_file)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next



Laktozsuzlar = LinkedList()
elemanlar = []
i = 0
while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["laktoz"] == False:
             elemanlar.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
           
            i = i + 1

i = 0
while(i<len(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"])):
            if db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i]["laktoz"] == False:
             elemanlar.append(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i])
           
            i = i + 1

for eleman in elemanlar:
    Laktozsuzlar.append(eleman)


Veganlar = LinkedList()
elemanlar = []
i = 0
while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["vegan"] == True:
             elemanlar.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
           
            i = i + 1


i = 0
while(i<len(db["Main"][1]["Atıştırmalıklar"][0]["Çikolatalar"])):
            if db["Main"][1]["Atıştırmalıklar"][0]["Çikolatalar"][i]["vegan"] == True:
             elemanlar.append(db["Main"][1]["Atıştırmalıklar"][0]["Çikolatalar"][i])
           
            i = i + 1


for eleman in elemanlar:
    Veganlar.append(eleman)


Organikler = LinkedList()
elemanlar = []
i = 0
while(i<len(db["Main"][1]["Atıştırmalıklar"][1]["Cipsler"])):
            if db["Main"][1]["Atıştırmalıklar"][1]["Cipsler"][i]["organik"] == True:
             elemanlar.append(db["Main"][1]["Atıştırmalıklar"][1]["Cipsler"][i])
           
            i = i + 1

i = 0
while(i<len(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"])):
            if db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i]["organik"] == True:
             elemanlar.append(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i])
           
            i = i + 1


for eleman in elemanlar:
    Organikler.append(eleman)




    

def home(request):
    Sections = db["Main"]
    Liste = Laktozsuzlar
    ListeTwo = Veganlar
    ListeThree = Organikler
    return render(request, "anaSayfa.html",{'sections': Sections, 'liste':Liste, 'listetwo':ListeTwo, 'listethree':ListeThree})

def sutUrunlerı(request):
   SutUrunlerı = db["Main"][0]["SütÜrünleri"]
   Sutler = db["Main"][0]["SütÜrünleri"][0]["Sütler"]
   Yogurtlar = db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"]
   
   return render(request, "sutUrunlerı.html", {'products': SutUrunlerı , 'sutler': Sutler,  'yogurtlar': Yogurtlar })

def sutler(request):
   SutUrunlerı = db["Main"][0]["SütÜrünleri"]
   Sutler = db["Main"][0]["SütÜrünleri"][0]["Sütler"]
   if request.method == "POST":
        choose=request.POST.getlist("choose")
        Sutler=[]
        i = 0
        #append methodu ile veriler eklendi
        if choose==["Laktozsuz"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["laktoz"] == False:
             Sutler.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
            i = i + 1

        if choose==["Vegan"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["vegan"] == True:
             Sutler.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
            i = i + 1

        if choose==["Laktozsuz","Vegan"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][0]["Sütler"])):
            if (db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["laktoz"] == False and db["Main"][0]["SütÜrünleri"][0]["Sütler"][i]["vegan"] == True) :
             Sutler.append(db["Main"][0]["SütÜrünleri"][0]["Sütler"][i])
            i = i + 1
   return render(request, "sutler.html",{'products': SutUrunlerı , 'sutler': Sutler})


def yogurtlar(request):
   
   SutUrunlerı = db["Main"][0]["SütÜrünleri"]
   Yogurtlar = db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"]
   if request.method == "POST":
        choose=request.POST.getlist("choose")
        Yogurtlar=[]
        i = 0
        #append methodu ile veriler eklendi
        if choose==["Laktozsuz"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"])):
            if db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i]["laktoz"] == False:
             Yogurtlar.append(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i])
            i = i + 1

        if choose==["Vegan"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"])):
            if db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i]["organik"] == True:
             Yogurtlar.append(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i])
            i = i + 1

        if choose==["Laktozsuz","Vegan"]:
           while(i<len(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"])):
            if (db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i]["laktoz"] == False and db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i]["organik"] == True) :
             Yogurtlar.append(db["Main"][0]["SütÜrünleri"][1]["Yogurtlar"][i])
            i = i + 1
            
   return render(request, "yogurtlar.html",{'products': SutUrunlerı , 'yogurtlar': Yogurtlar})

def peynirler(request):
   SutUrunlerı = db["Main"][0]["SütÜrünleri"]
   Peynirler = db["Main"][0]["SütÜrünleri"][2]["Peynirler"]
   return render(request, "peynirler.html",{'products': SutUrunlerı , 'peynirler': Peynirler})


def atıştırmalıklar(request):
   Atıştırmalıklar = db["Main"][1]["Atıştırmalıklar"]
   Çikolatalar = db["Main"][1]["Atıştırmalıklar"][0]["Çikolatalar"]
   Cipsler = db["Main"][1]["Atıştırmalıklar"][1]["Cipsler"]
   Bisküviler = db["Main"][1]["Atıştırmalıklar"][2]["Bisküviler"]
   return render(request, "atıştırmalıklar.html", {'products': Atıştırmalıklar , 'sutler': Çikolatalar,  'yogurtlar': Cipsler, 'bisküviler': Bisküviler })

def çikolatalar(request):
   Atıştırmalıklar = db["Main"][1]["Atıştırmalıklar"]
   Çikolatalar = db["Main"][1]["Atıştırmalıklar"][0]["Çikolatalar"]
   return render(request, "çikolatalar.html",{'products': Atıştırmalıklar , 'sutler': Çikolatalar })

def cipsler(request):
   Atıştırmalıklar = db["Main"][1]["Atıştırmalıklar"]
   Cipsler = db["Main"][1]["Atıştırmalıklar"][1]["Cipsler"]
   return render(request, "cipsler.html",{'products': Atıştırmalıklar , 'sutler': Cipsler })

def bisküviler(request):
   Atıştırmalıklar = db["Main"][1]["Atıştırmalıklar"]
   Bisküviler = db["Main"][1]["Atıştırmalıklar"][2]["Bisküviler"]
   return render(request, "bisküviler.html",{'products': Atıştırmalıklar , 'sutler': Bisküviler })