class Vehicle:
    def __init__(self, vehicle_id: str, capacity: int):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.assigned_driver = None

    def assign_driver(self, driver_name: str):
        self.assigned_driver = driver_name

    def __str__(self):
        driver = self.assigned_driver if self.assigned_driver else "Unassigned"
        return f"Vehicle ID: {self.vehicle_id} | Capacity: {self.capacity} | Driver: {driver}"


class Bus(Vehicle):
    def __init__(self, vehicle_id: str, capacity: int, bus_number: str):
        super().__init__(vehicle_id, capacity)
        self.bus_number = bus_number

    def __str__(self):
        base_str = super().__str__()
        return f"[Bus No: {self.bus_number}] {base_str}"
        