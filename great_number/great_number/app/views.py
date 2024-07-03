from django.shortcuts import render, redirect
import random 

def home(request):
    if "number" not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['msg'] = ""
    return render(request, 'index.html')

def guess(request):
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        number = request.session['number']
        
        if guess < number:
            request.session['msg'] = "Too low!"
        elif guess > number:
            request.session['msg'] = "Too high!"
        else:
            request.session['msg'] = f"Correct! The number was {number}"
            request.session['number'] = random.randint(1, 100)  
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
            

   


