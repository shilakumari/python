# dependency Injection
class Flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self,engine):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")

class BoingEngine:
    def start(self):
        print("Start BoingEngine engine")

ae=AirbusEngine()
f=Flight(ae)
f.startEngine(ae)

be=BoingEngine()
f1=Flight(be)
f1.startEngine(be)