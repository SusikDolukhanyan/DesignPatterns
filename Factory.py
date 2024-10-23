from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Deliver by land in a box."


class Ship(Transport):
    def deliver(self):
        return "Deliver by sea in a container."

class TransportFactory:
    @staticmethod
    def get_transport(transport_type):
        if transport_type == 'truck':
            return Truck()
        elif transport_type == 'ship':
            return Ship()
        else:
            raise ValueError("Unknown transport type")


def logistics_app(transport_type):
    transport = TransportFactory.get_transport(transport_type)
    print(transport.deliver())


logistics_app('truck')  
logistics_app('ship')   