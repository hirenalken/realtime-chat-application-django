from channel_app.views import UserLoginView, UserRegistrationView, UsersDetail, UserMessageView, UserMessageListView, \
     RoomDetailView, UserListView
from django.conf.urls import url

urlpatterns = [



    url(r'^login/$', UserLoginView.as_view()),
    # url(r'^influencer/(?P<instagram_users_id>[0-9]+)/pricing/$', views.UserPriceDetail.as_view()),
    url(r'^users/$', UserRegistrationView.as_view()),
    url(r'^users/list/$', UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UsersDetail.as_view()),
    url(r'^users/(?P<from_user_id>[0-9]+)/message/(?P<to_user_id>[0-9]+)/$',
        UserMessageView.as_view()),
    url(r'^users/(?P<user_id>[0-9]+)/message/$',
        UserMessageListView.as_view()),

    url(r'^room/$', RoomDetailView.as_view()),
    url(r'^room/(?P<pk>[0-9]+)/$', RoomDetailView.as_view()),
]