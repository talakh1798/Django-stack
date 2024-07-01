from django.shortcuts import render,redirect

def count_time(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
    return render(request,'index.html')
#return render(request,'index.html',{'count'=request.session['count]}) --setsession 
      
def destroy_session(request):
    if 'count' in request.session:
        del request.session['count']
    return redirect('/')
 
def add(request):
    if 'count' in request.session:
        request.session['count']+=2
    else:
        request.session['count']=1
    return render(request,'index.html')  
