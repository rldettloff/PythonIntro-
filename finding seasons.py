input_month = input()
input_day = int(input())
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if not(input_month in months):
    print('Invalid')
if not(1<= input_day <= 31):
     print('Invalid')

elif input_month == "March":
    if input_day >= 20:
        print('Spring')
    else:
        print('Winter')
elif input_month == 'April':
    print('Spring')
elif input_month == 'May':
    print('Spring')
elif input_month =='June':
    if(1 <= input_day <= 20):
        print('Spring')
    else:
        print('Summer')
elif input_month == 'July':
    print('Summer')
elif input_month == 'August':
    print('Summer')
elif input_month == 'September':
    if not(1 <= input_day <= 30):
        print('Invalid')
    elif input_day <= 21:
        print('Summer')
    else:
        print('Autumn')
elif input_month == 'October':
    print('Autumn')
elif input_month == 'November':
    print('Autumn')
elif input_month == 'December':
    if (1 <= input_day <= 20):
        print('Autumn')
    else:
        print('Winter')
elif input_month == 'January':
    print('Winter')
elif input_month == 'Febuary':
    print('Winter')
    
