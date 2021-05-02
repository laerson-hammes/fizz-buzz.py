def main(n: int = 101, /) -> None:
   for number in range(1, n):
      if number % 15 == 0:
         print("FizzBuzz")
      elif number % 3 == 0:
         print("Fizz")
      elif number % 5 == 0:
         print("Buzz")
      else:
         print(number)
      

if __name__ == "__main__":
   main()