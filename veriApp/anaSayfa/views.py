from django.shortcuts import render
from django.http import HttpResponse

db = {
    "Main":[
        {
            "title":"Süt Ürünleri",
            "imageUrl":"https://img.freepik.com/free-photo/variety-dairy-products-cookies_23-2148239912.jpg?w=1060&t=st=1701710813~exp=1701711413~hmac=d42e993b4130c03781235729c72f2578bbd7ec502b2dbbd856185458a740197d",
            "slug":"",

        },
         {
            "title":"Baklagiller",
            "imageUrl":"https://img.freepik.com/free-photo/view-allergens-commonly-found-grains_23-2150170288.jpg?w=1060&t=st=1701710783~exp=1701711383~hmac=c407bd796aa42a30f0aec2a29bb08275936a0d5fa507c817e0a1a3e33c218ef6",
            "slug":"",
            
        },
         {
            "title":"Atıştırmalık",
            "imageUrl":"https://img.freepik.com/free-photo/top-view-fast-food-meal_23-2148273108.jpg?w=1060&t=st=1701699424~exp=1701700024~hmac=921d2ffa1f0068a65bdfce80384f582b7d26226e2ade1c0097ed63a5993cf8f1",
            "slug":"",
            
        }

    ],
    "SütÜrünleri":[
        {
            "title":"Sütler",
            "imageUrl":"https://img.freepik.com/free-photo/milk-glass-bottle-background-farm_1142-40886.jpg?t=st=1701682601~exp=1701686201~hmac=837adcdbce97d3d0bd163450ff8a7f29ff3bdaedd106063b2d678ab7ffe8f3c9&w=740",
            "Sütler": [{
                "title":"Torku Süt",
                "kalori":"Kalori: 200",
                "icindekiler":"% 1,5 yağlı inek sütü (hayvansal)",
                "gluten": True,
                "helal": True,
                "laktoz": True,
                "mensai":"Menşei Ülke: Türkiye",
                "imageUrl":"https://images.migrosone.com/sanalmarket/product/46054060/torku-yarim-yagli-sut-1l-17c30e-1650x1650.jpg"
            },
            {
                "title":"İçim Doğal Süt",
                "kalori":"Kalori: 200",
                "icindekiler":"%3 yağlı inek sütü",
                "gluten": False,
                "helal": True,
                "laktoz": True,
                "mensai":"Menşei Ülke: Türkiye",
                "imageUrl":"https://images.migrosone.com/sanalmarket/product/11013025/11013025-cf97ab-1650x1650.jpg"
            },
            {
                "title":"Sek Süt",
                "kalori":"Kalori: 300",
                "icindekiler":"UHT Yağlı süt (%3 Yağlı)",
                "gluten": False,
                "helal": True,
                "laktoz": False,
                "mensai":"Menşei Ülke: Türkiye",
                "imageUrl":"https://images.migrosone.com/sanalmarket/product/11012000/11012000-ad06f1-1650x1650.jpg"
            },
           
            ],
            
        },
        {
            "title":"Yoğurtlar",
            "imageUrl":"https://img.freepik.com/free-photo/greek-yoghurt_144627-27070.jpg?w=996&t=st=1701682488~exp=1701683088~hmac=16e324c284586a7f8c52b4a9ebe7ef6594d691fcc757c7b63b78de388072535f",
            "slug":","
        },
        {
            "title":"Peynirler",
            "imageUrl":"https://img.freepik.com/free-photo/french-swiss-cheeses-rustic-wood-tray-generated-by-ai_188544-17019.jpg?t=st=1701682650~exp=1701686250~hmac=8167222516938ecb44d18ddb458ec9471f02aee29c44074ae9f0683d88f82160&w=1380",
            "slug":","
        }
    ]

}

def home(request):
    Sections = db["Main"]
    return render(request, "anaSayfa.html",{'sections': Sections})

def sutUrunlerı(request):
   SutUrunlerı = db["SütÜrünleri"]

   return render(request, "sutUrunlerı.html", {'products': SutUrunlerı })

def laktozsuzSut(request):
   Sutler = db["SütÜrünleri"][0]["Sütler"]

   return render(request, "laktozsuzSut.html", {'sutler': Sutler})

def glutensizSut(request):
   Sutler = db["SütÜrünleri"][0]["Sütler"]

   return render(request, "glutensizSut.html", {'sutler': Sutler})

def sutler(request):
    Sutler = db["SütÜrünleri"][0]["Sütler"]
    return render(request, "sutler.html",{'sutler': Sutler})

def baklagıller(request):
    return HttpResponse("liste")

def atıstırmalıklar(request):
    return HttpResponse("liste")

def makarnalar(request):
    return HttpResponse("liste")

