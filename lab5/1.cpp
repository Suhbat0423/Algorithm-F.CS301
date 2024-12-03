#include <iostream>
#include <vector>

int fibonacci(int n) {
    std::vector<int> cache(n + 1, -1);
    cache[0] = 0;
    cache[1] = 1;

    for (int i = 2; i <= n; ++i) {
        cache[i] = cache[i - 1] + cache[i - 2];
    }

    return cache[n];
}

int main() {
    int n = 10; // Test Fibonacci number for n = 10
    std::cout << "Fibonacci number at position " << n << " is " << fibonacci(n) << std::endl;
    return 0;
}
