from django.shortcuts import render
from .forms import DetailForm
from .models import Detail
from django.views import View

class HomeView(View):
    def get(self, request):
        form = DetailForm
        candidates=Detail.objects.all()
        return render(request, 'students/home.html', {'candidates':candidates,'form':form})

    def post(self,request):
        form=DetailForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'students/home.html', {'form':form})

class CandidateView(View):
    def get(self,request,pk):
        candidate=Detail.objects.get(pk=pk)
        return render(request,'students/candidate.html',context={'candidate':candidate})

