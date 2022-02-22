# pydevice

Implementa un backend que devuelva información de dispositivos de red
Los dispositivos estarán en un inventario y alcanzables desde la LAN del servidor mediante SSH

Inventario:

Acepta 3 implentaciones: INI, yaml, JSON y BBDD
Contiene información del fabricante, la IP, nombre del dispositivos
Soporta peticiones CRUD 

Información a recuperar:

- Interfaces de capa 3 en todos los fabricantes: Cisco, Palo Alto, Servidor Linux, y F5 -> 
- La informacion se podrá recuperar Por dispositivo o por fabricante, en el segundo caso las peticiones podrían ser concurrentes si hay más de 1 dispositivo de cada fabricante

- Virtual Servers en F5 -> modelar en Pydantic

/manufacturer/
/device/?manufacturer="cisco"

/device/interfaces


Dicha información permanecerá en BBDD durante un tiempo TTL. Si el TTL es 0, dicha información tendrá que ser recuperada del dispositivo mediante SSH

Conexiones SSH

Podemos usar Paramiko o Netmiko

Ejemplos:

Cisco:

ios_xe#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       80.0.0.3        YES NVRAM  up                    up
GigabitEthernet2       10.0.0.1        YES NVRAM  up                    up
GigabitEthernet3       172.16.0.23     YES NVRAM  up                    up
GigabitEthernet4       unassigned      YES NVRAM  administratively down down
Tunnel9361             192.168.0.9     YES NVRAM  up                    down




Palo Alto

admin@FW_INT1(active)> show interface logical

name                id    vsys zone             forwarding               tag    address
------------------- ----- ---- ---------------- ------------------------ ------ ------------------
ethernet1/1         16    1    CONEXION-F5      vr:PRODUCCION            0      192.168.20.2/24
ethernet1/2         17    1    EXTERNA          vr:PRODUCCION            0      192.168.40.1/24
ethernet1/3         18    1    PROXY            vr:PRODUCCION            0      192.168.60.2/24
ethernet1/4         19    1    LAN              vr:PRODUCCION            0      N/A
ethernet1/4.23      260   1    LAN              vr:PRODUCCION            23     192.168.23.1/24
ethernet1/8         23    1    MPLS             vr:PRODUCCION            0      10.0.0.1/24
ethernet1/18        33    1    MPLS             vr:PRODUCCION            0      N/A
ethernet1/23        38    1                     ha                       0      N/A
ethernet1/24        39    1                     ha                       0      192.168.110.1/24
tunnel              4     1                     N/A                      0      N/A
show inter	


F5:

@(F5CPD)(cfg-sync Standalone)(Active)(/Common)(tmos)# list net self recursiv
net self 192.168.30.2 {
    address 192.168.30.2/24
    allow-service {
        default
    }
    traffic-group traffic-group-local-only
    vlan HA
}
net self external_self {
    address 192.168.20.1/24
    allow-service all
    traffic-group traffic-group-local-only
    vlan external
}
net self external_floating {
    address 192.168.20.254/24
    allow-service all
    floating enabled
    inherited-traffic-group true
    traffic-group traffic-group-1
    unit 1
    vlan external
}
net self internal_self {
    address 192.168.10.1/24
    allow-service all
    traffic-group traffic-group-local-only
    vlan internal
}
net self internal_floating {
    address 192.168.10.254/24
    allow-service all
    floating enabled
    inherited-traffic-group true
    traffic-group traffic-group-1
    unit 1
    vlan internal
}
net self VLAN132_self {
    address 192.168.50.1/24
    allow-service all
    traffic-group traffic-group-local-only
    vlan VLAN132
}
net self vlan132_floating {
    address 192.168.50.254/24
    allow-service all
    floating enabled
    inherited-traffic-group true
    traffic-group traffic-group-1
    unit 1
    vlan VLAN132
}
net self vlan133_self {
    address 192.168.60.1/24
    allow-service all
    traffic-group traffic-group-local-only
    vlan VLAN133
}
net self vlan133_floating {
    address 192.168.60.254/24
    allow-service all
    floating enabled
    inherited-traffic-group true
    traffic-group traffic-group-1
    unit 1
    vlan VLAN133
