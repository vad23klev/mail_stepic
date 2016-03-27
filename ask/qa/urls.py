from qa.views import test
from django.conf.urls import url, patterns

urlpatterns = patterns('qa.views',
        url(r'^(?P<pk>\d+)/',test,name='test')
        )
