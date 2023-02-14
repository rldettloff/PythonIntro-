user_age_years = int(input('Enter your age in years:\n'))

user_age_minutes = user_age_years  * 525600

user_age_seconds = user_age_years * 31536000

heart_beats_minute = user_age_minutes * 72

print(f'You are at least {user_age_minutes} minutes old.')
input("Click Enter to See How Many Seconds You've Lived!")
print(f'You are at least {user_age_seconds} seconds old.')
input('Click Enter to See number of Heart Beats in Your Lifteime!')
print(f'Your heart has beaten an estimated {heart_beats_minute} times.')

