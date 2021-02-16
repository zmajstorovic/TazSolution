import sumolib

lat = 45.848206
lon = 15.855591
edges = []
x = 12422.48
y = 6954.76
net = sumolib.net.readNet('planet32.net.xml')
r = 200
# x, y = net.convertLonLat2XY(lon, lat)
edges = net.getNeighboringEdges(x, y, r)
# pick the closest edge
if len(edges) > 0:
    distancesAndEdges = sorted([(dist, edge) for edge, dist in edges])
    dist, closestEdge = distancesAndEdges[0]
else:
    print('edges <= 0')
