import unittest
from customer_success_balancing import customerSuccessBalancingDistribution
from customer_success_balancing import map_entities
from customer_success_balancing import array_seq
from customer_success_balancing import build_size_entities
import datetime


class TestCustomerSuccessBalancing(unittest.TestCase):
    def test_scenario_1(self):
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
        expected = 1
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels,
                                                      customer_success_unavailable)
        self.assertEqual(result, expected)

    def test_scenario_2(self):
        cs_levels = [
            {"ID": 11, "Score": 60},
            {"ID": 21, "Score": 20},
            {"ID": 31, "Score": 95},
            {"ID": 3, "Score": 75},
            {"ID": 4, "Score": 10},
            {"ID": 5, "Score": 30}
        ]
        customer_levels = [
            {"ID": 10, "Score": 10},
            {"ID": 10, "Score": 10},
            {"ID": 10, "Score": 10},
            {"ID": 20, "Score": 20},
            {"ID": 20, "Score": 20},
            {"ID": 30, "Score": 30},
            {"ID": 30, "Score": 30},
            {"ID": 30, "Score": 30},
            {"ID": 20, "Score": 20},
            {"ID": 60, "Score": 60}
        ]
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_3(self):
        cs_levels = [
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
        unavailable_cs = [2, 4]
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_4(self):
        cs_levels = [
            {"ID": 11, "Score": 60},
            {"ID": 21, "Score": 20},
            {"ID": 31, "Score": 95},
            {"ID": 3, "Score": 75},
            {"ID": 4, "Score": 10},
            {"ID": 5, "Score": 30}
        ]
        customer_levels = [
            {"ID": 10, "Score": 10},
            {"ID": 10, "Score": 10},
            {"ID": 10, "Score": 10},
            {"ID": 20, "Score": 20},
            {"ID": 20, "Score": 20},
            {"ID": 30, "Score": 30},
            {"ID": 30, "Score": 30},
            {"ID": 30, "Score": 30},
            {"ID": 20, "Score": 20},
            {"ID": 60, "Score": 60}
        ]
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_5(self):
        cs_levels = [{"ID": i, "Score": i} for i in range(1, 999)]
        customer_levels = [{"ID": i, "Score": 998} for i in range(1, 100001)]
        unavailable_cs = [999]
        expected = 998
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_6(self):
        cs_levels = [{"ID": i, "Score": i} for i in range(1, 7)]
        customer_levels = [{"ID": i, "Score": i} for i in range(1, 11)]
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_7(self):
        cs_levels = [{"ID": 100, "Score": 100}, {"ID": 2, "Score": 2}, {"ID": 3, "Score": 3},
                     {"ID": 6, "Score": 6}, {"ID": 4, "Score": 4}, {"ID": 5, "Score": 5}]
        customer_levels = [{"ID": i, "Score": i} for i in range(1, 11)]
        unavailable_cs = []
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_8(self):
        cs_levels = [{"ID": 100, "Score": 100}, {"ID": 99, "Score": 99}, {"ID": 88, "Score": 88},
                     {"ID": 3, "Score": 3}, {"ID": 4, "Score": 4}, {"ID": 5, "Score": 5}]
        customer_levels = [{"ID": i, "Score": i} for i in range(1, 11)]
        unavailable_cs = [1, 3, 2]
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_9(self):
        cs_levels = [{"ID": 100, "Score": 100}, {"ID": 99, "Score": 99}, {"ID": 88, "Score": 88},
                     {"ID": 3, "Score": 3}, {"ID": 4, "Score": 4}, {"ID": 5, "Score": 5}]
        customer_levels = [{"ID": i, "Score": i} for i in range(1, 11)]
        unavailable_cs = [4, 5, 6]
        expected = 3
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_10(self):
        cs_levels = [{"ID": 60, "Score": 60}, {"ID": 40, "Score": 40}, {"ID": 95, "Score": 95}, {"ID": 75, "Score": 75}]
        customer_levels = [{"ID": 90, "Score": 90}, {"ID": 70, "Score": 70}, {"ID": 20, "Score": 20},
                           {"ID": 40, "Score": 40}, {"ID": 60, "Score": 60}, {"ID": 10, "Score": 10}]
        unavailable_cs = [2, 4]
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_11(self):
        cs_levels = [
            {"ID": 1, "Score": 60},
            {"ID": 2, "Score": 20},
            {"ID": 3, "Score": 95},
            {"ID": 4, "Score": 75},
        ]
        customer_levels = [
            {"ID": 1, "Score": 90},
            {"ID": 2, "Score": 20},
            {"ID": 3, "Score": 70},
            {"ID": 4, "Score": 40},
            {"ID": 5, "Score": 60},
            {"ID": 6, "Score": 10},
        ]
        unavailable_cs = [2, 4]
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_12(self):
        cs_levels = map_entities([11, 21, 31, 3, 4, 5])
        customer_levels = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_13(self):
        test_timeout_in_ms = 100
        test_start_time = datetime.datetime.now()

        cs_levels = map_entities(array_seq(999, 1))
        customer_levels = build_size_entities(10000, 998)
        unavailable_cs = [999]
        expected = 998
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

        if datetime.datetime.now() - test_start_time > test_timeout_in_ms / 1000:
            raise Exception(f"Test took longer than {test_timeout_in_ms}ms!")

    def test_scenario_14(self):
        cs_levels = map_entities([1, 2, 3, 4, 5, 6])
        customer_levels = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_15(self):
        cs_levels = map_entities([100, 2, 3, 6, 4, 5])
        customer_levels = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        unavailable_cs = []
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_16(self):
        cs_levels = map_entities([100, 99, 88, 3, 4, 5])
        customer_levels = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        unavailable_cs = [1, 3, 2]
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_17(self):
        cs_levels = map_entities([100, 99, 88, 3, 4, 5])
        customer_levels = map_entities([10, 10, 10, 20, 20, 30, 30, 30, 20, 60])
        unavailable_cs = [4, 5, 6]
        expected = 3
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_18(self):
        cs_levels = map_entities([60, 40, 95, 75])
        customer_levels = map_entities([90, 70, 20, 40, 60, 10])
        unavailable_cs = [2, 4]
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        assert result == expected

    def test_scenario_19(self):
        customer_success_levels = [
            {"ID": 60, "Score": 60},
            {"ID": 20, "Score": 20},
            {"ID": 95, "Score": 95},
            {"ID": 75, "Score": 75}
        ]
        customer_levels = [
            {"ID": 90, "Score": 90},
            {"ID": 20, "Score": 20},
            {"ID": 70, "Score": 70},
            {"ID": 40, "Score": 40},
            {"ID": 60, "Score": 60},
            {"ID": 10, "Score": 10}
        ]
        customer_success_unavailable = [2, 4]
        expected = 1
        result = customerSuccessBalancingDistribution(customer_success_levels, customer_levels,
                                                      customer_success_unavailable)
        self.assertEqual(result, expected)

    def test_scenario_20(self):
        cs_levels = [
            {"ID": 11, "Score": 60},
            {"ID": 21, "Score": 20},
            {"ID": 31, "Score": 95},
            {"ID": 3, "Score": 75},
            {"ID": 4, "Score": 10},
            {"ID": 5, "Score": 30}
        ]
        customer_levels = [
            {"ID": 10, "Score": 10},
            {"ID": 10, "Score": 10},
            {"ID": 10, "Score": 10},
            {"ID": 20, "Score": 20},
            {"ID": 20, "Score": 20},
            {"ID": 30, "Score": 30},
            {"ID": 30, "Score": 30},
            {"ID": 30, "Score": 30},
            {"ID": 20, "Score": 20},
            {"ID": 60, "Score": 60}
        ]
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_21(self):
        cs_levels = [{"ID": i, "Score": i} for i in range(1, 1000)]
        customer_levels = [{"ID": i, "Score": 998} for i in range(1, 10001)]
        unavailable_cs = [999]
        expected = 998
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_22(self):
        cs_levels = [
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
        unavailable_cs = []
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_23(self):
        cs_levels = [
            {"ID": 100, "Score": 100},
            {"ID": 2, "Score": 2},
            {"ID": 3, "Score": 3},
            {"ID": 6, "Score": 6},
            {"ID": 4, "Score": 4},
            {"ID": 5, "Score": 5}
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
        unavailable_cs = []
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_24(self):
        cs_levels = [
            {"ID": 100, "Score": 100},
            {"ID": 99, "Score": 99},
            {"ID": 88, "Score": 88},
            {"ID": 3, "Score": 3},
            {"ID": 4, "Score": 4},
            {"ID": 5, "Score": 5}
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
        unavailable_cs = [1, 3, 2]
        expected = 0
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_25(self):
        cs_levels = [
            {"ID": 100, "Score": 100},
            {"ID": 99, "Score": 99},
            {"ID": 88, "Score": 88},
            {"ID": 3, "Score": 3},
            {"ID": 4, "Score": 4},
            {"ID": 5, "Score": 5}
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
        unavailable_cs = [4, 5, 6]
        expected = 3
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    def test_scenario_26(self):
        cs_levels = [
            {"ID": 60, "Score": 60},
            {"ID": 40, "Score": 40},
            {"ID": 95, "Score": 95},
            {"ID": 75, "Score": 75}
        ]
        customer_levels = [
            {"ID": 90, "Score": 90},
            {"ID": 70, "Score": 70},
            {"ID": 20, "Score": 20},
            {"ID": 40, "Score": 40},
            {"ID": 60, "Score": 60},
            {"ID": 10, "Score": 10}
        ]
        unavailable_cs = [2, 4]
        expected = 1
        result = customerSuccessBalancingDistribution(cs_levels, customer_levels, unavailable_cs)
        self.assertEqual(result, expected)

    if __name__ == '__main__':
        unittest.main()
