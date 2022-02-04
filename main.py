class Element:
    def change_scale(self, t, scale):
        if scale == 'Fahrenheit':
            return ((t - 32) * 5) / 9
        if scale == 'Kelvin':
            return t - 273
    def agg_state(self, t):
        if t < self.hardening:
            return ('Solid state')
        if t >= self.melting and t < self.evaporation:
            return ('Liquid state')
        if t >= self.evaporation:
             return ('Gas State')

class Oxygen(Element):
    hardening = -218
    melting = -218
    evaporation = -182
    scale = 'Celsius'


class Chlorine(Element):
    hardening = -100
    melting = -100
    evaporation = -34
    scale = 'Celsius'


class Iron(Element):
    hardening = 1538
    melting = 1538
    evaporation = 2862
    'Celsius'
