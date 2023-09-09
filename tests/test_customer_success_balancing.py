import unittest
from customer_success_balancing import customerSuccessBalancingDistribution

class TestCustomerSuccessBalancing(unittest.TestCase):
    def test_case_one(self):
        customer_success_levels = [
            {"ID": 1, "Score": 50},
            {"ID": 2, "Score": 100},
            {"ID": 3, "Score": 150},
            {"ID": 4, "Score": 200}
        ]
        customer_levels = [
            {"ID": 1, "Score": 20},
            {"ID": 2, "Score": 30},
            {"ID": 3, "Score": 35},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 80}
        ]
        customer_success_unavailable = [2, 4]
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable)
        self.assertEqual(result, 1)

    def test_case_two(self):
        customer_success_levels = [
            {"ID": 1, "Score": 50},
            {"ID": 2, "Score": 100},
            {"ID": 3, "Score": 150}
        ]
        customer_levels = [
            {"ID": 1, "Score": 20},
            {"ID": 2, "Score": 30},
            {"ID": 3, "Score": 35},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 80}
        ]
        customer_success_unavailable = [2]
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable)
        self.assertEqual(result, 1)

    def test_case_three(self):
        customer_success_levels = [
            {"ID": 1, "Score": 50},
            {"ID": 2, "Score": 100},
            {"ID": 3, "Score": 150}
        ]
        customer_levels = [
            {"ID": 1, "Score": 20},
            {"ID": 2, "Score": 30},
            {"ID": 3, "Score": 35},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 80}
        ]
        customer_success_unavailable = []
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels, customer_success_unavailable)
        self.assertEqual(result, 1)

    def test_case_four(self):
        cs_levels = [
            {"ID": 1, "Score": 50},
            {"ID": 2, "Score": 100},
            {"ID": 3, "Score": 150}
        ]
        customer_levels = [
            {"ID": 1, "Score": 20},
            {"ID": 2, "Score": 30},
            {"ID": 3, "Score": 35},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 80}
        ]
        unavailable_cs = [1, 2, 3]
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, 0)

    def test_case_five(self):
        customer_success_levels = [
            {"ID": 1, "Score": 60},
            {"ID": 2, "Score": 20},
            {"ID": 3, "Score": 95},
            {"ID": 4, "Score": 75}
        ]
        customer_levels = [
            {"ID": 1, "Score": 90},
            {"ID": 2, "Score": 20},
            {"ID": 3, "Score": 70},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 10}
        ]
        customer_success_unavailable = [2, 4]

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(1, result)

    def test_case_six(self):
        customer_success_levels = [
            {"ID": 1, "Score": 11},
            {"ID": 2, "Score": 21},
            {"ID": 3, "Score": 31},
            {"ID": 4, "Score": 3},
            {"ID": 5, "Score": 4},
            {"ID": 6, "Score": 5}
        ]
        customer_levels = [
            {"ID": 1, "Score": 10},
            {"ID": 2, "Score": 10},
            {"ID": 3, "Score": 10},
            {"ID": 4, "Score": 20},
            {"ID": 5, "Score": 20},
            {"ID": 6, "Score": 30},
            {"ID": 7, "Score": 30},
            {"ID": 8, "Score": 30},
            {"ID": 9, "Score": 20},
            {"ID": 10, "Score": 60}
        ]
        customer_success_unavailable = []

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(0, result)

    def test_case_seven(self):
        customer_success_levels = [{"ID": i, "Score": i} for i in range(1, 1000)]
        customer_levels = [{"ID": i, "Score": 998} for i in range(1, 10001)]
        customer_success_unavailable = [999]

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(998, result)

    def test_case_eight(self):
        customer_success_levels = [
            {"ID": 1, "Score": 1},
            {"ID": 2, "Score": 2},
            {"ID": 3, "Score": 3},
            {"ID": 4, "Score": 4},
            {"ID": 5, "Score": 5},
            {"ID": 6, "Score": 6}
        ]
        customer_levels = [
            {"ID": 1, "Score": 10},
            {"ID": 2, "Score": 10},
            {"ID": 3, "Score": 10},
            {"ID": 4, "Score": 20},
            {"ID": 5, "Score": 20},
            {"ID": 6, "Score": 30},
            {"ID": 7, "Score": 30},
            {"ID": 8, "Score": 30},
            {"ID": 9, "Score": 20},
            {"ID": 10, "Score": 60}
        ]
        customer_success_unavailable = []

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(0, result)

    def test_case_nine(self):
        customer_success_levels = [
            {"ID": 1, "Score": 100},
            {"ID": 2, "Score": 2},
            {"ID": 3, "Score": 3},
            {"ID": 4, "Score": 6},
            {"ID": 5, "Score": 4},
            {"ID": 6, "Score": 5}
        ]
        customer_levels = [
            {"ID": 1, "Score": 10},
            {"ID": 2, "Score": 10},
            {"ID": 3, "Score": 10},
            {"ID": 4, "Score": 20},
            {"ID": 5, "Score": 20},
            {"ID": 6, "Score": 30},
            {"ID": 7, "Score": 30},
            {"ID": 8, "Score": 30},
            {"ID": 9, "Score": 20},
            {"ID": 10, "Score": 60}
        ]
        customer_success_unavailable = []

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(1, result)

    def test_case_ten(self):
        customer_success_levels = [
            {"ID": 1, "Score": 100},
            {"ID": 2, "Score": 99},
            {"ID": 3, "Score": 88},
            {"ID": 4, "Score": 3},
            {"ID": 5, "Score": 4},
            {"ID": 6, "Score": 5}
        ]
        customer_levels = [
            {"ID": 1, "Score": 10},
            {"ID": 2, "Score": 10},
            {"ID": 3, "Score": 10},
            {"ID": 4, "Score": 20},
            {"ID": 5, "Score": 20},
            {"ID": 6, "Score": 30},
            {"ID": 7, "Score": 30},
            {"ID": 8, "Score": 30},
            {"ID": 9, "Score": 20},
            {"ID": 10, "Score": 60}
        ]
        customer_success_unavailable = [1, 3, 2]

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(0, result)

    def test_case_eleven(self):
        customer_success_levels = [
            {"ID": 1, "Score": 100},
            {"ID": 2, "Score": 99},
            {"ID": 3, "Score": 88},
            {"ID": 4, "Score": 3},
            {"ID": 5, "Score": 4},
            {"ID": 6, "Score": 5}
        ]
        customer_levels = [
            {"ID": 1, "Score": 10},
            {"ID": 2, "Score": 10},
            {"ID": 3, "Score": 10},
            {"ID": 4, "Score": 20},
            {"ID": 5, "Score": 20},
            {"ID": 6, "Score": 30},
            {"ID": 7, "Score": 30},
            {"ID": 8, "Score": 30},
            {"ID": 9, "Score": 20},
            {"ID": 10, "Score": 60}
        ]
        customer_success_unavailable = [4, 5, 6]

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(3, result)

    def test_case_twelve(self):
        customer_success_levels = [
            {"ID": 1, "Score": 60},
            {"ID": 2, "Score": 40},
            {"ID": 3, "Score": 95},
            {"ID": 4, "Score": 75}
        ]
        customer_levels = [
            {"ID": 1, "Score": 90},
            {"ID": 2, "Score": 70},
            {"ID": 3, "Score": 20},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 10}
        ]
        customer_success_unavailable = [2, 4]

        result = customerSuccessBalancingDistribution(
            customer_success_levels, customer_levels, customer_success_unavailable
        )
        self.assertEqual(1, result)

    if __name__ == '__main__':
        unittest.main()