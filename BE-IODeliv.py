from datetime import datetime
import time
import pint
import icontract
ureg = pint.UnitRegistry()


class Etat:
    def __init__(self):
        pass

    @icontract.require(lambda date: date > datetime.today().date())
    def commande(self, date:datetime.date, zone:'Zone'):
        self.date = date
        self.zone = zone


class Mission:  #T

    def __init__(self, lieu, date:datetime.date, ordre):
        self.ordre = ordre
        self.lieu = lieu
        self.date = date


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

class CRM: #T
    def __init__(self, mission:Mission, zones:dict = {}):
        self.mission = mission
        self.zones = zones

    def add_zone(self, zone):
        self.zones[zone] = time.time()

class Zone: #T

    @icontract.require(lambda pop: pop > 0)
    def __init__(self, pop:int, idZone):
        self.idZone = idZone
        self.pop = pop
