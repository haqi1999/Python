import sys
class Node(): 
    def _init_(self, state, parent, action)
        self.state = state
        self.parent = parent
        self.action = action

# For DFS
class StackFrontier()
    # Initial empty state
    def __init__(self):
        self.frontier = []

    # Adds to the frontier 
    def add(self,node):
        self.frontier.append(node)

    # Checks if the frontier contains a particular state 
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    # Checks if the frontier is empty. If true then return length of zero
    def empty(self):
        return len(self.frontier) == 0
    
    # Checks if the frontier is empty. If true then empty frontier text is returned
    # Else, the last element is removed from the stack (DFS) by using negative indexing
    # Then update the frontier by taking every element except the last one
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
    
# In this class, the class inherits from the StackFrontier
# But we take the first element instead to take into consideration rather than the last one (FOR BFS)
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty()
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier [1:]
            return node

"""A section code is missing in this script. FOR IMPORTING THE MAZE"""

def solve (self):
    """Find solution to maze, if one exist"""

    # Keep track of number of states explored
    self.num_explored = 0

    # Initialise frontier to just the starting position
    start = Node(state=self.start, parent=None, action=None)
    frontier  = StackFrontier()
    frontier.add(start)

    # Initialise an empty explored set
    self.explored = set()

    # Keep looping until solution found
    while True:

        # If nothing left in frontier, then no path
        if frontier.empty():
            raise Exception("No Solution")
        
        # Choose a node from the frontier 
        node = frontier.remove()
        self.num_explored += 1

        # If node is the goal, then we have a solution
        if node.state == self.goal:
            actions=[]
            cells = []

            # Follow parent nodes to find solution
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            self.solution = (actions, cells)
            return
        
        # Mark node as explored set 
        self.explored.add(node.state)

        # Add neighbours to frontier
        # Checks if the node and state is in the frontier or in the explored set 
        # If not, the node and state is added as the new child 
        for action, state in self.neighbors(node.state):
            if not frontier.contains_state(state) and state not in self.explored:
                child = Node(state = state, parent = node, action = action)
                frontier.add(child)


        
  
        
        