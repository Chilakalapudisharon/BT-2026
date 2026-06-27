class Driver:
    def __init__(self, driver_id: str, name: str, license_number: str):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "On Route"
        return f"Driver ID: {self.driver_id} | Name: {self.name} | Status: {status}"