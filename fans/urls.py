from django.urls import path
from .views import FansView, FansUploadView, FansDownloadView

urlpatterns = [
    path('', FansView.as_view(), name='fans'),
    path('upload/', FansUploadView.as_view(), name='upload-csv'),
    path('download/', FansDownloadView.as_view(), name='download-csv'),
]