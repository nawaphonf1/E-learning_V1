from django.shortcuts import render, redirect
from .models import User, VideoDB
from django.http import JsonResponse
from api.serializers import PointSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def update_video_progress(request):
    if request.method == "POST":
        video_id = request.POST.get("video_id")
        videoPro = request.POST.get("videopro")
        video_db = VideoDB.objects.get(pk=6)
        if video_id == "1":
            video_db.videoP1 = 1
            video_db.save()
        elif video_id == "2":
            video_db.videoP2 = 1
            video_db.save()
        elif video_id == "3":
            video_db.videoP3 = 1
            video_db.save()
        elif video_id == "4":
            video_db.videoP4 = 1
            video_db.save()
        elif video_id == "5":
            video_db.videoP5 = 1
            video_db.save()
        elif video_id == "6":
            video_db.videoP6 = 1
            video_db.save()
        elif video_id == "7":
            video_db.videoP7 = 1
            video_db.save()
        elif video_id == "8":
            video_db.videoP8 = 1
            video_db.save()
        elif video_id == "9":
            video_db.videoP9 = 1
            video_db.save()
        elif video_id == "10":
            video_db.videoP10 = 1
            video_db.save()
        elif video_id == "11":
            video_db.videoP11 = 1
            video_db.save()
        elif video_id == "12":
            video_db.videoP12 = 1
            video_db.save()
        elif video_id == "13":
            video_db.videoP13 = 1
            video_db.save()
        elif video_id == "14":
            video_db.videoP14 = 1
            video_db.save()
        elif video_id == "15":
            video_db.videoP15 = 1
            video_db.save()
        elif video_id == "16":
            video_db.videoP16 = 1
            video_db.save()
        elif video_id == "17":
            video_db.videoP17 = 1
            video_db.save()
        



def index(request):
    video_db = VideoDB.objects.get(pk=6)
    return render(request, 'User-page.html', {'video_db': video_db})

def quiz(request):
    correctAnswers = User.objects.all()
    return render(request,'quiz.html',{'correctAnswers': correctAnswers})

def admin(request):
    return render(request,'admin-page.html')

def save_data(request):
    if request.method == 'POST':
        correctAnswers = request.POST.get('correctAnswers')
        correctAnswers.User.objects.create(correctAnswers=correctAnswers)
        return render(request, 'quiz.html', {'correctAnswers': correctAnswers})
        
    return redirect('home')

def user_page(request):
    return render(request, 'User_page.html')

@api_view(['GET']) 
def Userlist(request):
    if request.method == 'GET':
        User = User.objects.all()
        serializer=PointSerializer(User, many=True)
        return JsonResponse({'pointtest':serializer.data},safe=False)