def bmi(weight, height):
    return weight / (height ** 2)

print(bmi(70, 1.75))


def ft_and_inch_to_meters(feet, inch):
    return feet * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.453592

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / (height ** 2)

print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_meters(5, 7)))