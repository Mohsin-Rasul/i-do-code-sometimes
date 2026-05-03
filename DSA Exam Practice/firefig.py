from collections import deque

class BuildingGraph:
    def __init__(self):
        self.adj = {}
    
    def addroom(self, room):
        if room not in self.adj:
            self.adj[room] = []
            
    def connectrooms(self, r1, r2):
        self.addroom(r1)
        self.addroom(r2)
        if r2 not in self.adj[r1]:
            self.adj[r1].append(r2)
        if r1 not in self.adj[r2]:
            self.adj[r2].append(r1)

    def findclosestalarm(self, start, alarms):
        if start not in self.adj:
            return "Start room not found in the building map."

        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            current, path = queue.popleft()

            if current in alarms:
                print(f" Alarm found! Closest room is '{current}'.")
                print(f"Shortest path: {' -> '.join(path)}")
                return path

            for neighbor in self.adj.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    newpath = path + [neighbor]
                    queue.append((neighbor, newpath))
        
        return "No fire alarm room is reachable."

building = BuildingGraph()
building.connectrooms("HA", "R101")
building.connectrooms("HA", "R102")
building.connectrooms("R101", "Sto")
building.connectrooms("R102", "Sta")
building.connectrooms("Sta", "R205")

alarms = {"Sto", "R205"} 
start = "HA"

print("\n--- Firefighting Robot (BFS) ---")
building.findclosestalarm(start, alarms)
