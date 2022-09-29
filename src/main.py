import datetime as dt
from datetime import date
import requests
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import functions
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = 'f820095e8faeb3eb39572008bae7a59c'
city = input('Which city in Australia are you flying out of? ')
url = base_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
response = requests.get(url).json()

if response['cod'] == '404':
    city = input('That city is not available, please try again: ')
    url = base_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
    response = requests.get(url).json()



ground_temp = functions.f_to_c(response['main']['temp'])
weather_description = response['weather'][0]['description']
current_humidity = response['main']['humidity']
cloud_cover_percent = (response['clouds']['all'])
dew_point = ground_temp - ((100 - current_humidity) / 5)
cloud_base = ((ground_temp - dew_point) / 2.5) * 1000
cloud_base_temp = (-0.00984 * cloud_base) + ground_temp
alt_clear = "{:.2f}".format((10 + ground_temp) / 0.00984)
alt_mixed = "{:.2f}".format((15 + ground_temp) / 0.00984)
alt_rime = "{:.2f}".format((20 + ground_temp) / 0.00984)

flying_altitude = 2500


def ice_type():
    if weather_description != "clear sky" and cloud_base_temp <= 0:
        if cloud_base <= flying_altitude and flying_altitude < alt_clear:
            hazard = 'Clear Ice'
            print(hazard)
        elif alt_clear <= flying_altitude < alt_mixed:
            hazard = 'Mixed Ice'
            print(hazard)
        elif alt_mixed <= flying_altitude < alt_rime:
            hazard = 'Rime Ice'
            print(hazard)


if weather_description != "clear sky":
    ice_present = 'Yes'
else:
    ice_present = 'No'


print(ground_temp, cloud_base_temp, cloud_base, alt_clear, alt_mixed, alt_rime)

x = PrettyTable()
x.field_names = ['City Name', 'Weather Description', 'Cloud Cover (%)', 'Cloud Base (ft)', 'Ice Present', 'Ice-free Flying Altitude']
x.add_row([city, weather_description, cloud_cover_percent, cloud_base, ice_present, f"Try to fly below {cloud_base}, or above {alt_rime}"])
print(x)

print('Here is a visual output of the potential icing zones higlighted in red:')

def visual_output():
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░Low Risk of icing░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED} █░░░░░░░░░░Rime Ice at max {alt_rime} feet░░░░░░░░█-20C')
    print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}A█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}L█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}T█░░░░░░░░░░░Mixed Ice at max {alt_mixed} feet░░░░░░░░░█-15C')
    print(f'{Fore.RED}I█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}T█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}U█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}D█░░░░░░░░░Clear Ice at max {alt_clear} feet░░░░░░░░░█-10C')
    print(f'{Fore.RED}U█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED}E█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.RED} █░░░░░░░░░Cloud base at {cloud_base} feet░░░░░░░░█ 0C')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░No risk of icing░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
    
visual_output()



fly_today = input('Are you happy to fly today? (yes/no) ')
if fly_today == 'yes' and ice_present == 'yes':
    print('Enjoy your flight, but watch out for ice!')
elif fly_today == 'yes' and ice_present == 'no':
    print('Enjoy your flight, the weather appears to be clear!')
elif fly_today == 'no':
    def day():
        print("This is the forecast for the next week, when would you like to fly?")
        options = [str(dt.date.today() + dt.timedelta(days=1)), str(dt.date.today() + dt.timedelta(days=2)), str(dt.date.today() + dt.timedelta(days=3)), str(dt.date.today() + dt.timedelta(days=4)), str(dt.date.today() + dt.timedelta(days=5)), str(dt.date.today() + dt.timedelta(days=6)), str(dt.date.today() + dt.timedelta(days=7))]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
    if __name__ == "__day__":
        day()

# forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?'
# api_key = 'f820095e8faeb3eb39572008bae7a59c'
# url = forecast_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
# response = requests.get(url).json()
# print(response)