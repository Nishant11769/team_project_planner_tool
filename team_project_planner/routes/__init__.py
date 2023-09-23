from django.urls import include,path

urlpatterns = [
    path('users/', include('team_project_planner.routes.User')),
    path('teams/', include('team_project_planner.routes.Team')),
    path('boards/', include('team_project_planner.routes.Board'))
]