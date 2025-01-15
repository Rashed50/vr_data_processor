from django.shortcuts import render
from django.http import HttpResponse
from datasource import mqtt_tls_broker


def index_view(request):
    mqtt_tls_broker.startMQTTBroker()
    return HttpResponse("Your are Welcome Here, MQTT Broker Successfully Run")
