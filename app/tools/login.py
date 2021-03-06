# the program will generate greet message according to server/client time
# and select a wallpaper number randomly
# 'wallpaper_num' for select a wallpaper
# 'greet' will change with time
# 'date' to record date of time
# 'color_mode' to change the background color at night
import random
from pytz import timezone
from datetime import datetime

la_tz = timezone('America/Los_Angeles')
la_time = datetime.now(la_tz)

def greet():
    # format time into something like Sat Mar 08 22:12:03 2020
    cur_time = la_time.strftime("%a %b %d %H:%M:%S %Y")
    wallpaper_daytime = random.randint(0, 22)
    wallpaper_night = random.randint(23, 30)

    # display different greet information at different time
    date = cur_time[0:10]
    hour = int(cur_time[11:13])
    greet = 'Good'
    color_mode = 'bg-white'

    if 5 <= hour < 13:
        greet += ' Morning'
        wallpaper = wallpaper_daytime
    elif 13 <= hour < 19:
        greet += ' Afternoon'
        wallpaper = wallpaper_daytime
    else:
        greet += ' Evening'
        wallpaper = wallpaper_night

    return {
        'wallpaper_num': wallpaper,
        'greet': greet,
        'date': date,
        'color_mode': color_mode,
    }
