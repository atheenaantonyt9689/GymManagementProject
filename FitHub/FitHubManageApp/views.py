from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from FitHubManageApp.forms import AdminstratorCreateForm, TrainerCreateForm


# Create your views here.
class SuperAdminDashBoardView(TemplateView):
    template_name = "FitHubManageApp/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FitHub'
        return context


class AdminDashBoardView(TemplateView):
    template_name = "FitHubManageApp/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FitHub'
        return context


class TrainerDashBoardView(TemplateView):
    template_name = "FitHubManageApp/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FitHub'
        return context


class AdministratorCreateView(CreateView):
    model = User
    form_class = AdminstratorCreateForm
    template_name = 'FitHubManageApp/Admin/admininstrator_create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class AdministratorUpdateView(UpdateView):
    model = User
    form_class = AdminstratorCreateForm
    template_name = 'FitHubManageApp/Admin/administrator_update.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class AdministratorListView(ListView):
    model = User
    template_name = 'FitHubManageApp/Admin/adminstrator_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrators'] = User.objects.filter(groups__name='Administrator')
        return context


class AdministratorDeleteView(DeleteView):
    model = User
    template_name = 'FitHubManageApp/Admin/admin_delete.html'
    success_url = reverse_lazy('fithub_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerCreateView(CreateView):
    model = User
    form_class = TrainerCreateForm
    template_name = 'FitHubManageApp/Trainer/trainer_create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class TrainerUpdateView(UpdateView):
    model = User
    form_class = TrainerCreateForm
    template_name = 'FitHubManageApp/Trainer/trainer_update.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class TrainerListView(ListView):
    model = User
    template_name = 'FitHubManageApp/Trainer/trainer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrators'] = User.objects.filter(groups__name='Trainer')
        return context


class TrainerDeleteView(DeleteView):
    model = User
    template_name = 'FitHubManageApp/Trainer/trainer_delete.html'
    success_url = reverse_lazy('fithub_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
