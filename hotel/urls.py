
from django.urls import path
from .views import RoomListView, ReservationList , ReservationView, RoomDetailView
app_name = 'hotel'

urlpatterns= [
    path('room_list/', RoomListView, name='RoomList'),
    path('reservation_list/', ReservationList.as_view(), name='ReservationList'),
    path('reserve/', ReservationView.as_view(), name= 'ReservationView'),
    path('room/<category>', RoomDetailView.as_view(), name= 'RoomDetailView')
]