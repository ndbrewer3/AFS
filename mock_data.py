### mock_data

mock_carriers = {
    "Swift Transit": {"rate_per_mile": 2.10, "available_trucks": 3, "reliability": 0.95},
    "FedEx Freight": {"rate_per_mile": 2.50, "available_trucks": 1, "reliability": 0.99},
    "TForce Freight": {"rate_per_mile": 1.75, "available_trucks": 5, "reliability": 0.80}
}

mock_locations = {
    "Washington, D.C.": {"Boston": 920, "Charlotte": 297, "Atlanta": 530},
    "Boston": {"Charlotte": 630, "Atlanta": 283},
    "Charlotte": {"Atlanta": 450}
}

mock_disruptions = [
    {"location": "Charlotte", "delay_hours": 8, "reason": "Bridge Closure due to structural integrity check"}
]