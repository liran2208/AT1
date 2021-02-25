V0 = {0:(1,2)}
V1 = {0:(1, 4, 5), 1:(2, 6), 2:(3), 3:(0), 4:(1), 5:(2)}
V2 = {0:(1, 4, 5), 1:(2, 6), 2:(3, 7), 3:(7), 4:(1), 5:(2), 7:(3), 8:(1, 2), 9:(0, 4, 5, 6, 7, 3)}

E0 = list(range(0, 2))
E1 = list(range(0, 6))
E2 = list(range(0, 9))

EX_GRAPH0 = (E0, V0)
EX_GRAPH1 = (E1, V1)
EX_GRAPH2 = (E2, V2)

def make_complete_graph(num_nodes):
    # which is:

    # for i in list(range(num_nodes)):
    #     v[i] = list(range(num_nodes))
    #     v[i].pop(i)
    
    return (list(range(num_nodes)), {i: (list(set(list(range(num_nodes))) - set([i]))) for i in list(range(num_nodes))})

print ("A complete graph: ", (make_complete_graph(5)))
