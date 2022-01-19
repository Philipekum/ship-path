class Ship():

    def __init__(self, displacement, max_speed, min_speed):
        self.displacement = displacement
        self.max_speed = max_speed
        self.min_speed = min_speed

    def fuel_consumption(self):
        pass

evergreen = Ship(200000, 23, 7)

# f1(t, w, n(v), Pcurr, Pwave, Pwind) = 0

# v - заданная скорость на тихой воде
# n(v) - зависимость частоты вращения винта от скорости

#P*  = P*(t, широта, долгота)

# w - фактическая скорость

# v(t) - заданная линейная скорость судна вдоль определенного курсом направления соответственно в момент времени t
