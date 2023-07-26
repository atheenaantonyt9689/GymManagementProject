from FitHubManageApp.views import SuperAdminDashBoardView, AdministratorCreateView, AdministratorUpdateView, AdministratorDeleteView, \
    AdministratorListView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView, TrainerListView

from django.urls import path

urlpatterns = [
    path('', SuperAdminDashBoardView.as_view(), name='home'),
    # Admin Section
    path('user/admin/create/', AdministratorCreateView.as_view(), name='fithub_admin_create'),
    path('user/admin/update/<int:pk>', AdministratorUpdateView.as_view(), name='fithub_admin_update'),
    path('user/admin/delete/<int:pk>', AdministratorDeleteView.as_view(), name='fithub_admin_delete'),
    path('user/admin/list/', AdministratorListView.as_view(), name='fithub_admin_list'),

    # Trainer Section
    path('user/trainer/create/', TrainerCreateView.as_view(), name='fithub_trainer_create'),
    path('user/trainer/update/<int:pk>', TrainerUpdateView.as_view(), name='fithub_trainer_update'),
    path('user/trainer/delete/<int:pk>', TrainerDeleteView.as_view(), name='fithub_trainer_delete'),
    path('user/trainer/list/', TrainerListView.as_view(), name='fithub_trainer_list'),



]
