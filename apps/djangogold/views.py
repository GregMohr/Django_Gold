from django.shortcuts import render, redirect
import random

def index(request):
    if 'activity_log' not in request.session:
        request.session['activity_log']=[]
    if 'your_gold' not in request.session:
        request.session['your_gold']=0
    return render(request,'djangogold/index.html')

def process_money(request):
    building = request.POST['building']
    if building == "farm":
        new_gold=random.randint(10,20)
        request.session['your_gold']+=new_gold
    elif building == "cave":
        new_gold=random.randint(5,10)
        request.session['your_gold']+=new_gold
    elif building == "house":
        new_gold=random.randint(2,5)
        request.session['your_gold']+=new_gold
    elif building == "casino":
        new_gold=random.randint(-50,50)
        request.session['your_gold']+=new_gold

    # print(new_gold)
    new_activity = {"actText": "You {} {} from the {}".format("earned" if new_gold > 0 else "lost", abs(new_gold), building), "actColor": "green" if new_gold > 0 else "red"}
    request.session['activity_log'].append(new_activity)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
