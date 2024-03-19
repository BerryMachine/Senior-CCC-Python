# initialize variables
name = ''
temp = 201

while True:
  # get each city and it's temperature as input
  city = input().split()
  
  # store name and temperature of lowest temperature city
  if int(city[1]) < temp:
    temp = int(city[1])
    name = value[0]

  # break when user enters "Waterloo"
  if value[0] == "Waterloo":
    break

print(name)
