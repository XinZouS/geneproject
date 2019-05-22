from django.conf.urls import url
from . import views

app_name = 'strategy'

urlpatterns = [
	url(r'^$',views.StrategyList.as_view(),name='all'),
	url(r'^new/$',views.StrategyCreate.as_view(),name='create'),
	url(r'^verify/$',views.StrategyVerify.as_view(),name='verify'),
	url(r'^by/(?P<username>[-\w]+)/$',views.StrategyListByUser.as_view(),name='by_user'),
	url(r'^detail/(?P<pk>\d+)/(?P<slug>[-\w]+)/$',views.StrategyDetail.as_view(),name='detail'),
	url(r'^delete/(?P<pk>\d+)/$',views.StrategyDelete.as_view(),name='delete'),
]

