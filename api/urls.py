from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comment_view_set'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/group/', GroupViewSet.as_view()),
    path('v1/follow/', FollowViewSet.as_view()),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
