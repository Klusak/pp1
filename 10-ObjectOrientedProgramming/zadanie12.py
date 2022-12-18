class TV():
    def __init__(self):
        self.is_on=False
        self.channel=1
        self.list=[self.channel]
        self.change=1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def set_channel(self,channel):
        self.channel=channel
    def show_status(self):
        if self.is_on==True:
            print(f"TV is on, channel: {self.channel} ({self.list[self.channel]})")
        else:
            print(("TV is off"))
    def channels_list(self,list):
        self.list=list
    def show_channels(self):
        print(self.list)
    def change_channel(self,number):
        self.change=number

tv1=TV()
tv1.show_status()
tv1.turn_on()
tv1.set_channel(4)
tv1.channels_list(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
tv1.set_channel(4)
tv1.change_channel(4)
tv1.show_status()
tv1.turn_off()
tv1.show_status()