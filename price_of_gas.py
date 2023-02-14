def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_per_gallon / dollars_per_gallon) * miles_driven
    # Define your function here.

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon= float(input())
print(f'{driving_cost(10, miles_per_gallon, dollars_per_gallon):.2f}')
print(f'{driving_cost(50, miles_per_gallon, dollars_per_gallon):.2f}')
print(f'{driving_cost(400, miles_per_gallon, dollars_per_gallon):.2f}')

