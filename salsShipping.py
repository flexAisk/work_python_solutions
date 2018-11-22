premium_ground = 125.00

#ground
def ground_shipping(weight):
  cost = 0
  if weight <= 2:
    cost = weight * 1.50 + 20.00
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20.00
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20.00
  else:
    cost = weight * 4.75 + 20.00
  return cost

#drone

def drone_shipping(weight):
  cost = 0
  if weight <= 2:
    cost = weight * 4.50 
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00 
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost

#best_shipping

def best_shipping(weight):
  ground_price = ground_shipping(weight)
  drone_price = drone_shipping(weight)
  if ground_price < drone_price and ground_price < premium_ground:
    print("It's cheaper to ship via ground!")
    print(ground_price)
    return ground_price
  elif drone_price < ground_price and drone_price < premium_ground:
    print("It's chearper to ship via drone!")
    print(drone_price)
    return drone_price
  else:
    print("It's cheaper to ship via premium ground!")
    print(premium_ground)
    return premium_ground
  
  
best_shipping(1)