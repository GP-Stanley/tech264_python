import sys

# Check for arguments
if len(sys.argv) > 1:  # If more than one argument is passed (including the script name)
    print("You gave me an argument.")
    print("Print argument with index 0 (the script name):")
    print(sys.argv[0])  # This prints the script name
    print("Print argument with index 1 (the first passed argument):")
    print(sys.argv[1])  # This prints the first actual argument (e.g., 'hello')
else:
    print("You gave me no argument.")
    print("Print argument with index 0 (the script name):")
    print(sys.argv[0])  # This prints the script name when no other arguments are given


# FIRST OUTPUT:
# You gave me no argument.
# Print argument with index 0
# .\test_for_args.py

# WITH [1] ARGUMENT (HELLO):
# You gave me an argument.
# Print argument with index 0 (the script name):
# .\test_for_args.py
# Print argument with index 1 (the first passed argument):
# hello


