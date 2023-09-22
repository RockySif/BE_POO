class Etat:
    def __init__(self):
        pass

    def commande(self, ordre_mission:'mission'):
        pass


class Mission:
    def __init__(self, lieu, date, ordre):
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


