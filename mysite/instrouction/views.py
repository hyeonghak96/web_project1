from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from instrouction.models import Instrouction


class InstrouctionLV(ListView):
    model = Instrouction

class InstrouctionDV(DetailView):
    model = Instrouction