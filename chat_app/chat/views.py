from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse, HttpResponse
import datetime
# Create your views here.
def main_view(request):
    chat = request.POST['room_name']
    user = request.POST['user']
    apply_filter = Chat.objects.filter(name=chat)
    if apply_filter.exists():
        return redirect('/chat/'+chat+'/'+user)
    else:
        Chat.objects.create(name=chat)
        return redirect('/chat/'+chat+'/'+user)

def chat_view(request, chat, user):
    data = {
        'chat': chat,
        'user': user,
    }
    return render(request, 'chat/index.html', data) 

def read_message(request, chat, user): 
    room = Chat.objects.get(name=chat)
    message = Message.objects.filter(room=room.id)
    return JsonResponse({'res': list(message.values())}, safe=False)

def post_message(request, chat, user):
    title = request.POST['title']
    room = Chat.objects.get(name=chat)
    Message.objects.create(title=title, sender=user, room=room, date=datetime.date.today())
    return HttpResponse("messge posted")

def get_time(request):
    obj = datetime.datetime.now().time()
    return JsonResponse({'res': obj},safe=False)