
def customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable):
    if not customer_success_levels or not customer_levels:
        return 0

    available_cs = [cs for cs in customer_success_levels if cs[0] not in customer_success_unavailable]

    if not available_cs:
        return 0

    cs_customers_count = {cs[0]: 0 for cs in available_cs}

    for customer in customer_levels:
        closest_cs = min(available_cs, key=lambda cs: abs(cs[1] - customer[1]))
        cs_customers_count[closest_cs[0]] += 1

    max_customers = max(cs_customers_count.values())
    best_cs = [cs for cs, count in cs_customers_count.items() if count == max_customers]

    if len(best_cs) == 1:
        return best_cs[0]
    else:
        return 0

