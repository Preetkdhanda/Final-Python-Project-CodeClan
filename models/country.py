class Country:
    def __init__(self, name, continent_id, visited = False, id=None) -> None:
        self.name = name
        self.continent_id = continent_id
        self.visited = visited
        self.id = id