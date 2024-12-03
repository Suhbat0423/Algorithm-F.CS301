import unittest

def count_primes(n):
    if n < 2:
        return 0

    count = 0
    for num in range(2, n + 1):  
        a = False
        for i in range(2, num): 
            if (num % i) == 0:  
                a = True
                break
        if not a:  
            count += 1

    return count


class TestPrimeCounting(unittest.TestCase):
    
    def test_count_primes(self):
        self.assertEqual(count_primes(18), 7) 
        self.assertEqual(count_primes(10), 4) 
        self.assertEqual(count_primes(1), 0) 
        self.assertEqual(count_primes(0), 0)  

if __name__ == '__main__':
    unittest.main()
