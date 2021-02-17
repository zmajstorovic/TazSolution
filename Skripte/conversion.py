import sumolib
import xml.etree.cElementTree as ET
import math

net = sumolib.net.readNet('planet32.net.xml')
# koordinate u stupnjevima
lat = 45.780814
lon = 16.001999

# koordinate u metrima
# xc = 13776.76
# yc = 6041.51

xc, yc = net.convertLonLat2XY(lon, lat)

# korekcija koordinata
xc = xc - 8476.015194
yc = yc + 7581.0136319

Listasvih, x, y = [], [], []

tree = ET.parse('planet32.net.xml')
root = tree.getroot()

for junctions in root.findall('junction'):
    Listasvih.append(junctions.get('id'))
    x.append(float(junctions.get('x')))
    y.append(float(junctions.get('y')))


Min = 9999999
Xmin = 0
Ymin = 0

for i in x:
    Udaljenost = math.sqrt(math.pow((xc - i), 2) + math.pow((yc - y[x.index(i)]), 2))

    if Udaljenost < Min:
        Min = Udaljenost
        Xmin = i
        Ymin = y[x.index(i)]

Index = 0

for i in x:
    if i == Xmin and y[x.index(i)] == Ymin:
        Index = x.index(i)

Junctionofinterest = Listasvih[Index]

for edges in root.findall('edge'):
    if edges.get('from') == str(Junctionofinterest):
        edgekojitezanima = edges.attrib['id']

print(edgekojitezanima)
