#-----------
#bibliotecas
#-----------
import esp
esp.osdebug(None)
#essa classe garante que toda memoria em desuso vai ser liberada
import gc
gc.collect() 
import network
import time
from util import open_json, web_register_uix

#-------------------
#Conectar com o wifi
#-------------------

#Coleta das de dados variaveis
survey_data = open_json()

ssid = survey_data['ssid']
password = survey_data['pwd']

#sistema que vai conectar a EPS a wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
time.sleep(5)

#Caso de tudo certo vai executar essa fun鑾借尗o
if station.isconnected() == True:
    print('Conectado com Sucesso')
    print(station.ifconfig())
    
#Se der errado ela vai gerar uma rede pr璐竝ria, nessa rede vai ser possivel cadastrar uma nova rede
else:
    ap = network.WLAN(network.AP_IF)     
    ap.active(True)                      
    ap.config(essid='ESP32-IoT-BlueShift',password=b"Be@Loved", channel=11, authmode=network.AUTH_WPA_WPA2_PSK)
    print('Falha ao se conectar, acesse a Rede IP e reconfigure a conexão')
    ap.ifconfig(('192.168.15.5', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    print('192.168.15.5')
    web_register_uix()


