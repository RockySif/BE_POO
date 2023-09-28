from datetime import datetime
import random
import pint
import icontract
from math import sqrt
ureg = pint.UnitRegistry()


class Etat:
    def __init__(self):
        pass

    @icontract.require(lambda date: date >= datetime.today().date())
    def commande(self, date:datetime.date, zone:'Zone'):
        self.date = date
        self.zone = zone



class Mission:  #T

    def __init__(self, date:datetime.date, orderId:int, zones:list={}, chrono:pint.Quantity = 0 * ureg.second):
        self.order = orderId
        self.zones = zones
        self.date = date
        self.chrono = chrono
        self.crm = {}
        for zone in self.zones:
            self.crm[zone.idZone] = {'status': 'In delivery', 'delivery_time': None}

    def newMission(self, date:datetime.date, orderId:int, zones:list=[]):
        m=Mission(date, orderId, zones)
        Operateur.receiveMission(m)




    @icontract.require(lambda dt: dt >= 0)
    @icontract.snapshot(lambda self: self.chrono, name='chrono')
    @icontract.ensure(lambda OLD, self, dt: OLD.chrono + dt == self.chrono)
    def update(self, zone:'Zone', etat:bool, dt:pint.Quantity = 0*ureg.second):
        self.chrono += dt
        if etat == True:
            self.crm[zone.idZone] = {'status': 'Delivered', 'delivery_time': self.chrono}
        else:
            self.crm[zone.idZone] = {'status': 'Not delivered', 'delivery_time': self.chrono}
        IODeliv.receiveCRM(CRM, state)


    def crmZone(self, zone:'Zone'):
        return self.crm[zone.idZone]



class IODeliv:
    def __init__(self):
        self.state_orders = []
        self.registered_operators = []
        self.active_missions = []

    def receive_state_order(self, order):
        pass

    def plan_delivery_missions(self):
        pass

    def track_delivery_missions(self):
        pass

    def register_operator(self, operator):
        pass

    def manage_operators(self):
        pass

    def receive_operator_info(self, info):
        pass

    def assign_missions_to_drones(self):
        pass

    def receive_mission_report(self, report):
        pass

class Drone:
    def __init__(self, name:str):
        self.name = name
        self.payload_capacity = 0
        self.autonomy = 0

    def send_status_report(self, status):
        pass

class Operateur:
    def __init__(self, name:str, flotte:list=[]):
        self.name = name
        self.flotte = flotte

    def add_drone(self, drone:Drone):
        self.flotte.append(drone)




class Zone: #T

    @icontract.require(lambda pop: pop > 0)
    def __init__(self, pop:int, idZone:int, x:pint.Quantity = 0 * ureg.meter, y:pint.Quantity = 0 * ureg.meter, z:pint.Quantity = 0 * ureg.meter):
        self.idZone = idZone
        self.pop = pop
        self.x = x
        self.y = y
        self.z = z

    @icontract.require(lambda d: d >= 0)
    def distance(self, zone1):
        d = sqrt((self.x - zone1.x)**2 + (self.y - zone1.y)**2 + (self.z - zone1.z)**2)
        return d

# Confirme la reception des pilules par la population de la zone : il y a 95% de chance que la population récupère les pilules
    def receive(self):
        received = random.random()
        if received < 0.95:
            return True


