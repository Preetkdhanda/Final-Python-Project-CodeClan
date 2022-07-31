class City:
    def __init__(self, name, country, continent, visited = False, id = None):
        self.name = name
        self.country = country
        self.continent = continent
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True