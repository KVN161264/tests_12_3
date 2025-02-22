import unittest
from tests_12_3 import RunnerTest, TournamentTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
