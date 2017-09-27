import unittest
import Quiz2

class KakaoQuiz3Test(unittest.TestCase):

    def test1(self):
        cacheSize = 3
        cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
        print(Quiz2.Quiz2Solver(cacheSize, cities))

    def test2(self):
        cacheSize = 3
        cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
        print(Quiz2.Quiz2Solver(cacheSize, cities))

    def test3(self):
        cacheSize = 2
        cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
        print(Quiz2.Quiz2Solver(cacheSize, cities))

    def test4(self):
        cacheSize = 5
        cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
        print(Quiz2.Quiz2Solver(cacheSize, cities))

    def test5(self):
        cacheSize = 2
        cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
        print(Quiz2.Quiz2Solver(cacheSize, cities))

    def test6(self):
        cacheSize = 0
        cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
        print(Quiz2.Quiz2Solver(cacheSize, cities))

if __name__=='__main__':
    unittest.main()

