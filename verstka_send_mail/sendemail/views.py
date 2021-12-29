from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def Home(request):
    return render(request, 'alpaca.html')


def HomeContact(request):
    if request.method == 'POST':
        nazvaniya = request.POST['nazvaniya']
        opisaniya = request.POST['opisaniya']
        kategorya = request.POST['kategorya']
        summa = request.POST['summa']
        myUrl = request.POST['myUrl']
        
        title=nazvaniya
        msg='Название проекта: '+ nazvaniya + '\nОписание проекта: '+opisaniya + '\nКатегория проекта: ' + kategorya + '\nНеобходимая сумма:  '+summa+'$' + '\nFile: '+myUrl

        print(nazvaniya, opisaniya, kategorya)
        send_mail(
            nazvaniya,
            msg,
            kategorya,
            ['kir32232@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'alpaca1.html')