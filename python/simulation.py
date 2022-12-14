def position(angle, strength, time):
    strength = 1/strength
    pos = -(strength)*(time**2)+(angle*time)
    return pos

def velocity(angle, strength, time):
    strength = 1/strength
    velo = -(2*strength)*(time)+(angle)
    return velo

def acceleration(strength):
    strength = 1/strength
    accel = -(2*strength)
    return accel

angle = input("What angle do you want to throw the ball at?")
angle = int(angle)
strength = input("How hard do you want to throw the ball?")
strength = int(strength)

time = 0
while True:
    pos = position(angle,strength,time)
    velo = velocity(angle,strength,time)
    accel = acceleration(strength)
    print(f"The ball at {time} seconds is {pos} feet off the ground, moving at {velo} feet per second, and accelerating at {accel} feet per second, per second")
    if pos == 0:
        if time == 0:
            time += 1
        elif time != 0:
            break
    else:
        time += 1