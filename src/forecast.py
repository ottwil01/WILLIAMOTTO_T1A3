# forecast_base_url = 'https://api.openweathermap.org/data/2.5/forecast?'
# api_key = 'f820095e8faeb3eb39572008bae7a59c'
# forecast_city = input('Which city in Australia do you want to know the forecast for? ')
# forecast_url = forecast_base_url + '&appid=' + api_key + '&q=' + forecast_city + '&units=imperial'
# forecast_response = requests.get(forecast_url).json()
# if forecast_response['cod'] == '404' or forecast_response['cod'] == '400':
#     forecast_city = input('That didn\'t work, please try again: ')
#     forecast_url = forecast_base_url + '&appid=' + api_key + '&q=' + forecast_city + '&units=imperial'
#     forecast_response = requests.get(forecast_url).json()
#     clearing.clear()
# print(forecast_response)

# forecast = PrettyTable()
# forecast.field_names = ['City Name', 'Date', 'Weather Description', 'Cloud Cover (%)', 'Cloud Base (ft)', 'Ice Present', 'Ice-free Flying Altitude']
# forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(1), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
# forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(2), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
# forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(3), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
# forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(4), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
# forecast.add_row([forecast_city, datetime.datetime.now() + datetime.timedelta(5), weather_description, cloud_cover_percent, cloud_base, ice_present, safe_zone])
# print(forecast)
        
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
