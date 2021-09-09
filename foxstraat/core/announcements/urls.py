from django.urls import path
from foxstraat.core.announcements.views import (
    create_announcement,
)

app_name = "announcements"

urlpatterns = [
    path("create/", create_announcement, name="create-announcement"),
]
