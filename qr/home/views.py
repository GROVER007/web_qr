from pathlib import Path
import os.path
from django.shortcuts import render
import qrcode

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    return render(request,"temp1.html")

def result(request):
    qr = None
    if request.method == "POST":
        data = request.POST.get("text")
        qr = qrcode.make(data)
        path = os.path.join(BASE_DIR,"static/qr/test1.png")
        qr.save(path)
    return render(request,"result.html")
