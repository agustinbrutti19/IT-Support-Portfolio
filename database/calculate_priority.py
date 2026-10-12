def calculate_priority(impact, urgency):
    valid_levels = {"low": "Low", "medium": "Medium", "high": "High"}

    if not isinstance(impact, str):
        raise ValueError("Impact must be a string.")

    if not isinstance(urgency, str):
        raise ValueError("Urgency must be a string.")

    impact = impact.strip().lower()
    urgency = urgency.strip().lower()

    if impact not in valid_levels:
        raise ValueError(
            f"Invalid impact: {impact}. Expected Low, Medium, or High."
        )

    if urgency not in valid_levels:
        raise ValueError(
            f"Invalid urgency: {urgency}. Expected Low, Medium, or High."
        )

    impact = valid_levels[impact]
    urgency = valid_levels[urgency]

    priority_matrix = {
        ("Low", "Low"): "Low",
        ("Low", "Medium"): "Low",
        ("Low", "High"): "Medium",
        ("Medium", "Low"): "Low",
        ("Medium", "Medium"): "Medium",
        ("Medium", "High"): "High",
        ("High", "Low"): "Medium",
        ("High", "Medium"): "High",
        ("High", "High"): "Critical",
    }

    return priority_matrix[(impact, urgency)]
