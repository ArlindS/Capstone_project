from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', PostListView.as_view(), name="academia-home"), --> makes the home view a list view
    path('', views.home, name="academia-home"),
    path('about/', views.about, name="academia-about"),
    path('compSci/', views.compSci, name="academia-compSci"),
    path('compSci/discussion_CS/', PostListView.as_view(), name='discussion_CS'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('compSci/theoretical/', views.theoretical, name="academia-theoretical"),
    path('compSci/theoretical/algorithms', views.algorithms, name="algorithms"),
    path('compSci/theoretical/algorithms/graphs', views.algo_graph, name="algo_graph"),
    path('compSci/theoretical/algorithms/graphs/graph?', views.graph, name="graph"),
    path('compSci/dataSci/', views.dataSci, name="academia-dataSci"),
    path('compSci/compEng/', views.compEng, name="academia-compEng"),
    path('compSci/compEng/', views.compEng, name="academia-compEng"),
]
