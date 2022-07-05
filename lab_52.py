def check_baggage(baggage_weight):
    if 0 <= baggage_weight <= 40:
        return True
    return False


def check_immigration(expiry_date):
    if 2030 <= expiry_date <= 2050:
        return True
    return False


def check_security(noc_status):
    str1 = "valid"
    str2 = "VALID"
    if (noc_status == str1) or (noc_status == str2):
        return True
    return False


def traveler():
    print("Variable    \t    Value")
    traveler_id = int(input("traveler_id     \t"))
    traveler_name = input("traveler_name     \t")
    bag = int(input("baggage_weight    \t"))
    exp = int(input("expiry_year     \t"))
    noc = input("noc_status       \t")
    print("\n")
    if (check_baggage(bag) is True) and (check_immigration(exp) is True) and (check_security(noc) is True):
        print(traveler_id, "\t", traveler_name)
        print("Allow Traveler to fly!")
    else:
        print(traveler_id, "\t", traveler_name)
        print("Detain Traveler for Re-checking!")


traveler()
