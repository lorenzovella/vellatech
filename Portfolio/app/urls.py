from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("carrinho", api.carrinhoViewSet)
router.register("opcionais", api.opcionaisViewSet)
router.register("cardapio", api.cardapioViewSet)
router.register("itemDoCarrinho", api.itemDoCarrinhoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("app/carrinho/", views.carrinhoListView.as_view(), name="app_carrinho_list"),
    path("app/carrinho/create/", views.carrinhoCreateView.as_view(), name="app_carrinho_create"),
    path("app/carrinho/detail/<int:pk>/", views.carrinhoDetailView.as_view(), name="app_carrinho_detail"),
    path("app/carrinho/update/<int:pk>/", views.carrinhoUpdateView.as_view(), name="app_carrinho_update"),
    path("app/opcionais/", views.opcionaisListView.as_view(), name="app_opcionais_list"),
    path("app/opcionais/create/", views.opcionaisCreateView.as_view(), name="app_opcionais_create"),
    path("app/opcionais/detail/<int:pk>/", views.opcionaisDetailView.as_view(), name="app_opcionais_detail"),
    path("app/opcionais/update/<int:pk>/", views.opcionaisUpdateView.as_view(), name="app_opcionais_update"),
    path("app/cardapio/", views.cardapioListView.as_view(), name="app_cardapio_list"),
    path("app/cardapio/create/", views.cardapioCreateView.as_view(), name="app_cardapio_create"),
    path("app/cardapio/detail/<int:pk>/", views.cardapioDetailView.as_view(), name="app_cardapio_detail"),
    path("app/cardapio/update/<int:pk>/", views.cardapioUpdateView.as_view(), name="app_cardapio_update"),
    path("app/itemDoCarrinho/", views.itemDoCarrinhoListView.as_view(), name="app_itemDoCarrinho_list"),
    path("app/itemDoCarrinho/create/", views.itemDoCarrinhoCreateView.as_view(), name="app_itemDoCarrinho_create"),
    path("app/itemDoCarrinho/detail/<int:pk>/", views.itemDoCarrinhoDetailView.as_view(), name="app_itemDoCarrinho_detail"),
    path("app/itemDoCarrinho/update/<int:pk>/", views.itemDoCarrinhoUpdateView.as_view(), name="app_itemDoCarrinho_update"),
    path("app/adicionarAoCarrinho/<int:pk>/", views.adicionarAoCarrinho, name="adicionar_ao_carrinho"),
)
