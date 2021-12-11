import objects

left_map_one = objects.Map(0, 0)

left_map_wall_one = objects.Wall(left_map_one, 100, 575, 50, 50)
left_map_wall_two = objects.Wall(left_map_one, 100, 100, 250, 50)

right_map_one = objects.Map(600, 0)

right_map_wall_one = objects.Wall(right_map_one, 500, 575, 50, 50)