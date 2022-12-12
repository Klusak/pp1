class TV():
    def __init__(self):
        self.is_on=False
        self.channel=1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def set_channel(self,channel):
        self.channel=channel
    def show_status(self):
        if self.is_on==True:
            print(f"TV is on, channel {self.channel} ")
        else:
            print(("TV is off"))

tv1=TV()
tv1.show_status()
tv1.turn_on()
tv1.set_channel(5)
tv1.show_status()
tv1.turn_off()
tv1.show_status()