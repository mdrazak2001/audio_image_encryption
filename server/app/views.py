from django.shortcuts import redirect, render
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import random
import string
from Crypto.Cipher import AES
from .models import File
from .forms import FileForm

def home(request):
    context = {}
    form = FileForm() 
    context['form'] = form 
    for f in File.objects.all() :
        print(f.file)
    if request.method == 'POST':
        file = request.FILES['file']
        file_ob = File.objects.create(file = file)
        file_ob.save()
        # print(file_ob.file)
        return redirect('home')
    return render(request, 'app/home.html', context)

def encrypt():
    AES_KEY = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
    AES_IV = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))