from models import RGB, CMYK, HSV

def rgb_to_cmyk():
    rgb = RGB()
    rgb.set_values()
    cmyk = rgb.to_cmyk()
    print(cmyk)
    
def cmyk_to_rgb():
    cmyk = CMYK()
    cmyk.set_values()
    rgb = cmyk.to_rgb()
    print(rgb)

def rgb_to_hsv():
    rgb = RGB()
    rgb.set_values()
    hsv = rgb.to_hsv()
    print(hsv)

def hsv_to_rgb():
    hsv = HSV()
    hsv.set_values()
    rgb = hsv.to_rgb()
    print(rgb)

def normalize_rgb():
    rgb = RGB()
    rgb.set_values()
    rgb.normalize()
    print(rgb)

def main():
    print('''
[1] RGB to CMYK
[2] CMYK to RGB
[3] RGB to HSV
[4] HSV to RGB
[5] Normalize RGB
    ''')

    conversion = input('select a conversion: ')

    conversions = {
        '1': rgb_to_cmyk,
        '2': cmyk_to_rgb,
        '3': rgb_to_hsv,
        '4': hsv_to_rgb,
        '5': normalize_rgb
    }

    conversions[conversion]()


if __name__ == "__main__":
    main() 
