class RoadNetwork:
    def __init__(self):
        self.adj = {}

    def addroad(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj[u]:
            self.adj[u].append(v)

        if v not in self.adj:
            self.adj[v] = []
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def displayroads(self):
        roads = set()
        print("--- Unique Roads in the Network ---")
        
        for u in self.adj:
            for v in self.adj[u]:
                if u < v:
                    road = (u, v)
                else:
                    road = (v, u)
                
                if road not in roads:
                    roads.add(road)
                    print(f"Road: {u} <-> {v}")

city = RoadNetwork()
city.addroad("Main", "Oak")
city.addroad("Elm", "Maple")
city.addroad("Main", "Maple")
city.addroad("Oak", "Elm") 

city.displayroads()
