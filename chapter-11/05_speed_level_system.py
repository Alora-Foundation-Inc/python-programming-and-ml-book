import turtle, time

screen = turtle.Screen(); screen.setup(400,300); screen.tracer(0)

score = 0
level = 1
foods_eaten = 0
base_delay = 0.14
min_delay = 0.06

def calculate_speed():
    # faster as level increases
    return max(min_delay, base_delay - (level-1)*0.02)

def eat():
    global score, foods_eaten, level
    score += 10; foods_eaten += 1
    if foods_eaten % 5 == 0:
        level += 1
        print("Level up! Now level", level)

for _ in range(12):
    eat()
    time.sleep(calculate_speed())
