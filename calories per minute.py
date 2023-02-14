
age_years = float(input())
weight_pounds = float(input())
heartrate_minute = float(input())
time_minutes = float(input())

calories = ((age_years * 0.2757) + (weight_pounds * 0.03295) + (heartrate_minute * 1.0781) - 75.4991) * time_minutes / 8.368

print(f'Calories: {calories:.2f} calories')

