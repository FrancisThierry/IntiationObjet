from Axle import Axle
from Bike import Bike
from Car import Car
from BetterCar import BetterCar

# clio =  Car() ne fonctionne pas car ne respecte pas le constructeur
zoe = Car("Renault", "Zoe", 2020, "blue",4,5)
zoeAxle = zoe.axle
print( type(zoe.axle.number))
print( type(zoe.axle.length))
print(zoe.start_engine())

vtt = Bike("Giant", "Talon", 2021)

print(vtt.brand)
print(vtt.bike_info())

deloreanAxle = Axle(2.5, 5)
delorean = BetterCar("DeLorean", "DMC-12", 1981, deloreanAxle)
# delorean.set_color("silver")

print(delorean.get_color())

# print(delorean.__color)

# cadillacAxle = Axle(2.0, 4)
cadillac = BetterCar("Cadillac", "Eldorado", 1978, Axle(2.0, 4))
# cadillac.axle = Axle(2.0, 1)


