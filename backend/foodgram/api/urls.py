from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipes.views import ListTagViewSet, RecipeViewSet, IngredientsViewSet

router = DefaultRouter()

router.register('tags', ListTagViewSet)
router.register(r'tags/?P(<id>\d+)', ListTagViewSet)
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientsViewSet)
router.register('ingredients/?P(<id>\d+)', IngredientsViewSet)


urlpatterns = [
    path('', include('users.urls'), name='users'),
    path('', include(router.urls)),
    # path('tags/', ListTag.as_view(), name='tag')
]