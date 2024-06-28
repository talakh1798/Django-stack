from django.shortcuts import render

from django.shortcuts import render
from time import gmtime, strftime

# from datetime import datetime

    
def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", gmtime())
        # "time":datetime.strptime('Jun 28, 2024 05:08 PM', '%b %d %Y %I:%M%p')
    }
    return render(request,'index.html', context)


