import unittest

from matcher import Matcher


class TestMatcher(unittest.TestCase):
    def test_case_01(self):
        case = ['3',
                'E H R A D W Q C T P',
                'E G U D A M C P V B',
                'E H R D A Q W C T M']

        result = Matcher().get_couples(case)
        result.sort()
        self.assertEqual(['1-3'], result)

    def test_case_02(self):
        case = ['3',
                'A B C D E F G H I J',
                'A B C D E F G H I J',
                'A B C D E F G H I J']

        expect = ['1-2', '1-3', '2-3']
        expect.sort()
        result = Matcher().get_couples(case)
        result.sort()

        self.assertEqual(expect, result)

    def test_case_100(self):
        file = open('./resources/100.txt', 'r')
        case = file.readlines()
        file.close()

        expect = ['21-76', '29-52', '44-64', '77-81']
        expect.sort()

        result = Matcher().get_couples(case)
        result.sort()

        self.assertEqual(expect, result)

    def test_case_10000(self):
        file = open('./resources/10000.txt', 'r')
        case = file.readlines()
        file.close()

        expect = ['1401-4203', '1868-8699', '2641-7764', '3232-4304', '333-7189'
                  , '3459-5726', '3921-7107', '4192-8575', '496-8710']
        expect.sort()
        result = Matcher().get_couples(case)
        result.sort()

        self.assertListEqual(expect, result)
