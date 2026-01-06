from django.urls import path
from .controllers import (
    create_user,
    get_users,
    get_user,
    update_user,
    partial_update_user,
    delete_user,
)

urlpatterns = [
    # CREATE
    path('users/create/', create_user),

    # READ
    path('users/', get_users),                 # GET all
    path('users/<int:user_id>/', get_user),    # GET one

    # UPDATE
    path('users/<int:user_id>/update/', update_user),          # PUT
    path('users/<int:user_id>/partial-update/', partial_update_user),  # PATCH

    # DELETE
    path('users/<int:user_id>/delete/', delete_user),
]
