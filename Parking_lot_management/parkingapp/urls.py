from django.urls import path,include
from . import views

urlpatterns = [
    path('parking_lot/',views.parking_lot_index,name='parking_lot_index'),
    # path('book/<int:site_no>',views.site_position_book, name='site_position_book'),
    # path('check/<int:site_no>',views.admin_position, name='admin_position'),
    # path('order_position/<int:site_no>/<posi_num>',views.order_position,name='order_position'),
    # path('download',views.download_positions,name='download'),
    # path('admins',views.admins,name='download'),
]