from django.shortcuts import render
from .forms import StudentForm
# Create your views here.


def index(request):
    form = StudentForm(None or request.POST)
    if form.is_valid():
        print("form is valid")
    return render(request, 'index.html', {'form': form})
