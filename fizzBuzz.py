# for n in range(1, 101):
#   if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
#   elif n % 5 == 0:
#     print("Buzz")
#   elif n % 3 == 0:
#     print("Fizz")
#   else:
#     print(n)

class fizzBuzz():
    def fizz(self, maxno):
        no = 1
        ans = []
        #maxno = 15
        while no <= maxno:
            if no % 3 == 0 and no % 5 == 0:
                ans.append("FizzBuzz")
                print("FizzBuzz")
            elif no % 3 == 0: 
                ans.append("Fizz")
                print("Fizz")
            elif no % 5 == 0:
                ans.append("Buzz")
                print("Buzz")
            else:
                ans.append(no)
                print(no)
            no += 1
        print(ans)
        return ans

x = fizzBuzz().fizz(maxno=100)
