from itertools import permutations
import csv

def permutations_nodes(nodes):
    return [[a, b] for a, b in permutations(nodes, 2)]

def permutations_subordinations(control_node, nodes):
    return [[node, control_node] for node in nodes]

def permutations_management(control_node, nodes):
    return [[control_node, node] for node in nodes]

def all_subordinations(subordination,  nodes, submission_dict):
    for node in nodes:
        if node not in subordination:
            subordination.append(node)
            if node in submission_dict:
                all_subordinations(subordination, submission_dict[node], submission_dict)

def indirect_subordination(subordination, nodes, submission_dict):
    for node in nodes:
        if node in submission_dict:
            all_subordinations(subordination, submission_dict[node], submission_dict)

#a la DFS
def process(nodes):
    connections = [[] for i in range(5)]
    submissions = {}
    for node in nodes:
        if node[0] not in connections[0]:
            connections[0].append(node[0])
        if node[1] not in connections[1]:
            connections[1].append(node[1])
        if node[0] in submissions:
            submissions[node[0]].append(node[1])
        else:
            submissions[node[0]] = [node[1]]

    for key in submissions:
        nodes = submissions[key]
        if len(nodes) > 1:
            connections[4].extend(nodes)
        subordination = []
        indirect_subordination(subordination, submissions[key], submissions)
        if key not in connections[2] and len(subordination) > 0:
            connections[2].append(key)

        for node in subordination:
            if node not in connections[3]:
                connections[3].append(node)

    [r.sort() for r in connections]
    return connections

file = open('dataset.csv')
data = csv.reader(file, delimiter=',')
prepared_data = [[int(node) for node in row] for row in data]

result = process(prepared_data)
print(result)