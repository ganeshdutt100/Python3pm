row = 5

for i in range(row , 0 , -1 ):
    for j in range(i):
        print( j, end="")
    print('')

    # 1234
    # 123
    # 12
    # 1

# rows = 5
# for i in range(1, rows + 1):
#  print(" " * (rows - i) + "*" * (2 * i - 1))


# row  = 5
# for i in range( 1,row +1):
#     for j in range(row - i):
#         print(" ", end="")
#         for j in range(i):
#             print("* ", end="")
#         print()

# row = 5
# for i in range(1, row + 1):
#     for j in range(row - i):
#         print(" ", end="")  # Printing leading spaces
#     for j in range(i):  
#         print("* ", end="")  # Printing stars with spaces
#     print()  # Newline after each row
