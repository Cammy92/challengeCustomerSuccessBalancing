def customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable):
    if not customer_success_levels or not customer_levels:
        return 0

    available_cs = filter_unavailable_cs(customer_success_levels, customer_success_unavailable)

    if not available_cs:
        return 0

    cs_customers_count = count_customers_per_cs(available_cs, customer_levels)

    if not cs_customers_count or all(count == 0 for count in cs_customers_count.values()):
        return 0

    return find_best_customer_success(cs_customers_count)


def filter_unavailable_cs(customer_success_levels, customer_success_unavailable):
    unavailable_ids = set(customer_success_unavailable)
    return [cs for cs in customer_success_levels if cs["ID"] not in unavailable_ids]

def count_customers_per_cs(available_cs, customer_levels):
    cs_customers_count = {cs["ID"]: 0 for cs in available_cs}

    for customer in customer_levels:
        closest_cs = find_closest_cs(available_cs, customer["Score"])
        if closest_cs:
            cs_customers_count[closest_cs["ID"]] += 1

    return cs_customers_count


def find_closest_cs(available_cs, customer_level):
    return min(available_cs, key=lambda cs: abs(cs["Score"] - customer_level))

def find_best_customer_success(cs_customers_count):
    max_customers = max(cs_customers_count.values())
    best_cs = [cs for cs, count in cs_customers_count.items() if count == max_customers]

    return best_cs[0] if len(best_cs) == 1 else 0
