import unittest

def assign_bicycles(a, b):
    n = len(a)
    m = len(b)
    
    calA = [-1] * n
    calB = [False] * m
    
    for indS in range(n):
        closest = -1
        minZai = float('inf')
        
        for bIndex in range(m):
            zai = abs(a[indS][0] - b[bIndex][0]) + abs(a[indS][1] - b[bIndex][1])
            
            if zai < minZai or (zai == minZai and bIndex < closest):
                minZai = zai
                closest = bIndex
        
        calA[indS] = closest
        calB[closest] = True
    
    return calA

class TestAssignBicycles(unittest.TestCase):

    def test_case_2(self):
        a = [(0, 0), (1, 1), (2, 2)]
        b = [(0, 1), (4, 3), (2, 1), (1, 1)]
        expected_output = [0, 3, 2]
        self.assertEqual(assign_bicycles(a, b), expected_output)

    def test_case_3(self):
        a = [(0, 0)]
        b = [(2, 2), (3, 3)]
        expected_output = [0]
        self.assertEqual(assign_bicycles(a, b), expected_output)

    def test_case_4(self):
        a = [(0, 0), (2, 2)]
        b = [(0, 1), (1, 1)]
        expected_output = [0, 1]
        self.assertEqual(assign_bicycles(a, b), expected_output)

if __name__ == '__main__':
    unittest.main()
