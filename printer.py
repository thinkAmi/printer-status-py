
from pysnmp.hlapi import *
import config

class Tank(object):
    OID_PREFIX = '1.3.6.1.2.1.43.'
    OID_MARKER_SUPPLIES_DESCRIPTION = "{prefix}11.1.1.6.1.".format(prefix=OID_PREFIX)
    OID_MARKER_SUPPLIES_LEVEL = "{prefix}11.1.1.9.1.".format(prefix=OID_PREFIX)

    def __init__(self, number):
        self.number = number
        
    def sync(self):
        # 'OctetString'で取得できるので、使用目的に応じて型を変換しておく
        self.name = str(recieve_varbind(self.OID_MARKER_SUPPLIES_DESCRIPTION, self.number))
        self.rest_volume = int(recieve_varbind(self.OID_MARKER_SUPPLIES_LEVEL, self.number))
        self.color = self.get_color()
        
        return self

    def get_color(self):
        if "Black" in self.name:
            return "black"
        elif "Magenta" in self.name:
            return "red"
        elif "Yellow" in self.name:
            return "yellow"
        elif "Cyan" in self.name:
            return "blue"
        else:
            return "green" 
        
    
class PX105(object):
    OID_PREFIX = '1.3.6.1.2.1.43.'
    OID_MARKER_PROCESS_COLORANTS = "{prefix}10.2.1.6.1.".format(prefix=OID_PREFIX)
    
    def __init__(self):
        tank_count = recieve_varbind(self.OID_MARKER_PROCESS_COLORANTS)

        self.tanks = []
        for i in range(1, tank_count + 1):
            self.tanks.append(Tank(i).sync())


def recieve_varbind(mib_id, tail=1):
    g = getCmd(SnmpEngine(),
        CommunityData(config.COMMUNITY, mpModel=0),
        UdpTransportTarget((config.PRINTER_HOST_IPV4, 161)),
        ContextData(),
        # http://python.civic-apps.com/vars/
        ObjectType(ObjectIdentity("{mib_id}{tail}".format(**vars()))))
        
    errIndication, errorStatus, errorIndex, varBinds = next(g)
    
    # 'OctetString' objectが取得できる
    return varBinds[0][1]