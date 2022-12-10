from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from qrcode import *
import time
from PIL import Image
from qrcode.main import make

from app.forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Create your views here.
def qr(request):
    scheme = request.scheme + '://' + request.get_host()
    img = make(scheme)
    img_name = 'qr' + str(time.time()) + '.png'
    img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
    return render(request, 'qr.html', {'img_name': img_name})


@login_required
def profile(request):
    return render(request, "profile.html")
