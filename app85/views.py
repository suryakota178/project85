from django.shortcuts import render
from app85.models import Employee,Manager,SeniorManager
from django.views.generic import( TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView)



class Index(TemplateView):
    template_name = 'index.html'


class Create(CreateView):
    model = Employee
    fields = ('__all__')
    template_name = 'create.html'



class Table(ListView):
    model=Employee
    template_name = 'table.html'



class Detail(DetailView):
    model = Employee
    template_name = 'detail.html'