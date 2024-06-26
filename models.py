class RGB():
    def __init__(self, R=0, G=0, B=0):
        self._red = R
        self._green = G
        self._blue = B

    def set_values(self):
        self._red = int(input('R: '))
        while self._red < 0 or self._red > 255:
            print("The value must be between 0 and 255")
            self._red = int(input('R: '))

        self._green = int(input('G: '))
        while self._green < 0 or self._blue > 255:
            print("The value must be between 0 and 255")
            self._green = int(input('G: '))

        self._blue = int(input('B: '))
        while self._blue < 0 or self._blue > 255:
            print("The value must be between 0 and 255")
            self._blue = int(input('B: '))
    
    def __str__(self):
        return f'RGB: {round(self._red)}, {round(self._green)}, {round(self._blue)}'

    def to_cmyk(self):
        r1 = self._red / 255
        g1 = self._green / 255
        b1 = self._blue / 255
        k = 1 - max(r1, g1, b1)
        if (k == 1):
            c = m = y = 0
        else: 
            c = (1 - r1 - k) / (1 - k)
            m = (1 - g1 - k) / (1 - k)
            y = (1 - b1 - k) / (1 - k)
        cmyk = CMYK(c, m, y, k)
        return cmyk

    def to_hsv(self):
        r1 = self._red / 255
        g1 = self._green / 255
        b1 = self._blue / 255
        cmax = max(r1, g1, b1)
        cmin = min(r1, g1, b1)
        delta = cmax - cmin
        h = 0
        if (delta == 0):
            h = 0
        elif (cmax == r1):
            h = 60 * (((g1 - b1) / delta) % 6)
        elif (cmax == g1):
            h = 60 * (((b1 - r1) / delta) + 2)
        elif (cmax == b1):
            h = 60 * (((r1 - g1) / delta) + 4)

        s = 0
        if (cmax != 0):
            s = delta / cmax * 100

        v = cmax * 100
        hsv = HSV(h, s, v)
        return hsv

    def normalize(self):
        total = (self._red + self._green + self._blue)

        self._red = (self._red / total) * 255
        self._green = (self._green / total) * 255
        self._blue = (self._blue / total) * 255

    def to_grayscale(self):
        avg = (self._red + self._green + self._blue) / 3

        self._red = avg
        self._green = avg
        self._blue = avg

class CMYK():
    def __init__(self, C=0, M=0, Y=0, K=0):
        self._cian = C
        self._magenta = M
        self._yellow = Y
        self._key = K

    def set_values(self):
        self._cian = float(input('C: '))
        while self._cian < 0 or self._cian > 100:
            print("The value must be between 0 and 100")
            self._cian = float(input('C: '))
        
        self._magenta = float(input('M: '))
        while self._magenta < 0 or self._magenta > 100:
            print("The value must be between 0 and 100")
            self._magenta = float(input('M: '))

        self._yellow = float(input('Y: '))
        while self._yellow < 0 or self._yellow > 100:
            print("The value must be between 0 and 100")
            self._yellow = float(input('Y: '))

        self._key = float(input('K: '))
        while self._key < 0 or self._key > 100:
            print("The value must be between 0 and 100")
            self._key = float(input('K: '))

    def __str__(self):
        return f'CMYK: {round(self._cian * 100)}%, {round(self._magenta * 100)}%, {round(self._yellow * 100)}%, {round(self._key * 100)}%'

    def to_rgb(self):
        c = self._cian / 100
        m = self._magenta / 100
        y = self._yellow / 100
        k = self._key / 100
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)
        rgb = RGB(r, g, b)
        return rgb

class HSV():
    def __init__(self, H=0, S=0, V=0):
        self._hue = H
        self._saturation = S
        self._value = V

    def set_values(self):
        self._hue = float(input('H: '))
        while self._hue < 0 or self._hue > 359:
            print("The value must be between 0 and 359")
            self._hue = float(input('H: '))

        self._saturation = float(input('S: '))
        while self._saturation < 0 or self._saturation > 100:
            print("The value must be between 0 and 100")
            self._saturation = float(input('S: '))

        self._value = float(input('V: '))
        while self._value < 0 or self.value > 100:
            print("The value must be between 0 and 100")
            self._value = float(input('V: '))


    def __str__(self):
        return f'HSV: {round(self._hue)}°, {round(self._saturation)}%, {round(self._value)}%'

    def to_rgb(self):
        c = (self._value / 100) * (self._saturation / 100)
        x = c * (1 - abs((self._hue / 60) % 2 - 1))
        m = (self._value / 100) - c

        r1 = g1 = b1 = 0

        if (self._hue >= 0 and self._hue < 60):
            r1 = c
            g1 = x
            b1 = 0
        elif (self._hue < 120):
            r1 = x
            g1 = c
            b1 = 0
        elif (self._hue < 180):
            r1 = 0
            g1 = c
            b1 = x
        elif (self._hue < 240):
            r1 = 0
            g1 = x
            b1 = c
        elif (self._hue < 300):
            r1 = x
            g1 = 0
            b1 = c
        elif (self._hue < 360):
            r1 = c
            g1 = 0
            b1 = x
        
        rgb = RGB((r1 + m) * 255, (g1 + m) * 255, (b1 + m) * 255)
        return rgb
