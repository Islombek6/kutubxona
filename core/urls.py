from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),

    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talabalar_details_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('talabalar/<int:talaba_id>/delete-confirm/', talaba_delete_confirm_view),
    path('talabalar/<int:pk>/update/', talaba_update_view),
    path("talaba-qo'shish/", talaba_qoshish_view, name='talaba_qoshish'),

    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('mualliflar/<int:muallif_id>/', mualliflar_details_view),
    path('mualliflar/<int:pk>/delete-confrim/', muallif_delete_confrim_view),
    path('mualliflar/<int:pk>/update/', muallif_update_view),
    path('mualliflar/<int:muallif_id>/delete/', muallif_delete),
    path("muallif-qo'shish/", muallif_qoshish_view, name='muallif_qoshish'),

    path('kitoblar/', kitob_view, name='kitoblar'),
    path("kitob-qo'shish/", kitob_qoshish_view, name='kitob_qoshish'),
    path('kitoblar/<int:pk>/delete-confrim/', kitob_delete_confrim_view),
    path('kitoblar/<int:pk>/update/', kitob_update_view),
    path('kitoblar/<int:kitob_id>/delete/', kitob_delete),
    path('kitoblar/<int:kitob_id>/', kitoblar_details_view),

    path('kutubxonachilar/', kutubxonachi_view, name='kutubxonachilar'),
    path('kutubxonachilar/<int:kutubxonachi_id>/', kutubxonachi_details_view),
    path('kutubxonachilar/<int:pk>/delete-confrim/', kutubxonachi_delete_confirm_view),
    path('kutubxonachilar/<int:kutubxonachi_id>/delete/', kutubxonachi_delete_view, name='kutubxonachi_delete'),
    path('kutubxonachilar/<int:pk>/update/', kutubxonachi_update_view),
    path("kutubxonachi-qo'shish/", kutubxonachi_qoshish_view, name = 'kutubxonachi_qoshish/'),

    path('recordlar/', recordlar_view, name='recordlar'),
    path("record-qo'shish/", record_qoshish_view, name='record_qoshish/'),
    path('recordlar/<int:pk>/update/', record_update_view),
    path('recordlar/<int:pk>/delete-confrim/', record_delete_confrim_view),
    path('recordlar/<int:record_id>/delete/', record_delete),
    path('recordlar/<int:record_id>/', recordlar_details_view),

]
