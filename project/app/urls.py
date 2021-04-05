from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", views.UserAPI, 'user')
router.register(r"work", views.WorkAPI, 'work')
router.register(r"bug", views.BugAPI, 'bug')
router.register(r"unf-work", views.UnfinishedWorkAPI, 'unf-work')
router.register(r"unf-bug", views.UnresolvedBugAPI, 'unf-bug')

router.register(r"nested-work", views.WorkNestedAPI, 'nested-work')
router.register(r"nested-bug", views.BugNestedAPI, 'nested-bug')

urlpatterns = [
    path('api/', include(router.urls)),
    path('test', views.test, name='test'),
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('', views.homeView),
    path('logout/', views.logoutView, name='logout')

]