from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, Topic, Webpage , Usercustom
from . forms import FormName , NewuserForm
# # This is a simple view that returns a plain text response
# def index(request):
#     return HttpResponse("Hello, this is the index view.")

# -------------------------------------------------------------------------------------------------------

# # This is a simple view that returns a string response
# def index(request):
#     return render(request, 'template_example/index.html')

# -------------------------------------------------------------------------------------------------------

# # This view renders a template with a context dictionary
# def index(request):
#     my_dict = {'insert_me': "Now I am coming from the views.py file!"}
#     return render(request, 'template_example/index.html', context=my_dict)

# -------------------------------------------------------------------------------------------------------

# This view retrieves all AccessRecord objects, orders them by date, and passes them to the template
def index(request):
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': Webpages_list, 
                 'message': "Hello, Welcome!",
                 'number': 5}  
    return render(request, 'template_example/index.html', context=date_dict)

def user_list(request):
    users = Usercustom.objects.order_by('first_name')
    user_dict = {'users': users}
    return render(request, 'template_example/user_list.html', context=user_dict)

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            print(form.cleaned_data)
    return render(request, 'template_example/form_page.html',{'form':form})


def users(request):
    form = NewuserForm()

    if request.method == 'POST':
        form = NewuserForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form.save(commit=True)
            return index(request)
        
        else:
            print(form.errors)
    return render(request, 'template_example/signup.html', {'form': form})