households = [
    ("A", 100, False, False),
    ("B", 101, True, False),
    ("C", 101, False, False),
    ("D", 200, True, False),
    ("E", 200, False, False),
    ("F", 201, False, True),
    ("G", 201, True, False),
    ("H", 80, True, True),
]


def separate_ifs(units, ration_card, elderly_member):
    results = []
    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")
    if units > 200 and elderly_member:
        results.append("Elderly exception subsidy")
    if not results:
        results.append("No subsidy")
    return results


def if_elif_else(units, ration_card, elderly_member):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200 and ration_card:
        return "Partial subsidy"
    elif units > 200 and elderly_member:
        return "Elderly exception subsidy"
    else:
        return "No subsidy"


for name, units, ration_card, elderly_member in households:
    separate_result = separate_ifs(units, ration_card, elderly_member)
    combined_result = if_elif_else(units, ration_card, elderly_member)
    print(
        f"{name}: {units} units, ration card={ration_card}, "
        f"elderly={elderly_member} -> {separate_result} | {combined_result}"
    )


print("Both implementations agree:", all(
    separate_ifs(units, ration_card, elderly_member) == [if_elif_else(
        units, ration_card, elderly_member
    )]
    for _, units, ration_card, elderly_member in households
))
