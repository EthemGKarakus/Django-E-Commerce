from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    university="Türk Alman Üniversitesi"
    dept="Mechatronik"
    context={"university":university,"department":dept}
    return render(request, "index.html",context)
