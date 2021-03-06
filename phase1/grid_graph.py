import networkx as nx
import matplotlib.pyplot as plt     #only needed for plotting the graph

def grid_graph():
    #Change here for a new arena setup
    list_of_nodes=['D1','D2','D3','D4','S1','S2','S3','S4','A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4','E1','E2','E3','E4','F1','F2','F3','F4','G1','G2','G3','G4','H1','H2','H3','H4','J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','J11','J12','J13','J14','J15','J16','K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13','K14','K15','K16']
    #No diagonal movement
    list_of_edges=[('S1','A1'),('S2','A2'),('S3','A3'),('S4','A4'),('S1','S2'),('S2','S3'),('S3','S4'),('A1','B1'),('A2','B2'),('A3','B3'),('A4','B4'),('A1','A2'),('A2','A3'),('A3','A4'),('B1','C1'),('B2','C2'),('B3','C3'),('B4','C4'),('B1','B2'),('B2','B3'),('B3','B4'),('C1','E1'),('C2','E2'),('C3','E3'),('C4','E4'),('C1','C2'),('C2','C3'),('C3','C4'),('E1','F1'),('E2','F2'),('E3','F3'),('E4','F4'),('E1','E2'),('E2','E3'),('E3','E4'),('F1','G1'),('F2','G2'),('F3','G3'),('F4','G4'),('F1','F2'),('F2','F3'),('F3','F4'),('G1','H1'),('G2','H2'),('G3','H3'),('G4','H4'),('G1','G2'),('G2','G3'),('G3','G4'),('H1','J7'),('H2','J8'),('H3','J9'),('H4','J10'),('H1','H2'),('H2','H3'),('H3','H4'),('D1','J1'),('J1','J2'),('J2','J3'),('J3','J4'),('J4','J5'),('J5','J6'),('J6','J7'),('J7','J8'),('J8','J9'),('J9','J10'),('J10','J11'),('J11','J12'),('J12','J13'),('J13','J14'),('J14','J15'),('J15','J16'),('J16','D4'),('D2','K1'),('K1','K2'),('K2','K3'),('K3','K4'),('K4','K5'),('K5','K6'),('K6','K7'),('K7','K8'),('K8','K9'),('K9','K10'),('K10','K11'),('K11','K12'),('K12','K13'),('K13','K14'),('K14','K15'),('K15','K16'),('K16','D3'),('D1','D2'),('D4','D3'),('J1','K1'),('J2','K2'),('J3','K3'),('J4','K4'),('J5','K5'),('J6','K6'),('J7','K7'),('J8','K8'),('J9','K9'),('J10','K10'),('J11','K11'),('J12','K12'),('J13','K13'),('J14','K14'),('J15','K15'),('J16','K16')]

    #graph setup
    grid = nx.Graph()
    grid.add_nodes_from(list_of_nodes)
    grid.add_edges_from(list_of_edges)
    return grid

def visual():
    #Show visually
    grid = grid_graph()
    plt.subplot(121)
    nx.draw(grid, with_labels=True)
    plt.show()
    return

#Uncomment below line to get the plot
#visual()
