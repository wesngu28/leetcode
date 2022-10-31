class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz_list = []
        num = 1
        while (num <= n):
            fizzbuzz = ''
            if (num % 3 == 0):
                fizzbuzz += 'Fizz'
            if (num % 5 == 0):
                fizzbuzz += 'Buzz'
            if (num % 3 > 0 and num % 5 > 0):
                fizzbuzz += str(num)
            num += 1
            fizz_buzz_list.append(fizzbuzz)
        return fizz_buzz_list