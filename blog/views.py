from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

data= {
    "blogs":[
        {
            "id":1,
            "title":"Bootstrap Nedir?",
            "image":"What-is-Bootstrap.webp",
            "is_active":True,
            "is_home":False,
            "description":"Bootstrap nedir,ne işe yarar,nerelerde kullanılır?",
            "description_detail":"<strong>Bootstrap Nedir?</strong><br>Bootstrap, web uygulamaları ve mobil cihazlar için hızlı ve etkili bir şekilde kullanılan açık kaynaklı bir CSS ve JavaScript kütüphanesidir. Twitter tarafından geliştirilen bu araç, birçok hazır bileşen ve stil içerir, böylece web geliştiricileri için temel tasarım ve işlevsellik unsurlarını sağlar.<br><strong>Ne İşe Yarar?</strong><br>Bootstrap, geliştiricilere temel tasarım öğelerini ve bileşenlerini önceden oluşturulmuş bir yapı içinde sunar. Bu, geliştirme sürecini hızlandırır ve web uygulamalarının mobil cihazlarda uyumlu olmasını kolaylaştırır. Ayrıca, tarayıcı uyumluluğunu artırarak farklı platformlarda tutarlılık sağlar.<br><strong>Nerelerde Kullanılır?</strong><br>Bootstrap, genellikle web sitelerinin ve uygulamalarının ön yüz tasarımında kullanılır. Özellikle, hızlı prototip oluşturma, duyarlılık (responsive design) sağlama ve temel UI bileşenlerini kolayca ekleyebilme amacıyla tercih edilir."
        },
        {
            "id":2,
            "title":"Django Nedir?",
            "image":"django1.jpg",
            "is_active":True,
            "is_home":False,
            "description":"Django nedir,ne işe yarar,nerelerde kullanılır?",
            "description_detail":"<strong>Django Nedir?</strong><br> Django, web uygulamaları geliştirmek için kullanılan bir Python çatısıdır.<br><strong>Ne İşe Yarar?</strong><br>Django, hızlı ve güvenli web uygulamaları oluşturmanızı sağlar. Veritabanı yönetiminden oturum kontrolüne kadar birçok temel işlevi sağlar.<strong><br>Nerelerde Kullanılır?</strong><br> Django, haber sitelerinden sosyal medya platformlarına kadar çeşitli web projelerinde kullanılır. Özellikle veritabanı işlemleri ve kullanıcı yönetimi gibi karmaşık işlevler için idealdir."
        },
        {
            "id":3,
            "title":"Numpy Nedir?",
            "image":"Numpy2.png",
            "is_active":True,
            "is_home":False,
            "description":"Numpy nedir,ne işe yarar,nerelerde kullanılır?",
            "description_detail":"<strong><br>Numpy Nedir?</strong><br>Numpy, Python dilinde bilimsel hesaplamalar ve veri işleme için kullanılan bir kütüphanedir.<strong><br>Ne İşe Yarar?</strong><br> Numpy, çok boyutlu dizileri ve matrisleri işleme yetenekleriyle bilinir. Hızlı ve etkili veri işleme imkanı sağlar.<strong><br>Nerelerde Kullanılır?</strong><br> Bilimsel hesaplamalar, veri analizi, mühendislik, yapay zeka ve istatistik gibi alanlarda sıklıkla kullanılır. Özellikle büyük veri setleri üzerinde etkili çalışır."
        },
        {
            "id":4,
            "title":"Selenium Nedir?",
            "image":"selenium_2.jpg",
            "is_active":True,
            "is_home":False,
            "description":"Selenium nedir,ne işe yarar,nerelerde kullanılır?",
            "description_detail":"<strong><br>Selenium Nedir?</strong><br> Selenium, web uygulamalarını otomasyon için kullanılan bir açık kaynaklı araçtır.<strong><br>Ne İşe Yarar?</strong><br> Selenium, web tarayıcılarını otomatik olarak kontrol etmenizi ve test senaryoları oluşturmanızı sağlar. Ayrıca, web uygulamalarını otomatik olarak test etmek ve veri çekmek için kullanılabilir.<strong><br>Nerelerde Kullanılır?</strong><br> Selenium, web uygulama test otomasyonu, veri kazıma, otomatik web işlemleri ve performans testleri gibi birçok alanda kullanılır. Ayrıca, tarayıcı tabanlı web uygulamalarının test edilmesi için sıkça kullanılır."
        }
        
    ]
}

def index(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request,"blog/index.html",context)

def blogs(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request,"blog/blogs.html",context)

def blog_details(request,id):
    blogs=data["blogs"]
    selectedBlog=None

    for blog in blogs:
        if blog["id"]==id:
            selectedBlog=blog
    return render(request,"blog/blogs-detail.html",{
        "blog": selectedBlog
    })
