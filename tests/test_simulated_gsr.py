import unittest
from prototype.simulated_gsr import generate


class SyntheticDataTest(unittest.TestCase):
    def test_count_and_sequence(self):
        rows = list(generate(20, 4))
        self.assertEqual(len(rows), 80)
        self.assertEqual([r["seq"] for r in rows], list(range(80)))

    def test_deterministic(self):
        self.assertEqual(list(generate(10, 4)), list(generate(10, 4)))

    def test_contact_flag(self):
        rows = list(generate(20, 4))
        lost = [r for r in rows if r["quality"] == "contact_lost"]
        self.assertGreater(len(lost), 0)
        self.assertTrue(all(r["eda_uS"] == "" for r in lost))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            list(generate(0, 4))


if __name__ == "__main__":
    unittest.main()
