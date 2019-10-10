from visual import *
celestial1_mass = 1 #kg
celestial2_mass = 1 #kg
celestial3_mass = 0.5 #kg

constant = 100 #m^3 / kg s^2
R =1
r1 = 6371 #Radius of Celestial Object 1 in km
r2 = 3389.5 #Radius of Celestial Object 2 in km
r3 = 6051.8 #Radius of Celestial Object 3 in km
t = 0 #arbitrary start time for simulation
dt = 0.00001 #step for change in time

momentum1 = celestial1_mass*vector(0,2,0)
momentum3 = celestial3_mass*vector(0,3,0)
momentum2 = -momentum1 - momentum3


sphere1 = sphere(pos=vector(-5,0,0), radius=R, color=color.blue, make_trail=True)
sphere2 = sphere(pos=vector(5,0,0), radius = R, color=color.red, make_trail=True)
sphere3 = sphere(pos=vector(25,0,0), radius = R, color = color.green, make_trail=True)


while t <= 10000:
    t = t + dt
    rate(1000000)

    r12 = sphere2.pos - sphere1.pos
    r21 = -r12
    
    r13 = sphere3.pos - sphere1.pos
    r31 = -r13
    
    r23 = sphere3.pos - sphere1.pos
    r32 = -r23
    
    
    force12 = -constant*celestial1_mass*celestial2_mass*norm(r12)/(mag(r12)**2)
    force21 = -force12
    
    force13 = -constant*celestial1_mass*celestial3_mass*norm(r13)/(mag(r13)**2)
    force31 = -force13
    
    force23 = -constant*celestial2_mass*celestial3_mass*norm(r23)/(mag(r23)**2)
    force32 = -force23
    
    
    sphere1.pos = sphere1.pos + momentum1*dt/celestial1_mass
    sphere2.pos = sphere2.pos + momentum2*dt/celestial2_mass
    sphere3.pos = sphere3.pos + momentum3*dt/celestial3_mass
    
    momentum1 = momentum1 + (force21 + force31)*dt
    momentum2 = momentum2 + (force12 + force32)*dt
    momentum3 = momentum3 + (force13 + force23)*dt
    
    if sphere1.pos == sphere2.pos:
        break
    if sphere1.pos == sphere3.pos:
        break
    if sphere2.pos == sphere3.pos:
        break
    