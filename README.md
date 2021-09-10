# MazeSim - An A Star Search Simulation ⭐️

View the A* search algorithm do it's job right from your terminal! Given a graph with 9 nodes placed in different places on the plane, the graph searches the node with the value `*`. With the breadth-first search algorithm, the program has intergated user-inputs, in which a user can input a node from letter `a` to `z` and see the A* algorithm work it's magic. 

The A* algorithm runs in `O(b^d)` time where `b` represents the branching factor, and `d` represents the depth from the start node to the goal node, which is the node with the `*` value integrated. 

# The Graph 

The Graph can be visualized as a simple 3x3 matrix (without taking into consideration the coordinates): 

<p align="center">
  <img src="https://github.com/GEEGABYTE1/MazeSim/blob/master/Graph%20Visual%201.png" width="500">
</p>

However, with the coordinates, we can visualize how the graph actually looks like:
<p align="center">
  <img src="https://github.com/GEEGABYTE1/MazeSim/blob/master/Visual%202.png" width="500">
</p>

# The Simulation Run-through 

The user will first be prompted to enter a letter. With the use of the BFS algorithm, the program quickly scans the graph and searches the node in the graph. If the node value inputted by the user is not valid, then the simulation won't start and the user will be prompted again. However, if the value of the node is valid, with the use of the `.prompt_object_finder()` function, we find the vertex object that has the corresponding user value. We do this for the value, `*`, as well since our A* algorithm takes vertex objects as inputs. 

After finding the vertex objects, the A* algorithm commences. The base algorithm implementation uses the *Manhattan Heuristic*, however, I have implemented an *Eucliden Heuristic*, which can be implemented by chaning the statement:
`new_distance = current_distance + edge_weight + *heuristic_name*(neighbour, target)`.

*Note*: Heuristic functions are defined above the algorithm as well for reference. 

# User Customizability

Users can customize the nodes and their position by altering the graph in `nodes.py`. Users must add a vertex with a vertex object (`Vertex(value, x_position, y_position)`), and must append it to the base *objects* list. After that, users will the new vertex to the physical graph, `graph`, and can connect the vertex with other vertices with the command: `graph.add_edge(new_vertex, another_vertex_in_graph, edge_weight)` or `graph.add_edge(another_vertex_in_graph, new_vertex, edge_weight)`. 

Users can also alter the heuristics for A* and implement their own. 
