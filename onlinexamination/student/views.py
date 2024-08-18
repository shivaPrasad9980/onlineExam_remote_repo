from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def StudentSignupView(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request,'student/signup.html',{'form':form})