def hotel_cost(nights):
  return 140*nights
def plane_ride_cost(city):
  if (city=="Charlotte"):
    return 183
  if (city=="Tampa"):
    return 220
  if (city=="Pittsburgh"):
    return 222
  if (city=="Los Angeles"):
    return 475
def rental_car_cost(days):
  if(days>=7):
    return (days*40)-50
  elif(days>=3):
    return (days*40)-20
  else:
    return days*40
def trip_cost(city,days,spending_money):
  sum=hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+spending_money
  return sum
city="Los Angeles"
print (trip_cost(city,5,600))
input("")