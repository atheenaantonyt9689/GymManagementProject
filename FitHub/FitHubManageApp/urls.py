from FitHubManageApp.views import SuperAdminDashBoardView, AdministratorCreateView, AdministratorUpdateView, \
    AdministratorDeleteView, \
    AdministratorListView, TrainerCreateView, TrainerUpdateView, TrainerDeleteView, TrainerListView, \
    LogoutView, UserLogin, ChangePasswordView, TrainerDashBoardView, AdminDashBoardView, GymInformationCreateView, \
    GymInformationUpdateView, GymInfoDeleteView, GymInformationListView

from django.urls import path

urlpatterns = [
    path('superadmin/dashboard', SuperAdminDashBoardView.as_view(), name='superadmin_dashboard'),
    # superadmin section - GymCreation
    path('superadmin/gyminfo/create/', GymInformationCreateView.as_view(), name='superadmin_gym_create'),
    path('superadmin/gyminfo/update/<int:pk>', GymInformationUpdateView.as_view(), name='superadmin_gym_update'),
    path('superadmin/gyminfo/delete/<int:pk>', GymInfoDeleteView.as_view(), name='superadmin_gym_delete'),
    path('superadmin/gyminfo/list/', GymInformationListView.as_view(), name='superadmin_gym_list'),

    # Admin Section
    path('user/admin/create/', AdministratorCreateView.as_view(), name='fithub_admin_create'),
    path('user/admin/update/<int:pk>', AdministratorUpdateView.as_view(), name='fithub_admin_update'),
    path('user/admin/delete/<int:pk>', AdministratorDeleteView.as_view(), name='fithub_admin_delete'),
    path('user/admin/list/', AdministratorListView.as_view(), name='fithub_admin_list'),
    path('user/admin/dashboard', AdminDashBoardView.as_view(), name='fithub_admin_dashboard'),

    # Trainer Section
    path('user/trainer/create/', TrainerCreateView.as_view(), name='fithub_trainer_create'),
    path('user/trainer/update/<int:pk>', TrainerUpdateView.as_view(), name='fithub_trainer_update'),
    path('user/trainer/delete/<int:pk>', TrainerDeleteView.as_view(), name='fithub_trainer_delete'),
    path('user/trainer/list/', TrainerListView.as_view(), name='fithub_trainer_list'),
    path('user/trainer/dashboard', TrainerDashBoardView.as_view(), name='fithub_trainer_dashboard'),

    # Login Section
    path('', UserLogin.as_view(), name='fithub_login_view'),
    path('logout', LogoutView.as_view(), name='fithub_logout_view'),
    path('user/admins/change_password/', ChangePasswordView.as_view(), name='fithub_administrators_password_change'),



]
