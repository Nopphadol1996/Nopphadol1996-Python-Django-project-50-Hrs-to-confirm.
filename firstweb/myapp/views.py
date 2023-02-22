from django.shortcuts import render
from django.http import HttpResponse
# django คือ แพ็คเกจ หลัก .http คือ แพ็คเกจย่อย  HttpResponse คือฟังก์ชั่นที่ทำให้โชว์ข้อความหน้าเว็บได้

def Home(request):
 # return HttpResponse('สวัสดีชาวโลก...')
    
    return render(request,'myapp/home.html')