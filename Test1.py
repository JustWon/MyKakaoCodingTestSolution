import unittest
import Quiz1

class KakaoQuiz1Test(unittest.TestCase):

    def test1(self):
        n=5
        arr1 = [9, 20, 28, 18, 11]
        arr2 = [30, 1, 21, 17, 28]

        Quiz1.Quiz1Solver(n, arr1, arr2)

    def test2(self):
        n = 6
        arr1 = [46, 33, 33, 22, 31, 50]
        arr2 = [27, 56, 19, 14, 14, 10]

        Quiz1.Quiz1Solver(n, arr1, arr2)


if __name__=='__main__':
    unittest.main()

