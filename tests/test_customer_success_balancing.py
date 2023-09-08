import unittest
from customer_success_balancing import customerSuccessBalancingDistribution

class TestCustomerSuccessBalancing(unittest.TestCase):

    def test_case1(self):
        customer_success_levels = [(1, 50), (2, 100), (3, 150), (4, 200)]
        customer_levels = [(1, 20), (2, 30), (3, 35), (4, 40), (5, 60), (6, 80)]
        customer_success_unavailable = [2, 4]
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable)
        self.assertEqual(result, 1)

    def test_case2(self):
        customer_success_levels = [(1, 50), (2, 100), (3, 150)]
        customer_levels = [(1, 20), (2, 30), (3, 35), (4, 40), (5, 60), (6, 80)]
        customer_success_unavailable = [2]
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable)
        self.assertEqual(result, 1)

    def test_case3(self):
        customer_success_levels = [(1, 50), (2, 100), (3, 150)]
        customer_levels = [(1, 20), (2, 30), (3, 35), (4, 40), (5, 60), (6, 80)]
        customer_success_unavailable = []
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable)
        self.assertEqual(result, 1)

    def test_case4(self):
        cs_levels = [(1, 50), (2, 100), (3, 150)]
        customer_levels = [(1, 20), (2, 30), (3, 35), (4, 40), (5, 60), (6, 80)]
        unavailable_cs = [1, 2, 3]
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, 0)

    if __name__ == '__main__':
        unittest.main()