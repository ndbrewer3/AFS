### mock_data

mock_carriers = {
    "Swift Transit": {"rate_per_mile": 2.10, "available_trucks": 3, "reliability": 0.95},
    "FedEx Freight": {"rate_per_mile": 2.50, "available_trucks": 1, "reliability": 0.99},
    "TForce Freight": {"rate_per_mile": 1.75, "available_trucks": 5, "reliability": 0.80}
}

mock_locations = {
    "Washington, D.C.": {"Raleigh": 278, "Roanoke": 240, "Charlotte": 399},
    "Raleigh": {"Roanoke": 157, "Charlotte": 170},
    "Roanoke": {"Charlotte": 196}
}

mock_disruptions = [
    {"location": "Raleigh", "delay_hours": 8, "reason": "Interstate Construction causing lane closures"},
]