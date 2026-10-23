#BR2
import serial
import csv

ser = serial.Serial("COM10", 115200, timeout=1)

line = ser.readline().decode("utf-8").strip()
                    
 
filename = "LCCS.csv"
alert_flag = False

for x in range(10):
    parts = line.split(",")
    microtemp = float(parts[0])
    microlight = float(parts[1])
    fire_risk = parts[2]
    sim_result = parts[3]

#AR1
    fire_risk = round(microtemp*microlight,1) #MY BASE MODEL
    
    print("Current temp is", microtemp, "Light level :", microlight, "Fire risk is", fire_risk, "BR 3 Simulation Result:", sim_result)
    with open(filename, "a", newline="") as i:
        writer = csv.writer(i)
        writer.writerow([microtemp,microlight,fire_risk,sim_result])
        
print("BR2: Csv file saved as: ", filename)


print("The fire risk is ", fire_risk)

# AR2
print("\n\n-~~~- What ifs -~~~-")
            
# Scenario 1
print("\n Scenario 1: What if there's a thin canopy and low temperature")

sc1_microtemp = 5 # low temp
sc1_microlight = 125 # thin canopy

sc1_fire_risk = round((sc1_microtemp*sc1_microlight),1)
print("Temp =", sc1_microtemp, "Light =", sc1_microlight, "=> Scenario A Fire risk=", sc1_fire_risk)

if sc1_fire_risk > 6000:
    print("Fire risk is high")
else:
    print("Fire risk is low")

# Scenario 2
print("\n Scenario 2: What if There's a Thick Canopy and high temperature")

# hard code variables to set simulated conditions for scenerio
sc2_microtemp = 33 # high temp
sc2_microlight = 200 # thick canopy

sc2_fire_risk = round((sc2_microtemp*sc2_microlight),1)
print("Temp =", sc2_microtemp, "Light =", sc2_microlight, "=> Scenario B Fire risk=", sc2_fire_risk)

if sc2_fire_risk > 6000:
    print("Fire risk is high")
else:
    print("Fire risk is low")

#AR3
print("\n\n-~~~-Adaptive system-~~~-")

if fire_risk > 6000 and alert_flag == False:
    print("Checking if there is a risk or not: ALERT!!!")
    alert_flag = True
else:
    print("Checking if there is a risk or not: No alert")
    alert_flag = False

