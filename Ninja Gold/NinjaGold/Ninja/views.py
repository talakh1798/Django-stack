from django.shortcuts import render,redirect
import random
from datetime import datetime

def page(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['activities']=[]

    ninja={
        'gold':request.session['gold'],
        'activities':request.session['activities']
        }

    return render(request,'index.html',ninja)    
def process(request):
    building=request.POST['building']
    if building=='farm':
        earn_gold=random.randint(10,20)
    elif building=='Cave':
        earn_gold=random.randint(10,20) 
    elif building=='House':
        earn_gold=random.randint(10,20)         
    elif building=='Quest':
        earn_gold=random.randint(-50,50)
    Date_Time = datetime.now().strftime('%B %d %Y %I:%M %p')
    if earn_gold >= 0:
        activity=f'Earned {earn_gold} from {building} on {Date_Time}' 
    else: 
        activity=f'lost{earn_gold} from{building} on {Date_Time}' 
    request.session['activities'].insert(0,activity)
    request.session['gold']+=earn_gold

    return redirect('/')     

    


