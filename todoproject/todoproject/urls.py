from django.contrib import admin
from django.urls import path
from todoapp.views import todoappView, addTodoView, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todoappView),
    path('Добавить новое желание/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),

]
