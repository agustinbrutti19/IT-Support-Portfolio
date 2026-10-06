def calculate_priority(impact, urgency):

    priority_matrix = {
        ("Low", "Low"): "Low",
        ("Low", "Medium"): "Low",
        ("Low", "High"): "Medium",

        ("Medium", "Low"): "Low",
        ("Medium", "Medium"): "Medium",
        ("Medium", "High"): "High",

        ("High", "Low"): "Medium",
        ("High", "Medium"): "High",
        ("High", "High"): "Critical"
    }

    return priority_matrix[(impact, urgency)]

print(calculate_priority("High", "High"))
print(calculate_priority("Low", "High"))
  