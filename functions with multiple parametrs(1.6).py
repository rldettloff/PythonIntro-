def calc_circle_area(circle_diameter):
    pi_val = 3.14159265
	   
    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius * circle_radius
    return circle_area

def calc_pizza_calories(pizza_diameter):
    calories_per_square_inch = 16.7    # Regular crust pepperoni pizza
  
    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
    return total_calories
