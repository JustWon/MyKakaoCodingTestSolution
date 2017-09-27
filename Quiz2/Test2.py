import unittest
import Quiz2

class KakaoQuiz2Test(unittest.TestCase):

    def test1(self):
        print(Quiz2.Quiz2Solver('1S2D*3T'))

    def test2(self):
        print(Quiz2.Quiz2Solver('1D2S#10S'))

    def test3(self):
        print(Quiz2.Quiz2Solver('1D2S0T'))

    def test4(self):
        print(Quiz2.Quiz2Solver('1S*2T*3S'))

    def test5(self):
        print(Quiz2.Quiz2Solver('1D#2S*3S'))

    def test6(self):
        print(Quiz2.Quiz2Solver('1T2D3D#'))

    def test7(self):
        print(Quiz2.Quiz2Solver('1D2S3T*'))


if __name__=='__main__':
    unittest.main()

