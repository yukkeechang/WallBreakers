class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = [None]*n
        i = 1
        while i <= n :
            if i%5 == 0 and i%3 == 0 :
                l[i-1] = "FizzBuzz"
            elif i%5 == 0 :
                l[i-1] = "Buzz"
            elif i%3 == 0 :
                l[i-1] = "Fizz"
            else :
                l[i-1] = str(i)
            print(i)
            i += 1
        return l
            
