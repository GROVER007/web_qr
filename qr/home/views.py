from pathlib import Path
import os.path
from django.shortcuts import render
import qrcode
import datetime
from home.models import Feedback

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    return render(request,"temp1.html")

def result(request):
    qr = None
    if request.method == "POST":
        data = request.POST.get("text")
        qr = qrcode.make(data)
        path = os.path.join(BASE_DIR,"static/qr/mmqr.png")
        qr.save(path)
    return render(request,"result.html")

def feedback(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        fb = Feedback(fname = fname,lname = lname,email = email,comment = comment,date = datetime.date.today())
        fb.save()
        return render(request,"thanks.html")
    else:
        return render(request,"result.html")
