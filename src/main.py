import requests
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import clearing
import datetime
import functions
import colorama
from colorama import Fore
colorama.init(autoreset=True)

options = ['Choose A City', 'Request 5-day Forecast', 'Information on Icing', 'Exit']
submenu_options = ['Clear Ice', 'Mixed Ice', 'Rime Ice', 'Return to main menu']
submenu = TerminalMenu(submenu_options)
main_menu = TerminalMenu(options)
quitting = False
clearing.clear()
while quitting == False:
    clearing.clear()
    menu_entry_index = main_menu.show()
    selection = options[menu_entry_index]
    if selection == 'Exit':
        quitting = True
        clearing.clear()
        break
    if selection == 'Information on Icing':
        submenu_entry_index = submenu.show()
        submenu_selection = submenu_options[submenu_entry_index]
        if submenu_selection == 'Return to main menu':
            clearing.clear()
            continue
        elif submenu_selection == 'Clear Ice':
            print('Clear ice is formed by supercooled large water droplets that mostly occur in the temperature range from 0 C to -10 C. The ice itself freezes slowly upon impact forming a smooth sheet of transparent ice. Because the droplets are large, as they freeze, they spread over the surface, combining with other droplets, forming a solid surface. There are no air bubbles to weaken the structure of the ice layer. As more ice accumulates, it developes ridges which pose a large risk of causing issues to aerodynamic and instrument performance with up to a 500% increase in drag. It\'s thickness also makes it more difficult to remove using de-icing equipment.\n')
            print(f'Risk Level: {Fore.RED}High')
            input('\nPress enter to continue.')
            clearing.clear()
            continue
        elif submenu_selection == 'Rime Ice':
            print('Rime ice is a type of ice that occurs in the coldest conditions, usually below -15C. Rime ice is opaque or milky/white ice that occurs commonly in stratiform clouds. The supercooled water droplets that form are much smaller than that of clear ice. This means the droplets maintain the sperical shapes as they freeze without much spreading. This type if icing is usually confined to the leading edge of the planes wing, and can easily be removed with de-icing technology built into the aircraft.\n')
            print(f'Risk Level: {Fore.GREEN}Low')
            input('\nPress enter to continue.')
            clearing.clear()
            continue
        elif submenu_selection == 'Mixed Ice':
            print('Mixed ice is the most common type of ice that may occur due to the varying nature of droplet sizes within a cloud. This type of ice is most commonly found in temperatures ranging from -10C to -15C, and includes characteristics of both rime and clear icing.\n')
            print(f'Risk Level: {Fore.YELLOW}Moderate')
            input('\nPress enter to continue.')
            clearing.clear()
            continue
    if selection == 'Choose A City':
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        api_key = 'f820095e8faeb3eb39572008bae7a59c'
        city = input('Which city in Australia are you flying out of? ')
        url = base_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
        response = requests.get(url).json()
        if response['cod'] == '404' or response['cod'] == '400':
            city = input('That didn\'t work, please try again: ')
            url = base_url + '&appid=' + api_key + '&q=' + city + '&units=imperial'
            response = requests.get(url).json()

        ground_temp = functions.f_to_c(response['main']['temp'])
        weather_description = response['weather'][0]['description']
        current_humidity = response['main']['humidity']
        cloud_cover_percent = (response['clouds']['all'])
        dew_point = ground_temp - ((100 - current_humidity) / 5)
        cloud_base = int(((ground_temp - dew_point) / 2.5) * 1000)
        cloud_base_temp = (-0.00984 * cloud_base) + ground_temp
        alt_clear = int(cloud_base + 5000)
        alt_mixed = int(cloud_base + 7500)
        alt_rime = int(cloud_base + 10000)
        
        if weather_description != 'clear sky':
            ice_present = 'Yes'
            safe_zone = f'Safe to fly below {cloud_base} feet, or above {alt_rime} feet'

        else:
            ice_present = 'No'
            safe_zone = 'There is no potential for icing!'

        x = PrettyTable()
        x.field_names = ['City Name', 'Weather Description', 'Cloud Cover (%)', 'Cloud Base (ft)', 'Ice Present', 'Ice-free Flying Altitude']
        x.add_row([city, weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
        print(x)
        if ice_present == 'No':
            print('Here is a visual output of the potential icing zones higlighted in red:')
            print('-----------------------------------------------------------------------')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░No ice at any flying altitude!░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print('')
            input('Press enter to continue.')
            clearing.clear()
            continue
        else:
            print('Here is a visual output of the potential icing zones higlighted in red:')
            print('-----------------------------------------------------------------------')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░Low Risk of icing░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED} █░░░░░░░░░░░░░░░Rime Ice at max {alt_rime} feet░░░░░░░░░░░░░░░░░█-20C')
            print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED}A█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED}L█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED}T█░░░░░░░░░░░░░░░Mixed Ice at max {alt_mixed} feet░░░░░░░░░░░░░░░░█-15C')
            print(f'{Fore.RED}I█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED}T█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED}U█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED}D█░░░░░░░░░░░░░░░Clear Ice at max {alt_clear} feet░░░░░░░░░░░░░░░░█-10C')
            print(f'{Fore.RED}E█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.RED} █░░░░░░░░░░░░░░░Cloud base at {cloud_base} feet░░░░░░░░░░░░░░░░░░░█ 0C')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░No risk of icing░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print(f'{Fore.GREEN} █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█')
            print('')
            input('Press enter to continue.')
            clearing.clear()
            continue
    if selection == 'Request 5-day Forecast':
            forecast_base_url = 'https://api.openweathermap.org/data/2.5/forecast?'
            api_key = 'f820095e8faeb3eb39572008bae7a59c'
            forecast_city = input('Which city in Australia do you want to know the forecast for? ')
            forecast_url = forecast_base_url + '&appid=' + api_key + '&q=' + forecast_city + '&units=imperial'
            forecast_response = requests.get(forecast_url).json()
            if forecast_response['cod'] == '404' or forecast_response['cod'] == '400':
                forecast_city = input('That didn\'t work, please try again: ')
                forecast_url = forecast_base_url + '&appid=' + api_key + '&q=' + forecast_city + '&units=imperial'
                forecast_response = requests.get(forecast_url).json()
                clearing.clear()
            print(forecast_response)

            # forecast = PrettyTable()
            # forecast.field_names = ['City Name', 'Date', 'Weather Description', 'Cloud Cover (%)', 'Cloud Base (ft)', 'Ice Present', 'Ice-free Flying Altitude']
            # forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(1), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
            # forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(2), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
            # forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(3), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
            # forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(4), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
            # forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(5), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
            # # print(forecast)
                    
            # ground_temp = functions.f_to_c(forecast_response['main']['temp'])
            # weather_description = forecast_response['weather'][0]['description']
            # current_humidity = forecast_response['main']['humidity']
            # cloud_cover_percent = (forecast_response['clouds']['all'])
            # dew_point = ground_temp - ((100 - current_humidity) / 5)
            # cloud_base = int(((ground_temp - dew_point) / 2.5) * 1000)
            # cloud_base_temp = (-0.00984 * cloud_base) + ground_temp
            # alt_clear = int(cloud_base + 5000)
            # alt_mixed = int(cloud_base + 7500)
            # alt_rime = int(cloud_base + 10000)
            print('')
            input('Press enter to continue.')
            clearing.clear()
            continue