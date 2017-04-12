from django.shortcuts import render

def index(request):
    return render(request,'training/training_/home.html')


def train_me(request):
    return render(request,'training/train_me/train.html')