print("===FREETOWN COMMUTER TRANSIT SYSTEM===")
print("Enter RouteID")
routeID = input()
print("Enter vehicle maximum capacity")
maxCapacity = int(input())
print("Enter initial passenger count")
passengerCount = int(input())
boardMore = "YES"
while boardMore == "YES" and passengerCount < maxCapacity:
    print("Enter Zone (1-3)")
    distanceZone = int(input())
    while distanceZone < 1 or distanceZone > 3:
        print("INVALID ZONE! Please enter a zone between 1 and 3:")
        distanceZone = int(input())
    print("Is Peak Hour? (YES/NO)")
    peakHour = input()
    if distanceZone == 1:
        baseFare = 5.0
    else:
        if distanceZone == 2:
            baseFare = 10.0
        else:
            baseFare = 15.0
    if peakHour == "YES":
        finalFare = baseFare * 1.25
    else:
        finalFare = baseFare
    passengerCount = passengerCount + 1
    print("BOARDING SUCCESSFUL!")
    print("Fare: " + str(finalFare))
    print("passengers on board: " + str(passengerCount))
    if passengerCount >= maxCapacity:
        boardMore = "NO"
        print("VEHICLE IS FULL!")
    else:
        print("Board more passengers? (YES/NO)")
        boardMore = input()
print("Session finished. Have a safe journey!")
