from django.urls import path
from .views import HomePageView, NosotrosView, success, cancel, SaleInvoicePdfView
from productos import views


urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
    # path("disfraces/", views.products, name="products")
    path("disfraces/", views.products, name="products"),
    path("test", views.test, name="test"),
    path("comprobante/pdf/<int:pk>/", SaleInvoicePdfView.as_view(), name="comprobante"),
    path('<int:inventario_id>/', views.inventario_detail, name='inventario_detail'),
    path('disfraces/<int:inventario_id>/add_comment/', views.add_comment, name='add_comment'),
    path("disfraces/<int:inventario_id>/checkout/", views.checkout, name="checkout"),
    
]