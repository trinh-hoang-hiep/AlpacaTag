from django.urls import path
from rest_framework import routers

from .views import IndexView
from .views import ProjectView, DatasetView, DataUpload, LabelView, StatsView, SettingView, DictionaryView
from .views import ProjectsView, DataDownload, DataDownloadFile
from .api import ProjectViewSet, LabelList, ProjectStatsAPI, LabelDetail, \
    AnnotationList, AnnotationDetail, DocumentList, RecommendationList, LearningInitiate, OnlineLearning, DocumentDetail, \
    SettingList, ConnectToServer, RecommendationHistoryList, RecommendationHistoryDetail, ActiveLearning


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/projects/<int:project_id>/stats/', ProjectStatsAPI.as_view(), name='stats-api'),
    path('api/projects/<int:project_id>/settings/', SettingList.as_view(), name='settings'),
    path('api/projects/<int:project_id>/history/', RecommendationHistoryList.as_view(), name='histories'),
    path('api/projects/<int:project_id>/history/<int:history_id>', RecommendationHistoryDetail.as_view(), name='history'),
    path('api/projects/<int:project_id>/labels/', LabelList.as_view(), name='labels'),
    path('api/projects/<int:project_id>/labels/<int:label_id>', LabelDetail.as_view(), name='label'),
    path('api/projects/<int:project_id>/docs/', DocumentList.as_view(), name='docs'),
    path('api/projects/<int:project_id>/docs/<int:doc_id>', DocumentDetail.as_view(), name='doc'),
    path('api/projects/<int:project_id>/connectserver/', ConnectToServer.as_view(), name='connect'),
    path('api/projects/<int:project_id>/learninginitiate/', LearningInitiate.as_view(), name='initiate'),
    path('api/projects/<int:project_id>/onlinelearning/', OnlineLearning.as_view(), name='learning'),
    path('api/projects/<int:project_id>/activelearning/', ActiveLearning.as_view(), name='active'),
    path('api/projects/<int:project_id>/docs/<int:doc_id>/annotations/', AnnotationList.as_view(), name='annotations'),
    path('api/projects/<int:project_id>/docs/<int:doc_id>/recommendations/', RecommendationList.as_view(), name='recommendations'),
    path('api/projects/<int:project_id>/docs/<int:doc_id>/annotations/<int:annotation_id>', AnnotationDetail.as_view(), name='ann'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<int:project_id>/download', DataDownload.as_view(), name='download'),
    path('projects/<int:project_id>/download_file', DataDownloadFile.as_view(), name='download_file'),
    path('projects/<int:project_id>/', ProjectView.as_view(), name='annotation'),
    path('projects/<int:project_id>/docs/', DatasetView.as_view(), name='dataset'),
    path('projects/<int:project_id>/docs/create', DataUpload.as_view(), name='upload'),
    path('projects/<int:project_id>/labels/', LabelView.as_view(), name='label-management'),
    path('projects/<int:project_id>/stats/', StatsView.as_view(), name='stats'),
    path('projects/<int:project_id>/setting/', SettingView.as_view(), name='setting'),
    path('projects/<int:project_id>/dictionary/', DictionaryView.as_view(), name='dictionary'),
]
