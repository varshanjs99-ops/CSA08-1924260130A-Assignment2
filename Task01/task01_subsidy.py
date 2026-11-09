# Q1 – Decisions with Many Boundaries
# Electricity subsidy eligibility

def subsidy_separate(units, ration_card, age_over_80):
    """Intentionally demonstrates the risk of independent if statements."""
    decisions = []
    if units <= 100:
        decisions.append("Full subsidy")
    # Deliberately faulty independent condition: it omits the lower bound.
    # At <=100 units with a ration card, this overlaps with the full-subsidy rule.
    if units <= 200 and ration_card:
        decisions.append("Partial subsidy")
    if units > 200 and age_over_80:
        decisions.append("Special subsidy")
    if not decisions:
        decisions.append("No subsidy")
    return decisions

def subsidy_elif(units, ration_card, age_over_80):
    """Returns exactly one decision, using mutually exclusive branches."""
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200 and age_over_80:
        return "Special subsidy"
    else:
        return "No subsidy"

households = [
    ("H1", 80, False, False),
    ("H2", 100, True, False),
    ("H3", 101, True, False),
    ("H4", 150, False, False),
    ("H5", 200, True, False),
    ("H6", 201, False, False),
    ("H7", 250, False, True),
    ("H8", 250, True, False),
]

if __name__ == "__main__":
    print("Household | Units | Ration card | Age > 80 | Separate-if result | Elif result")
    for name, units, card, senior in households:
        print(f"{name:9} | {units:5} | {str(card):11} | {str(senior):8} | "
              f"{', '.join(subsidy_separate(units, card, senior))} | "
              f"{subsidy_elif(units, card, senior)}")
