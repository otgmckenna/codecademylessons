#Defining function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    return (f_temp - 32) * 5/9    #Formula used to convert F to C

#Testing func f_to_c
#f100_in_c = f_to_c(100)
#print(f100_in_c)

#Defining function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    return c_temp * (9/5) + 32    #formula used to convert C to F

#Testing func c_to_f
#c0_in_f = c_to_f(0)
#print(c0_in_f)

#Provided variables and values
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#Defining func get_force
def get_force(mass, acceleration):
    return mass * acceleration

#Testing func get_force
train_force = get_force(train_mass, train_acceleration)         #Essential, cannot be commented out
#print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

#Defining func get_energy
def get_energy(mass, c=3*10**8):    #c is equal to speed of light; 3x10^8
    return mass*c**2

#Testing func get_energy
bomb_energy = get_energy(bomb_mass)         #Essential, cannot be commented out
#print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#Defining func get_work
def get_work(mass, acceleration, distance):
    return get_force(train_mass, train_acceleration) * distance

#Testing func get_work
train_work = get_work(train_mass, train_acceleration, train_distance) #Essential, cannot be commented out
#print(train_work)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")