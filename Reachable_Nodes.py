def reachable(adj_list, start_node):
    neighbor_finding_array = [start_node]
    reachable_node = set()
    
    while neighbor_finding_array:
        value = neighbor_finding_array.pop()
        if value not in reachable_node:
            reachable_node.add(value)
            for neighbor in adj_list[value]:
                if neighbor not in reachable_node:
                    neighbor_finding_array.append(neighbor)
                    
   
    return reachable_node

adj_list = [[1, 3], [2], [0], [4], [3], []]

# Test Cases

print("---------- Test Cases ---------")

print("first_testcase")
print(reachable(adj_list,0))
print("Second_testcase")
print(reachable(adj_list,3))

adj_list = [[1, 3, 5], [2], [0], [4], [3], [4]]

print("three_testcase")
print(reachable(adj_list,0))
print("four_testcase")
print(reachable(adj_list,5))