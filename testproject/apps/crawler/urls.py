from django.conf.urls import url

from api import PostFile, GetFileInfo, GetGeneralIngo


urlpatterns = [
    url(r'^postfile/$', PostFile.as_view(),
        name='postfile'),
    url(r'^generalinfo/$', GetGeneralIngo.as_view(),
        name='general-info'),
    url(r'^postfile-info/(?P<pk>\d+)$', GetFileInfo.as_view(),
        name='file-info'),
]
