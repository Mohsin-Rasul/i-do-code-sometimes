class CampusMap:
    def __init__(self):
        self.adj = {}

    def insertbuilding(self, name):
        if name not in self.adj:
            self.adj[name] = []
            print(f"Building '{name}' added.")
        else:
            print(f" Building '{name}' already exists.")

    def insertwalkway(self, b1, b2):
        self.insertbuilding(b1)
        self.insertbuilding(b2)

        if b2 not in self.adj[b1]:
            self.adj[b1].append(b2)
        
        if b1 not in self.adj[b2]:
            self.adj[b2].append(b1)
            
        print(f" Walkway created between '{b1}' and '{b2}'.")

campus = CampusMap()

print("\n--- Inserting New Buildings ---")
campus.insertbuilding("Lib")
campus.insertbuilding("StuU")
campus.insertbuilding("SciH")

print("\n--- Creating New Walkways ---")
campus.insertwalkway("Lib", "StuU")
campus.insertwalkway("StuU", "SciH")
campus.insertwalkway("Lib", "Dorm")
campus.insertwalkway("Lib", "Lib")
