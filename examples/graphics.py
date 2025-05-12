x_vals = [0-10, 10, 10, 0-10, 0-10, 10, 10, 0-10]
y_vals = [0-10, 0-10, 10, 10, 0-10, 0-10, 10, 10]
z_vals = [0-10, 0-10, 0-10, 0-10, 10, 10, 10, 10]

edges = [1, 2, 2, 3, 3, 4, 4, 1, 5, 6, 6, 7, 7, 8, 8, 5, 1, 5, 2, 6, 3, 7, 4, 8]

FOCAL_LENGTH = 100

while 1 == 1:
    clear_screen()

    index = 1
    while index <= 24:
        x1 = x_vals[edges[index]] * FOCAL_LENGTH
        y1 = y_vals[edges[index]] * FOCAL_LENGTH
        z1 = z_vals[edges[index]] + FOCAL_LENGTH

        x2 = x_vals[edges[index + 1]] * FOCAL_LENGTH
        y2 = y_vals[edges[index + 1]] * FOCAL_LENGTH
        z2 = z_vals[edges[index + 1]] + FOCAL_LENGTH

        x1 = x1 / z1
        y1 = y1 / z1
        x2 = x2 / z2
        y2 = y2 / z2

        if z1 < 100:
            draw_line(x1, y1, x2, y2, GRAY)
        if z1 > 100:
            draw_line(x1, y1, x2, y2, DARKGRAY)

        index = index + 2
    
    # Rotate the cube by `n` radians around y-axis
    index = 1
    while index <= 8:
        x_vals[index] = x_vals[index] * cos(45) + z_vals[index] * sin(45)
        z_vals[index] = z_vals[index] * cos(45) - x_vals[index] * sin(45)


        index = index + 1