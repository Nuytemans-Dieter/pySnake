def add_vectors_2D(vector1, vector2):
    x = vector1[0] + vector2[0]
    y = vector1[1] + vector2[1]
    return (x, y)


def distance_squared(location1, location2):
    diff_x = location1[0] - location2[0]
    diff_y = location1[1] - location2[1]
    return diff_x * diff_x + diff_y * diff_y