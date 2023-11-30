# Search methods

import search
import timeit

def execution_time(function):
    return timeit.timeit(lambda: function(ab)[0].path(), number=10000)


if __name__ == '__main__':
    ab = search.GPSProblem('N', 'D', search.romania)

    bfs = search.breadth_first_graph_search(ab)
    dfs = search.depth_first_graph_search(ab)
    bab = search.branch_and_bound(ab)
    babh = search.branch_and_bound_heuristics(ab)



    print("Algoritmo BFS:\n", bfs[0].path(), "\nNodos generados=", bfs[1], "\nNodos visitados=",bfs[2],"\nCoste total=", bfs[0].__dict__["path_cost"],"\n")
    print("Algoritmo DFS:\n", dfs[0].path(), "\nNodos generados=",dfs[1], "\nNodos visitados=",dfs[2],"\nCoste total=", dfs[0].__dict__["path_cost"],"\n")
    print("Algoritmo Branch and bound:\n", bab[0].path(), "\nNodos generados=",bab[1], "\nNodos visitados=",bab[2],"\nCoste total=", bab[0].__dict__["path_cost"],"\n")
    print("Algoritmo Branch and bound con heurística:\n", babh[0].path(), "\nNodos generados=",babh[1], "\nNodos visitados=",babh[2],"\nCoste total=", babh[0].__dict__["path_cost"],"\n")

    print("El tiempo de ejecución medio de del bfs es:", execution_time(search.breadth_first_graph_search))
    print("El tiempo de ejecución medio de del dfs es:", execution_time(search.depth_first_graph_search))
    print("El tiempo de ejecución medio de del branch and bound es:",execution_time(search.branch_and_bound))
    print("El tiempo de ejecución medio de del branch and bound con heurística es:", execution_time(search.branch_and_bound_heuristics))
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

