from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'inject_me': 'Welcome from view index'}
    return render(request, 'index.html', context=my_dict)

def help(request):
    mydict = {'inject_help':'This is HELP Page'}
    return render(request, 'help.html', context=mydict)
