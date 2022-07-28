class City:
    def __init__(self, name, country_id, continent_id, visited = False, id = None):
        self.name = name
        self.country_id = country_id
        self.continent_id = continent_id
        self.visited = visited
        self.id = id