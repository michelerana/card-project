from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^/$', ), #dashboard azienda
    url(r'^add/<id-utente>/$', ), #aggiungi utente
    url(r'^signup/$', ), #iscrizione azienda
]
