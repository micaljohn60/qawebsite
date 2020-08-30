from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Questions,Solutions
from .import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):   
    questions = Questions.objects.all()
    paginator = Paginator(questions,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'qas/index.html',{'questions':page_obj})

def question_detail(request,qids):
    questions = Questions.objects.get(id=qids)
    details = Solutions.objects.filter(qid=qids)
    if request.method == 'POST':          
        form = forms.GiveSolution(request.POST)
        if form.is_valid():            
            instance = form.save(commit =False)        
            instance.qid = questions
            instance.author = request.user
            instance.save()
            return redirect('questions:questiondetail',qids)
    else:
        form = forms.GiveSolution()            
    return render(request,'qas/detail.html',{'details':details,'form':form,'question':questions})

@login_required
def askquestion(request):
    if request.method == 'POST':
        form = forms.AskQuestion(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('questions:questionlistis')
    else:
        form = forms.AskQuestion()
    return render(request,'qas/askquestion.html',{'form':form})
    