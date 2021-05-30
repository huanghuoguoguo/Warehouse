from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:obj>', views.add),
    path('delete/<str:obj>/<int:_id>', views.delete),
    path('modify/<str:obj>/<int:_id>', views.modify),
    path('deleteStorekeeper/<int:wid>/<int:sid>', views.deleteStoW),
    path('addStorekeeper/<int:wh_id>',views.addStorekeeper)
]
