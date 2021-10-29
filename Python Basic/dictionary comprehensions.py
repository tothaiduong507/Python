cities_F={'New York':32,
          'Boston':75,
          'Los Angeles':100,
          'Chicago':50}

cities_C={key:round((value-32)*5/9) for (key,value) in cities_F.items()}
print(cities_C)

weather={'New York':'snowing',
         'Chicago':'sunny',
         'Boston':'snowing',
         'LA':'sunny'}
sunny_weather={key:value for (key,value)in weather.items() if value =="sunny"}
print(sunny_weather)
def check_temp(value):
    if value>=40:
        return "WARM"
    else:
        return "COLD"
#desc_cities={key: ("WARM" if value>= 40 else "COLD") for (key,value)in cities_F.items()}

desc_cities={key: check_temp(value) for (key,value)in cities_F.items()}
print(desc_cities)
