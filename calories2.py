runner_age = float(input('years'))
runner_weight = float(input('pounds'))
heartrate_minute = float(input('time in minutes'))
time_minutes = float(input('time in minutes'))

runner_calories = ((runner_age * 0.2757) + (runner_weight * 0.03295) + (heartrate_minute * 1.0781) - 75.4991) * time_minutes / 8.368

print(f'Calories: {runner_calories:.2f} calories')
