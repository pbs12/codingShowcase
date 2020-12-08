'''
Problem 2 - Scaling PageRank and Search in a Citation Network
'''

import numpy as np

def efficentPageRank(nodes_text_file,edges_text_file,epsilon,one_iteration_only=False):

    with open(nodes_text_file) as f1:
        nodes = [line.rstrip() for line in f1]

    with open(edges_text_file) as f2:
        edges = [[int(x) for x in line.split()] for line in f2]

    num_nodes = len(nodes)
    num_edges = len(edges)
    isPointedToBy = [[] for each_node in nodes]

    outdegrees = [0]*num_nodes
    pointingTo = [[] for each_node in nodes]
    for i in range(num_edges):
        outdegrees[edges[i][0]] = outdegrees[edges[i][0]] + 1
        pointingTo[edges[i][0]].append(edges[i][1])
        isPointedToBy[edges[i][1]].append(edges[i][0])

    point85COEFF = [0]*num_nodes
    for pointedNode in range(num_nodes):
        tempSum = 0
        for pointingNode in isPointedToBy[pointedNode]:
            print(str(pointedNode) + "," + str(pointingNode))
            tempSum = tempSum + .85/outdegrees[pointingNode]

        point85COEFF[pointedNode] = tempSum
    sinks = []
    for i in range(num_nodes):
        if outdegrees[i] == 0:
            sinks.append(i)
    num_sinks = len(sinks)
    non_sinks = num_nodes - num_sinks

    pi_t = [1/num_nodes]*num_nodes
    iterations_done = 0;
    TVD = epsilon+1

    while (iterations_done <= 2):
        pi_next = [0]*num_nodes
        for j in range(num_nodes):
            pi_next[j] = pi_next[j] + (num_sinks/num_nodes) * pi_t[j] + (non_sinks*.15*pi_t[j])/num_nodes
            print("sinks: " + str((num_sinks/num_nodes) * pi_t[j]) + "\n")
            print("2nd case" + str((non_sinks*.15*pi_t[j])/num_nodes) + "\n")


            print("1st case" + str(point85COEFF[j]*pi_t[j]) + "\n")
            print("BUFFER")
            #print(pi_next[j])
            #on average pointingTo j length is 1 due to sparse matrix
            pi_next[j] = pi_next[j] + point85COEFF[j]*pi_t[j]
        print(str(sum(pi_next)))

        TVD = .5*sum(abs(np.array(pi_next)-np.array(pi_t)))
        pi_t = pi_next
        iterations_done = iterations_done + 1

        if one_iteration_only == True:
            if iterations_done == 1:
                break

    pi_final = pi_t

    return [nodes,pi_final,iterations_done]
