# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename:str)->dict:
    
    stations={}
    
    with open(filename) as station_data:
        
        for line in station_data:
            line=line.strip()
            parts=line.split(";")
            if parts[0]=="Longitude":
                continue
            
            stations[parts[3]]=(float(parts[0]),float(parts[1]))
    
    return stations

def distance(stations:dict, station1:str, station2:str)->float:
    
    longitude1=0
    latitude1=0
    longitude2=0
    latitude2=0
    
    for station, station_data in stations.items():
        if station==station1:
            longitude1=float(station_data[0])
            latitude1=float(station_data[1])
        elif station==station2:
            longitude2=float(station_data[0])
            latitude2=float(station_data[1])
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km
        

        
            
if __name__=="__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    
    #stations = get_station_data('stations1.csv')
    #station1, station2, greatest = greatest_distance(stations)
    #print(station1, station2, greatest)