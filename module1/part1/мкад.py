speed = int(input('Введите скорость байкера, км/ч: '))
time = int(input('Введите время движения байкера, ч: '))
length_mkad = 109
s = speed * time
point = s % length_mkad
print(point, '-й км МКАД')
