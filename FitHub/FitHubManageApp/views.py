from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, FormView, DetailView

from FitHubManageApp.forms import AdminstratorCreateForm, TrainerCreateForm, LoginForm, ChangePasswordForm, \
    GymInformationCreateForm, TrainerUpdateForm, AdminVideoCreateForm, AdminVideoEditForm, AdminBlogCreateForm, \
    PlanCreateForm, EquipmentCreateForm
from FitHubManageApp.models import GymInformation, GymAdministator, GymTrainer, GymMember, AdminVideoGallery, Blog, \
    Plan, Equipments


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


class AdministratorCreateView(LoginRequiredMixin, FormView):
    form_class = AdminstratorCreateForm
    template_name = 'FitHubManageApp/Admin/admininstrator_create.html'

    def get_success_url(self):
        return reverse('fithub_admin_list', kwargs={'gym_id': self.kwargs['gym_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_management_tree"] = "menu-open"
        context["admin_add"] = "active"
        return context

    def form_valid(self, form):
        print("form is valid")
        print(form.cleaned_data)
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = email
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            user_obj = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
            user_obj.save()
        print("user_obj ", user_obj)
        gym_info = GymInformation.objects.filter(id=self.kwargs['gym_id']).first()
        print("gym_info ", gym_info)
        if gym_info is not None:
            print("gym_info obje", gym_info)
            gym_admin, _ = GymAdministator.objects.get_or_create(user=user_obj, gym_info=gym_info)
            print("gym_admin ", gym_admin)
            if gym_admin is not None:
                GymMember.objects.get_or_create(user=user_obj, gym_info=gym_info, is_admin=True)
            messages.success(self.request, "Administrator added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class TrainerCreateView(LoginRequiredMixin, FormView):
    form_class = TrainerCreateForm
    template_name = 'FitHubManageApp/Trainer/trainer_create.html'

    def get_success_url(self):
        return reverse('fithub_trainer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainer_add"] = "active"
        context["trainer_management_tree"] = "menu-open"
        return context

    def form_valid(self, form):
        print("form is valid")
        print(form.cleaned_data)
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = email
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            user_obj = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
            user_obj.save()
        print("loginned Gym ", self.request.user.gymmember)
        gym_info = GymInformation.objects.filter(id=self.request.user.gymmember.gym_info.id).first()
        print("gym_info ", gym_info)
        if gym_info is not None:
            print("gym_info obje", gym_info)
            gym_trainer, _ = GymTrainer.objects.get_or_create(user=user_obj, gym_info=gym_info)
            print("gym_trainer ", gym_trainer)
            if gym_trainer is not None:
                GymMember.objects.get_or_create(user=user_obj, gym_info=gym_info, is_trainer=True)
            messages.success(self.request, "Trainer added successfully")
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
    model = GymAdministator
    template_name = 'FitHubManageApp/Admin/adminstrator_list.html'

    def get_queryset(self):
        return self.model.objects.filter(gym_info_id=self.kwargs['gym_id']).order_by('user__first_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gym_administrators'] = self.get_queryset()
        print("gym_administrators ", context['gym_administrators'])
        context["admins_list"] = "active"
        context["admin_management_tree"] = "menu-open"
        context['gym_id'] = self.kwargs['gym_id']
        print(context['gym_id'], "gym_id")
        return context


# ToDo need to correct DeleteView
class AdministratorDeleteView(LoginRequiredMixin, DeleteView):
    model = GymAdministator
    template_name = 'FitHubManageApp/Admin/admin_delete.html'

    def get_success_url(self):
        return reverse('fithub_admin_list', kwargs={'gym_id': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["admin_management_tree"] = "menu-open"
        context["admins_list"] = "active"
        return context


# class TrainerCreateView(LoginRequiredMixin, CreateView):
#     model = GymTrainer
#     form_class = TrainerCreateForm
#     template_name = 'FitHubManageApp/Trainer/trainer_create.html'
#     success_url = reverse_lazy('fithub_trainer_list')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["trainer_add"] = "active"
#         context["trainer_management_tree"] = "menu-open"
#         return context
#
#     def form_valid(self, form):
#         form.save()
#         print("form is valid")
#         print(form.cleaned_data)
#         messages.success(self.request, "Trainer added successfully")
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         print("form is invalid", form.errors)
#         return super().form_invalid(form)
#
#
class TrainerUpdateView(LoginRequiredMixin, FormView):
    model = User
    form_class = TrainerUpdateForm
    template_name = 'FitHubManageApp/Trainer/trainer_update.html'
    success_url = reverse_lazy('trainer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainer_management_tree"] = "menu-open"
        context["trainers_list"] = "active"
        return context

    def get_initial(self):
        initial = super().get_initial()
        print("self.kwargs['pk'] ", self.kwargs['pk'])
        trainer_obj = GymTrainer.objects.filter(id=self.kwargs['pk']).first()
        print(trainer_obj, "trainer_obj")
        initial['first_name'] = trainer_obj.user.first_name
        initial['last_name'] = trainer_obj.user.last_name
        initial['email'] = trainer_obj.user.email
        # initial['password'] = trainer_obj.user.password
        # Todo Need to Handle password update
        return initial

    def form_valid(self, form):
        form.save()
        print("form is valid")
        print(form.cleaned_data)
        id = self.kwargs.get('pk')
        # check the email exists for the other user
        email = form.cleaned_data['email']
        user_obj = User.objects.filter(id=id).first()
        if user_obj is not None:
            user_obj.first_name = form.cleaned_data['first_name']
            user_obj.last_name = form.cleaned_data['last_name']
            user_obj.email = form.cleaned_data['email']
            user_obj.save()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = email

        messages.success(self.request, "Trainer updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is invalid", form.errors)
        return super().form_invalid(form)


class TrainerListView(LoginRequiredMixin, ListView):
    model = GymTrainer
    template_name = 'FitHubManageApp/Trainer/trainer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gym_trainer'] = GymTrainer.objects.filter(gym_info_id=self.request.user.gymmember.gym_info.id)
        context["trainers_list"] = "active"
        context["trainer_management_tree"] = "menu-open"
        return context


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    model = GymTrainer
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
            if GymAdministator.objects.filter(user=user).exists():
                return redirect('fithub_admin_dashboard')
            elif GymTrainer.objects.filter(user=user).exists():
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


class AdminVideoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'FitHubManageApp/video_management/admin_video_add.html'
    model = AdminVideoGallery
    form_class = AdminVideoCreateForm
    success_url = reverse_lazy('fithub_admin_video_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["video_add"] = "active"
        context["video_management_tree"] = "menu-open"

        return context

    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)

        messages.success(self.request, 'Admin Video added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.cleaned_data)
        return super().form_invalid(form)


class AdminVideoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'FitHubManageApp/video_management/admin_video_edit.html'
    model = AdminVideoGallery
    form_class = AdminVideoEditForm
    success_url = reverse_lazy('fithub_admin_video_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["video_list"] = "active"
        context["video_management_tree"] = "menu-open"
        return context

    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        messages.success(self.request, 'Admin Video updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        messages.error(self.request, 'url already exists')
        return super().form_invalid(form)


class AdminVideoListView(LoginRequiredMixin, TemplateView):
    template_name = 'FitHubManageApp/video_management/admin_video_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["video_list"] = "active"
        context["video_management_tree"] = "menu-open"
        context["admin_video_list"] = AdminVideoGallery.objects.all()
        return context


class AdminVideoDeleteView(LoginRequiredMixin, DeleteView):
    model = AdminVideoGallery
    template_name = 'FitHubManageApp/video_management/admin_video_delete.html'

    def get_success_url(self):
        return reverse('fithub_admin_video_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["video_list"] = "active"
        context["video_management_tree"] = "menu-open"
        return context


class AdminBlogCreateView(LoginRequiredMixin, FormView):
    template_name = 'FitHubManageApp/Blog/admin_blog_add.html'
    model = Blog
    form_class = AdminBlogCreateForm
    success_url = reverse_lazy('fithub_admin_blog_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_add"] = "active"
        context["blog_management_tree"] = "menu-open"

        return context

    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        titile = form.cleaned_data['title']
        description = form.cleaned_data['description']
        image = form.cleaned_data['image']
        user = self.request.user
        admin_obj = GymAdministator.objects.filter(user=user).first()

        if admin_obj is not None:
            blog_obj = Blog.objects.create(title=titile, description=description, image=image, admin=admin_obj)
            blog_obj.save()
            messages.success(self.request, 'Admin Blog Posted successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        return super().form_invalid(form)


class AdminBlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = AdminBlogCreateForm
    template_name = 'FitHubManageApp/Blog/admin_blog_edit.html'
    success_url = reverse_lazy('fithub_admin_blog_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = "active"
        context["blog_management_tree"] = "menu-open"
        return context

    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        messages.success(self.request, 'Admin Blog updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        return super().form_invalid(form)


class AdminBlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'FitHubManageApp/Blog/admin_blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = "active"
        context["blog_management_tree"] = "menu-open"
        context["admin_blog_list"] = Blog.objects.all()
        return context


class AdminBlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'FitHubManageApp/Blog/admin_blog_delete.html'
    success_url = reverse_lazy('fithub_admin_blog_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = "active"
        context["blog_management_tree"] = "menu-open"
        return context


class AdminBlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'FitHubManageApp/Blog/blog_details.html'
    success_url = reverse_lazy('fithub_admin_blog_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = "active"
        context["blog_management_tree"] = "menu-open"
        return context


class AdminPaymentPlanCreateView(LoginRequiredMixin, CreateView):
    model = Plan
    template_name = 'FitHubManageApp/Payment_Plan/admin_payment_plan_add.html'
    form_class = PlanCreateForm
    success_url = reverse_lazy('fithub_admin_payment_plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_plan_add"] = "active"
        context["payment_management_tree"] = "menu-open"
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['gym_id'] = self.request.user.gymmember.gym_info.id
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['gym_info'] = self.request.user.gymmember.gym_info
        return initial

    # get initial for gym_info


    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Plan added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        return super().form_invalid(form)


class AdminPaymentPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = Plan
    template_name = 'FitHubManageApp/Payment_Plan/admin_payment_plan_edit.html'
    form_class = PlanCreateForm
    success_url = reverse_lazy('fithub_admin_payment_plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_plan_list"] = "active"
        context["payment_management_tree"] = "menu-open"
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['gym_id'] = self.request.user.gymmember.gym_info.id
        return kwargs


    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        messages.success(self.request, 'Plan updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        return super().form_invalid(form)


class AdminPaymentPlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'FitHubManageApp/Payment_Plan/admin__payment_plan_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_plan_list"] = "active"
        context["payment_management_tree"] = "menu-open"
        context["admin_payment_plan_list"] = Plan.objects.all()
        return context


class AdminPaymentPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = Plan
    template_name = 'FitHubManageApp/Payment_Plan/admin_plan_delete.html'
    success_url = reverse_lazy('fithub_admin_payment_plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_plan_list"] = "active"
        context["payment_management_tree"] = "menu-open"
        return context


class AdminEquipmentCreateView(LoginRequiredMixin, CreateView):
    model = Equipments
    template_name = 'FitHubManageApp/Gym_Equipment/gym_equipment_add.html'
    form_class = EquipmentCreateForm
    success_url = reverse_lazy('fithub_admin_equipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment_add"] = "active"
        context["equipment_management_tree"] = "menu-open"
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['gym_id'] = self.request.user.gymmember.gym_info.id
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['gym_info'] = self.request.user.gymmember.gym_info
        return initial

    # get initial for gym_info


    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Gym Equipement added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        return super().form_invalid(form)


class AdminEquipmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipments
    form_class = EquipmentCreateForm
    template_name = 'FitHubManageApp/Gym_Equipment/gym_equipment_edit.html'
    success_url = reverse_lazy('fithub_admin_equipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment_list"] = "active"
        context["equipment_management_tree"] = "menu-open"
        return context
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['gym_id'] = self.request.user.gymmember.gym_info.id
        return kwargs

    def form_valid(self, form):
        print("cleaned dataaa ", form.cleaned_data)
        messages.success(self.request, 'Gym Equipment updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid   ', form.errors)
        return super().form_invalid(form)


class AdminEquipmentListView(LoginRequiredMixin, ListView):
    model = Equipments
    template_name = 'FitHubManageApp/Gym_Equipment/gym_equipment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment_list"] = "active"
        context["equipment_management_tree"] = "menu-open"
        context["admin_equipment_list"] = Equipments.objects.all()
        return context


class AdminEquipmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipments
    template_name = 'FitHubManageApp/Gym_Equipment/gym_equipement_delete.html'
    success_url = reverse_lazy('fithub_admin_equipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment_list"] = "active"
        context["equipment_management_tree"] = "menu-open"
        return context


class AdminEquipmentDetailView(LoginRequiredMixin, DetailView):
    model = Equipments
    template_name = 'FitHubManageApp/Gym_Equipment/equipment_detail_view.html'
    success_url = reverse_lazy('fithub_admin_equipment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment_list"] = "active"
        context["equipment_management_tree"] = "menu-open"
        return context