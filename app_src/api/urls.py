from django.conf import settings
from django.urls import path

from app_src.api import views

app_name = "api"
urlpatterns = [
    path("users/", view=views.UserList.as_view(), name="user-list"),
    path("users/current/", view=views.UserCurrent.as_view(), name="user-current"),
    path("users/<int:user_id>/", view=views.UserDetail.as_view(), name="user-detail"),
    path("admins/", view=views.AdminList.as_view(), name="admin-list"),
    path("products/", view=views.ProductList.as_view(), name="product-list"),
    path(
        "products/<int:product_id>/",
        view=views.ProductDetail.as_view(),
        name="product-detail",
    ),
    path("managers/", view=views.ManagerList.as_view(), name="manager-list"),
    path(
        "managers/<int:manager_id>/",
        view=views.ManagerDetail.as_view(),
        name="manager-detail",
    ),
    path("agents/", view=views.AgentList.as_view(), name="agent-list"),
    path(
        "agents/<int:agent_id>/", view=views.AgentDetail.as_view(), name="agent-detail"
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path("reset/", view=views.Reset.as_view(), name="reset",),
        path("pull/", view=views.PullAndUpdate.as_view(), name="pull",),
        path("pullandbear/", view=views.PullAndUpdate.as_view(), name="pull",),
    ]
