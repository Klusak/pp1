import random
class Thermometer():
    def __init__(self):
        self.is_on=False
        self.temperature=0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def measure(self,temperature):
        if self.is_on==True:
            temperature==self.temperature+temperature
        if temperature>=37.0 and temperature<41.0:
            print(f"Temperature: {float(temperature)}C (fever)")
        elif temperature>=41.0 and temperature<=42.0:
            print(f"Temperature: {float(temperature)}C (CRITICAL TEMPERATURE!)")
        else:
            temperature>34.0 and temperature<37.0
            print(f"Temperature: {float(temperature)}C (you dont have a fever)")   


thermometer1=Thermometer()
thermometer1.turn_on()
thermometer1.measure(random.randrange(34.0,42.1))
thermometer1.turn_off()