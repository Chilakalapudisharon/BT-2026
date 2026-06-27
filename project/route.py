class Route:
    def __init__(self, route_id: str, start_point: str, end_point: str, distance_km: float):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.distance_km = distance_km
        self.stops = []

    def add_stop(self, stop_name: str):
        if stop_name not in self.stops:
            self.stops.append(stop_name)

    def __str__(self):
        stops_str = " -> ".join(self.stops) if self.stops else "No intermediate stops"
        return f"Route {self.route_id}: {self.start_point} to {self.end_point} ({self.distance_km} km) | Stops: [{stops_str}]"