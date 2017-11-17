#Version 1.1 using Prim's Algorithm

#Data Input
import csv
times = []
route = []
routeduration = 0
with open('distmat.csv', 'rb') as r:
    stationread = csv.reader(r)
    for row in stationread:
        times.append(row)

stations = times[0] #Stores station names to match indexes
#Establish Graph/distances between nodes
#Create MST for route via Prim's algorithm
column = 1
columnlist = [1]
routelength = 0
while True:  #Checks if any rows remain
    minval = [99,0]
    times[column] = False
    for i in columnlist:  #For every column numbered
        for a in times[1:]: #For every row
            if a != False: #convert data to usable format, blanks and deleted rows have 99/infinite distance
                tempval = str(a[i])
                if not tempval:
                    tempval = 99
                else:
                    tempval = float(tempval)
            else:
                tempval = 99

            if tempval < minval[0]: #find min value in matrix
                minval = [tempval, times.index(a), i] #keep hold of row of minval
    column = minval[1] #next node is row of minval - the index of which is the index of a in times
    columnlist.append(column)
    routeduration += minval[0]
    print routeduration
    try:
        route.append([stations[minval[1]], stations[minval[2]]])
    except:
        break
print route
positions = {}
node = route[0][0]
"""finalroute = [node]
while len(route) > 0:
    for pair in route:
        if node in pair:
            if pair[0] == node:
                node = pair[1]
            else:
                node = pair[0]
            finalroute.append(node)
            route.remove(pair)"""

count = 0
with open('stations.csv', 'rb') as r:
    stationsread = csv.reader(r)
    for row in stationsread:
        try:
            positions[str(row[2])] = [float(row[1]) * 10000, (float(row[0]) - 50) * 10000]
            count+= 1
        except:
            pass

route.append(["Chesham", "Hatton Cross"])
print "Routelength:" + str(routeduration)
import networkx as nx
import matplotlib.pyplot as plo
G = nx.Graph()
G.add_nodes_from(stations[1:])
G.add_edges_from(route)
print G.nodes()
#nx.draw(G)
nx.draw_networkx(G, pos=positions, node_size=5, font_size = 0)

plo.savefig("plot.png")
plo.show()



#Convert to TfL friendly data
