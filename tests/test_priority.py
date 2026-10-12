import pytest

from database.calculate_priority import calculate_priority


@pytest.mark.parametrize(
    "impact, urgency, expected",
    [
        ("Low", "Low", "Low"),
        ("Low", "Medium", "Low"),
        ("Low", "High", "Medium"),
        ("Medium", "Low", "Low"),
        ("Medium", "Medium", "Medium"),
        ("Medium", "High", "High"),
        ("High", "Low", "Medium"),
        ("High", "Medium", "High"),
        ("High", "High", "Critical"),
    ],
)

def test_calculate_priority(impact, urgency, expected):
    assert calculate_priority(impact, urgency) == expected

def test_calculate_priority_invalid_impact():
    with pytest.raises(ValueError, match="Invalid impact"):
        calculate_priority("Urgent", "High")

def test_calculate_priority_invalid_urgency():
    with pytest.raises(ValueError, match="Invalid urgency"):
        calculate_priority("High", "Urgent")

@pytest.mark.parametrize(
    "impact, urgency, expected",
    [
        ("low", "high", "Medium"),
        ("LOW", "HIGH", "Medium"),
        (" Low ", " High ", "Medium"),
        ("mEdIuM", "lOw", "Low"),
    ],
)
def test_calculate_priority_normalizes_input(impact, urgency, expected):
    assert calculate_priority(impact, urgency) == expected

@pytest.mark.parametrize("impact, urgency", [
    (123, "High"),
    ("High", None),
])
def test_calculate_priority_rejects_non_string_values(impact, urgency):
    with pytest.raises(ValueError, match="must be a string"):
        calculate_priority(impact, urgency)