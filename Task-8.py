# OOPS CONCEPT- Task-8
"""# question-1#   Create a python program called circle with constructor which will take a list an argument
   #question-2# create proper member variables inside the task if required and use them when necessary. for example
   for this task create a class private variable called p1=3.141
  # question-3#  From the given list create two class methods area and perimeter which will belong to calculate area and perimeter"""

# Creating circle class 
class Circle:
    #__ creating private a private variable
    __pi = 3.141

    def __init__(self, radius):
        self.radius = radius
        
# creating function to find the area using the radius

    def area(self):
        area = Circle.__pi * self.radius * self.radius
        return area
    
#creating function to find the perimeter
    def perimeter(self):
        circumference = 2 * Circle.__pi * self.radius
        return circumference

#call the function(method)
list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in list:
    circle_obj = Circle(radius)
    print(f"Radius: {radius}")
    print(f"Area: {circle_obj.area()}")
    print(f"Perimeter: {circle_obj.perimeter()}")
    print("------")

'''##question-4# convert UML diagram into python class and its methos
TVClass - Base class
LedTV class
PlasmaTV class

Part - A
Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume.
Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".

Part - B : LED , Plasma
Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate ,
functionalities like viewin gAngle , Backlight, Display Details , which displays the detailed features of the TV
'''

#Tvclass is a base class 
class Tvclass:
    # it is a constuctor used
    def __init__(self, brand, price, inches, OnOff, volume=50, channel=1):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.OnOff = OnOff
        self.volume = volume
        self.channel = channel

    def increaseVolume(self):
        if self.volume < 100:
            self.volume += 1

    def decreaseVolume(self):
        if self.volume > 0:
            self.volume -= 1

    def changeChannel(self, channel_number):
        if 1 <= channel_number <= 50:
            self.channel = channel_number

    def resetTv(self):
        self.channel = 1
        self.volume = 50

    def showStatus(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

#in this we inherit the Base class (Tvclass)
class LEDTV(Tvclass):
    def __init__(self, brand, price, inches, OnOff, screen_thickness, energy_usage, lifespan, refresh_rate, viewing_angle, backlight):
        super().__init__(brand, price, inches, OnOff)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = viewing_angle
        self.backlight = backlight

    def displayDetails(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, " \
               f"Backlight: {self.backlight}"

# in this we inherit the Base class (Tvclass)
class PlasmaTV(Tvclass):
    def __init__(self, brand, price, inches, OnOff, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches, OnOff)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def displayDetails(self):
        return f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"

# In this we can give the values to display
led_tv = LEDTV("Sony", 1000, 55, "on", "Slim", "Low", "5 years", "120Hz", "178 degrees", "Full Array LED")
plasma_tv = PlasmaTV("LG", 2000, 50, "on", "Thick", "Medium", "6 years", "60Hz")


led_tv.changeChannel(34)
led_tv.increaseVolume()

print(led_tv.showStatus())
print(led_tv.displayDetails())
# in this we can display  all the details

plasma_tv.changeChannel(29)

print(plasma_tv.showStatus())
print(plasma_tv.displayDetails())

              















