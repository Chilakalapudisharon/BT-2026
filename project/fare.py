class FareCalculator:
    BASE_FARE = 15.0
    PER_KM_RATE = 2.5

    @classmethod
    def calculate_fare(cls, distance_km: float) -> float:
        """Advanced calculation: Base fare + distance premium."""
        return cls.BASE_FARE + (distance_km * cls.PER_KM_RATE)