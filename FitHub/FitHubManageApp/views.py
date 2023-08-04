from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, FormView

from FitHubManageApp.forms import AdminstratorCreateForm, TrainerCreateForm, LoginForm, ChangePasswordForm, \
    GymInformationCreateForm
from FitHubManageApp.models import GymInformation, GymAdministator


# Create your views here.
class SuperAdminDashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "FitHubManageApp/superadmin/super_admin_dash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FitHub'
        return context


class AdminDashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "FitHubManageApp/Admin/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FitHub'
        context["admin_side"] = "active"

        return context


class TrainerDashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "FitHubManageApp/Trainer/trainer_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FitHub'
        return context


class AdministratorCreateView(LoginRequiredMixin, CreateView):
    model = GymAdministator
    form_class = AdminstratorCreateForm
    template_name = 'FitHubManageApp/Admin/admininstrator_create.html'
    success_url = reverse_lazy('fithub_admin_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_management_tree"] = "menu-open"
        context["admin_add"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        messages.success(self.request, "Administrator added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class AdministratorUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = AdminstratorCreateForm
    template_name = 'FitHubManageApp/Admin/administrator_update.html'
    success_url = reverse_lazy('fithub_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_management_tree"] = "menu-open"
        context["admins_list"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        messages.success(self.request, "Administrator updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class AdministratorListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'FitHubManageApp/Admin/adminstrator_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrators'] = User.objects.filter(groups__name='Administrator')
        context["admins_list"] = "active"
        context["admin_management_tree"] = "menu-open"
        return context


class AdministratorDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'FitHubManageApp/Admin/admin_delete.html'
    success_url = reverse_lazy('fithub_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_management_tree"] = "menu-open"
        context["admins_list"] = "active"
        return context


class TrainerCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = TrainerCreateForm
    template_name = 'FitHubManageApp/Trainer/trainer_create.html'
    success_url = reverse_lazy('fithub_trainer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainer_add"] = "active"
        context["trainer_management_tree"] = "menu-open"
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        messages.success(self.request, "Trainer added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = TrainerCreateForm
    template_name = 'FitHubManageApp/Trainer/trainer_update.html'
    success_url = reverse_lazy('trainer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainer_management_tree"] = "menu-open"
        context["trainers_list"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        messages.success(self.request, "Trainer updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class TrainerListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'FitHubManageApp/Trainer/trainer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrators'] = User.objects.filter(groups__name='Trainer')
        context["trainers_list"] = "active"
        context["trainer_management_tree"] = "menu-open"
        return context


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'FitHubManageApp/Trainer/trainer_delete.html'
    success_url = reverse_lazy('fithub_trainer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainer_management_tree"] = "menu-open"
        context["trainers_list"] = "active"
        return context


class UserLogin(FormView):
    template_name = 'FitHubManageApp/Account/login.html'
    success_url = reverse_lazy('superadmin_dashboard')
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
        print("from authen ", user)
        if user is not None:
            login(self.request, user)
            # check the user is superuser
            if user.is_superuser:
                return redirect('superadmin_dashboard')
            if user.groups.filter(name='Administrator').exists():
                return redirect('fithub_admin_dashboard')
            elif user.groups.filter(name='Trainer').exists():
                return redirect('fithub_trainer_dashboard')
            else:
                return redirect('home')





        else:
            return redirect('fithub_login_view')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('fithub_login_view')


class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm
    template_name = "FitHubManageApp/Account/change_password.html"
    success_url = reverse_lazy('fithub_admin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

    def form_invalid(self, form):
        print("Form invalid")
        messages.error(self.request, "password mismatch occurred")
        return super().form_invalid(form)

    def form_valid(self, form):
        confirm_password = form.cleaned_data['confirm_password']
        print("password match")
        user = self.request.user
        if user is not None:
            user.set_password(confirm_password)
            user.save()
        return super().form_valid(form)


class GymInformationCreateView(LoginRequiredMixin, CreateView):
    model = GymInformation
    form_class = GymInformationCreateForm
    template_name = 'FitHubManageApp/GymInformation/gym_create.html'
    success_url = reverse_lazy('superadmin_gym_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gym_management_tree"] = "menu-open"
        context["gym_information_add"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        messages.success(self.request, "Gym Information added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class GymInformationUpdateView(LoginRequiredMixin, UpdateView):
    model = GymInformation
    form_class = GymInformationCreateForm
    template_name = 'FitHubManageApp/GymInformation/gym_update.html'
    success_url = reverse_lazy('superadmin_gym_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gym_management_tree"] = "menu-open"
        context["gym_list"] = "active"
        return context

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        messages.success(self.request, "Gym Information updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class GymInfoDeleteView(LoginRequiredMixin, DeleteView):
    model = GymInformation
    template_name = 'FitHubManageApp/GymInformation/gym_delete.html'
    success_url = reverse_lazy('superadmin_gym_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gym_management_tree"] = "menu-open"
        context["gym_list"] = "active"
        return context


class GymInformationListView(LoginRequiredMixin, ListView):
    model = GymInformation
    template_name = 'FitHubManageApp/GymInformation/gym_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gym_information'] = GymInformation.objects.all()
        context["gym_information_list"] = "active"
        context["gym_management_tree"] = "menu-open"
        return context

