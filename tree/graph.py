def add_node(v):
    if v in graph:
        print("node already present")
    else:
        graph[v] = []
def add_edge(v1,v2):
    if v1 not in graph:
        print("node not present")
    if v2 not in graph:
        print("node not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

graph ={}
add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_node("e")
add_edge("a","b")
add_edge("a","c")
add_edge("a","d")

print(graph)