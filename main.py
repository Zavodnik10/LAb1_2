import argparse
parser = argparse.ArgumentParser()
parser.add_argument('a', type=int)
parser.add_argument('b', type=float)
parser.add_argument('k', type=float)

args = parser.parse_args()
year1 = args.a
cords = (args.b, args.k)

from haversine import haversine
from geopy.geocoders import Nominatim
import folium
geolocator = Nominatim(user_agent="hghghg")
def read_file(file_name):
    
    with open (file_name, 'r') as file:
        s = []
        for line in file.readlines()[13:300]:
            s.append(line)

    return s
def dicte(year, s):
    
    year = str(year)
    year = f'({year})'
    
    d = []
    for i in s:
        if year in i:
            d.append(i)
    for i in range (len(d)):
        
        d[i] = d[i].split('\t')       
        d[i] = d[i][-1]
        d[i] = d[i].strip('\n')
    return d
def vids(d, cord):
    for i in range(len(d)):
        d[i] = d[i].split(',')
    a = ''
    o = []
    for i in d:
        for j in i:
            a += j
            o.append(a)
        a = '' 
    
    b = []
    for j, i in enumerate (o):
        try:
            location = geolocator.geocode(i)           
            
            b.append((location.latitude, location.longitude))
            
        except :
            continue
    c = []
    for j, i in enumerate(b):
        z = haversine(i, cord)
        c.append([i, z])
    c = sorted(c, key = lambda x: x[1])
    new_list = []

    [new_list.append(item) for item in c if item not in new_list]
    
    new_list = new_list[0:10]
    new_list1 = []
    for i in new_list:
        new_list1.append(i[0])
    return new_list1
print(cords)
print(year1)
print (vids(dicte(year1, read_file('locations.list')), cords))

