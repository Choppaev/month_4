from django.urls import path
from . import views

urlpatterns = [
    path('tvshow/', views.TvshowView.as_view(), name='tvshow'),
    path('tvshow/<int:id>', views.TvshowDetail.as_view(), name='tvshow_detail'),
    path('add-films/', views.CreateTvshowView.as_view(), name='add_film'),
    path('films_detail/<int:id>/delete/', views.DeleteTvshowView.as_view(), name='films_delete'),
    path('films_detail/<int:id>/update/', views.UpdateTvshowView.as_view(), name='films_update'),
    path('search/', views.Search.as_view(), name='search'),
    path('reviews/', views.CreateFilmView.as_view(), name='reviews'),
]
