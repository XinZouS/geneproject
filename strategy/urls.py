from django.conf.urls import url
from . import views

app_name = 'strategy'

urlpatterns = [
	url(r'^$',views.StrategyList.as_view(),name='all'),
	url(r'^new/$',views.StrategyCreate.as_view(),name='create'),
	url(r'^detail/(?P<slug>[-\w]+/)$',views.StrategyDetail.as_view(),name='detail'),
	url(r'^delete/$',views.StrategyDelete.as_view(),name='delete'),
]

