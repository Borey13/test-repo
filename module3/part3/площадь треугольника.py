def area_triangle(a, b, c):
    half_p = (a + b + c) / 2
    area = round((half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5, 1)
    return area
