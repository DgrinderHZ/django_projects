from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Make, Auto


class MainView(LoginRequiredMixin, View):
    """
    Fetshes the Autos list and the makes count.
    """
    def get(self, request):
        al = Auto.objects.all()
        mc = Make.objects.all().count()

        params = {'auto_list': al, 'make_count': mc}
        return render(request, 'autos/auto_list.html', params)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        params = {'make_list': ml}
        return render(request, 'autos/make_list.html', params)


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
