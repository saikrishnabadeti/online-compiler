

# test_01.py
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")


# # test_02.py
# score = int(input("Score (0-100): "))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# else:
#     grade = 'F'
# print("Grade:", grade)


# # test_03.py
# n = int(input("Count to: "))
# for i in range(1, n+1):
#     print(i, end=' ')
# print()

# # test_04.py
# total = 0
# while True:
#     s = input("Number (or 'q' to quit): ")
#     if s == 'q':
#         break
#     if not s.isdigit():
#         print("Not a digit, ignored.")
#         continue
#     total += int(s)
# print("Sum =", total)


# # test_05.py
# nums = [int(x) for x in input("Space-separated numbers: ").split()]
# print("Original:", nums)
# print("Squares :", [x*x for x in nums])


# # test_06.py
# word = input("Word: ")
# counts = {}
# for ch in word:
#     counts[ch] = counts.get(ch, 0) + 1
# print("Letter counts:", counts)

# # test_07.py
# def greet(name, greeting="Hi"):
#     return f"{greeting}, {name}!"

# def stats(*numbers, op='sum'):
#     if op == 'sum':
#         return sum(numbers)
#     elif op == 'avg':
#         return sum(numbers)/len(numbers) if numbers else 0

# print(greet(input("Name: ")))
# print(stats(1, 2, 3, 4, op='avg'))


# # test_08.py
# def fact(n):
#     return 1 if n <= 1 else n * fact(n-1)

# n = int(input("n! = "))
# print(f"{n}! =", fact(n))

# # test_09.py
# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Division by zero!")
# except ValueError:
#     print("Invalid integer!")

# # test_10.py
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return "???"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# name = input("Dog name: ")
# d = Dog(name)
# print(d.name, "says", d.speak())


# # test_11.py
# import time
# filename = input("File to create: ")
# text = input("Text line: ")
# with open(filename, 'w') as f:
#     f.write(text + '\n')
# time.sleep(2)
# with open(filename) as f:
#     print("Read back:", f.read().strip())

# # test_12.py
# def secret():
#     return "Shhh!"

# if __name__ == "__main__":
#     print("Running directly:", secret())
# else:
#     print("Imported as module")


# # test_13.py
# def fib_upto(n):
#     a, b = 0, 1
#     while a <= n:
#         yield a
#         a, b = b, a + b

# limit = int(input("Fib limit: "))
# print(list(fib_upto(limit)))


# # test_14.py
# class Timer:
#     def __enter__(self):
#         import time
#         self.start = time.time()
#         return self
#     def __exit__(self, *args):
#         import time
#         print("Elapsed:", time.time() - self.start)

# with Timer():
#     _ = input("Press Enter to stop timer...")


# # test_15.py
# nums = [int(x) for x in input("Numbers: ").split()]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# squares = list(map(lambda x: x*x, evens))
# print("Evens squared:", squares)


# # test_16.py
# def timer(func):
#     import time
#     def wrapper(*a, **k):
#         t0 = time.time()
#         res = func(*a, **k)
#         print("Time:", time.time() - t0)
#         return res
#     return wrapper

# @timer
# def slow_square(n):
#     import time
#     time.sleep(0.5)
#     return n*n

# print(slow_square(int(input("n: "))))


# # test_17.py
# try:
#     x = int(input("Number: "))
# except ValueError:
#     print("Bad input")
# else:
#     print("Squared:", x*x)
# finally:
#     print("Done")


# # test_18.py
# while (line := input("Line (empty to quit): ")):
#     print("You typed:", line)
# print("Bye")

# # test_19.py
# from dataclasses import dataclass

# @dataclass
# class Point:
#     x: int
#     y: int

# p = Point(*map(int, input("x y: ").split()))
# print(p)


# # test_20.py
# cmd = input("Command (quit/greet/count): ")
# match cmd.split():
#     case ["quit"]:
#         print("Good-bye")
#     case ["greet", name]:
#         print(f"Hi {name}!")
#     case ["count", *nums]:
#         print("Count:", len(nums))
#     case _:
#         print("Unknown")






# # ------------

# # error_tests.py
# # Comprehensive error-test suite for Python compilers/interpreters
# # Run this file and verify every "ERROR #X" line appears with the correct exception.

# import sys
# from typing import Any

# def test_errors():
#     errors = []

#     # ------------------------------------------------------------
#     # 1. Syntax Errors (these will be caught by parser, not runtime)
#     # ------------------------------------------------------------
#     # Note: Syntax errors cannot be caught at runtime.
#     # Your compiler must report them during parsing/compilation.
#     # Uncomment one at a time to test parser:

#     # errors.append("ERROR #1: SyntaxError - invalid syntax")
#     # if: pass  # missing condition

#     # errors.append("ERROR #2: SyntaxError - unexpected indent")
#     #     x = 1

#     # ------------------------------------------------------------
#     # Runtime Errors (below are executable)
#     # ------------------------------------------------------------

#     # 2. NameError
#     try:
#         print(undefined_variable)
#     except NameError as e:
#         errors.append("ERROR #2: NameError - name 'undefined_variable' is not defined")

#     # 3. TypeError - unsupported operand
#     try:
#         result = "5" + 5
#     except TypeError as e:
#         errors.append("ERROR #3: TypeError - can only concatenate str to str")

#     # 4. ZeroDivisionError
#     try:
#         x = 10 / 0
#     except ZeroDivisionError as e:
#         errors.append("ERROR #4: ZeroDivisionError - division by zero")

#     # 5. IndexError
#     try:
#         lst = [1, 2, 3]
#         print(lst[99])
#     except IndexError as e:
#         errors.append("ERROR #5: IndexError - list index out of range")

#     # 6. KeyError
#     try:
#         d = {'a': 1}
#         print(d['b'])
#     except KeyError as e:
#         errors.append("ERROR #6: KeyError - 'b'")

#     # 7. AttributeError
#     try:
#         x = 42
#         x.append(5)
#     except AttributeError as e:
#         errors.append("ERROR #7: AttributeError - 'int' object has no attribute 'append'")

#     # 8. ImportError / ModuleNotFoundError
#     try:
#         import nonexistent_module_12345
#     except ModuleNotFoundError as e:
#         errors.append("ERROR #8: ModuleNotFoundError - No module named 'nonexistent_module_12345'")

#     # 9. ValueError - invalid literal
#     try:
#         int("abc")
#     except ValueError as e:
#         errors.append("ERROR #9: ValueError - invalid literal for int() with base 10: 'abc'")

#     # 10. OverflowError (very large exponent)
#     try:
#         x = 2 ** 999999
#     except OverflowError as e:
#         errors.append("ERROR #10: OverflowError - int too large to convert to float")
#     except RecursionError:
#         errors.append("ERROR #10: RecursionError - too deep (fallback if pow overflows recursion)")

#     # 11. FileNotFoundError
#     try:
#         with open("nonexistent_file.txt") as f:
#             pass
#     except FileNotFoundError as e:
#         errors.append("ERROR #11: FileNotFoundError - No  No such file or directory: 'nonexistent_file.txt'")

#     # 12. PermissionError
#     try:
#         with open("/root/secret.txt", "w") as f:
#             pass
#     except PermissionError as e:
#         errors.append("ERROR #12: PermissionError - [Errno 13] Permission denied")
#     except FileNotFoundError:
#         errors.append("ERROR #12: FileNotFoundError - /root not accessible (fallback)")

#     # 13. UnicodeDecodeError
#     try:
#         with open(__file__, 'r', encoding='ascii') as f:
#             f.read()
#     except UnicodeDecodeError as e:
#         errors.append("ERROR #13: UnicodeDecodeError - 'ascii' codec can't decode byte")

#     # 14. IndentationError (runtime? No — but some compilers delay it)
#     # This is a SyntaxError — skip in runtime test

#     # 15. TabError (inconsistent tabs/spaces)
#     # Also SyntaxError — skip

#     # 16. StopIteration
#     try:
#         it = iter([1, 2])
#         next(it)
#         next(it)
#         next(it)
#     except StopIteration as e:
#         errors.append("ERROR #16: StopIteration - (raised by next())")

#     # 17. GeneratorExit
#     def gen():
#         try:
#             yield 1
#         except GeneratorExit:
#             errors.append("ERROR #17: GeneratorExit - generator closed")
#             raise
#     try:
#         g = gen()
#         next(g)
#         g.close()
#     except GeneratorExit:
#         pass  # already caught inside

#     # 18. KeyboardInterrupt
#     # Cannot reliably trigger in script — skip or simulate
#     errors.append("ERROR #18: KeyboardInterrupt - (simulate with Ctrl+C in interactive)")

#     # 19. SystemExit
#     try:
#         sys.exit(1)
#     except SystemExit as e:
#         errors.append(f"ERROR #19: SystemExit - code {e.code}")

#     # 20. RecursionError
#     try:
#         def rec():
#             rec()
#         rec()
#     except RecursionError as e:
#         errors.append("ERROR #20: RecursionError - maximum recursion depth exceeded")

#     # 21. MemoryError (simulate with huge list)
#     try:
#         x = [0] * (10**9)
#     except MemoryError as e:
#         errors.append("ERROR #21: MemoryError - cannot allocate memory")
#     except OverflowError:
#         errors.append("ERROR #21: OverflowError - too large for list (fallback)")

#     # 22. AssertionError
#     try:
#         assert False, "Custom assert message"
#     except AssertionError as e:
#         errors.append("ERROR #22: AssertionError - Custom assert message")

#     # 23. LookupError (parent of Index/Key)
#     try:
#         raise LookupError("test")
#     except LookupError as e:
#         errors.append("ERROR #23: LookupError - test")

#     # 24. RuntimeError
#     try:
#         raise RuntimeError("Something went wrong")
#     except RuntimeError as e:
#         errors.append("ERROR #24: RuntimeError - Something went wrong")

#     # 25. NotImplementedError
#     try:
#         raise NotImplementedError("Feature not ready")
#     except NotImplementedError as e:
#         errors.append("ERROR #25: NotImplementedError - Feature not ready")

#     # 26. SyntaxError in exec()
#     try:
#         exec("if: pass")
#     except SyntaxError as e:
#         errors.append("ERROR #26: SyntaxError - invalid syntax (in exec)")

#     # 27. IndentationError in exec()
#     try:
#         exec("  if True:\n    pass\n  pass")
#     except IndentationError as e:
#         errors.append("ERROR #27: IndentationError - unexpected indent (in exec)")

#     # 28. TypeError - too many args
#     try:
#         print("a", "b", end="c", extra=1)
#     except TypeError as e:
#         errors.append("ERROR #28: TypeError - print() got an unexpected keyword argument 'extra'")

#     # 29. UnboundLocalError
#     try:
#         def func():
#             print(var)
#             var = 1
#         func()
#     except UnboundLocalError as e:
#         errors.append("ERROR #29: UnboundLocalError - local variable 'var' referenced before assignment")

#     # 30. ImportError (from module import bad)
#     try:
#         from math import nonexistent_function
#     except ImportError as e:
#         errors.append("ERROR #30: ImportError - cannot import name 'nonexistent_function' from 'math'")

#     # 31. OSError (generic)
#     try:
#         import os
#         os.listdir("/nonexistent_directory_12345")
#     except OSError as e:
#         errors.append("ERROR #31: OSError - No such file or directory")

#     # 32. BlockingIOError
#     # Hard to trigger reliably — skip or simulate
#     errors.append("ERROR #32: BlockingIOError - (requires non-blocking I/O)")

#     # 33. ChildProcessError, TimeoutError, etc. — advanced
#     errors.append("ERROR #33: Advanced OS errors - test separately with subprocess")

#     # ------------------------------------------------------------
#     # Final Output
#     # ------------------------------------------------------------
#     print("\n=== ERROR TEST RESULTS ===")
#     for err in errors:
#         print(err)
#     print(f"\nTotal errors triggered: {len(errors)}")
#     print("If you see all ERROR # lines above, your compiler handles exceptions correctly!")

# if __name__ == "__main__":
#     test_errors()

# # -------------



# #---------------------------
# # infinite loop
# #---------------------------
# print("Infinite loop starting...")
# while True:
#     pass
# print("Loop ends")

# #---------------------------

# #---------------------------



