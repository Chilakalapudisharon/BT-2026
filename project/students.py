class Student:
    def __init__(self, student_id: str, name: str, stop_name: str):
        self.student_id = student_id
        self.name = name
        self.stop_name = stop_name
        self.assigned_route_id = None

    def assign_route(self, route_id: str):
        self.assigned_route_id = route_id

    def __str__(self):
        route = self.assigned_route_id if self.assigned_route_id else "None"
        return f"Student ID: {self.student_id} | Name: {self.name} | Stop: {self.stop_name} | Route: {route}"