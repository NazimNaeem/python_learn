import argparse

# Introducing Positional arguments

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print(args.square**2)

# Introducing Optional arguments

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")

# Short options

# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# Combining Positional and Optional arguments

# Example 1
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print("the square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)

# Example 2

# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity:
#     print("the square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)

# Conflicting options

# parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# args = parser.parse_args()
# answer = args.x**args.y

# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# else:
#     print("{}^{} == {}".format(args.x, args.y, answer))


# Multiple values for single parameter

# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     nargs=2,type=int)
# args = parser.parse_args()
# print(type(args.verbose))
# if args.verbose == '1':
#     print("verbosity turned on 1")
# elif args.verbose == 2:
# 	print("verbosity turned on 2")


