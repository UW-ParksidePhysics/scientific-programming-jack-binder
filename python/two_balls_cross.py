import vpython as vp

initial_position = vp.vector(-3., 3., 3.)
initial_velocity = vp.vector(1., -1., -1.)
ball = vp.sphere(
    pos=initial_position,
    radius=0.5,
    color=vp.color.red,
    make_trail=True,
    trail_type="points",
    trail_radius=0.5,
    interval=15,
    retain=30
)

initial_position2 = vp.vector(7., 7., 7.)
initial_velocity2 = vp.vector(-3., -3., -3.)
ball2 = vp.sphere(
    pos=initial_position,
    radius=0.5,
    color=vp.color.blue,
    make_trail=True,
    trail_type="points",
    trail_radius=0.5,
    interval=15,
    retain=30
)

animation_time_step = 0.1  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.05
stop_time = 10.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x = initial_position.x + initial_velocity.x * time
    y = initial_position.y + initial_velocity.y * time
    z = initial_position.z + initial_velocity.z * time
    ball.pos = vp.vector(x, y, z)

    x2 = initial_position2.x + initial_velocity2.x * time
    y2 = initial_position2.y + initial_velocity2.y * time
    z2 = initial_position2.z + initial_velocity2.z * time
    ball2.pos = vp.vector(x2, y2, z2)
    time += time_step
