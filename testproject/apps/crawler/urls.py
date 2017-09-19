from django.conf.urls import url

from api import PostFile, GetFileInfo, GetGeneralIngo


urlpatterns = [
    url(r'^api/v1/postfile/$', PostFile.as_view(),
        name='postfile'),
    url(r'^api/v1/generalinfo/$', GetGeneralIngo.as_view(),
        name='general-info'),
    url(r'^api/v1/postfile-info/(?P<pk>\d+)$', GetFileInfo.as_view(),
        name='file-info'),
]
