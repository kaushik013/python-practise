

#//! pattern programing

# a = int(input('enter the count : '))

# for i in range(1,a+1):
#     print('*',end=' ')
# print()

# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ 



# a = int(input('enter the count : '))

# for i in range(1,a+1):
#     for j in range(1,a+1):
#         print('⭐️',end=' ')
#     print()

# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ 
# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ 
# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ 
# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ 
# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ 
# ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️



# a = 2
# b = 3

# for i in range(1,a+1):
#     for j in range(1,b+1):
#         print('⭐️',end=' ')
#     print()

# ⭐️ ⭐️ ⭐️ 
# ⭐️ ⭐️ ⭐️


#//! primary diagnal

# for i in range(1,6):
#     for j in range(1,6):
#         if(i == j):
#             print('@',end=' ')
#         elif(i > j):
#             print('⭐️',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# @         
# ⭐️ @       
# ⭐️ ⭐️ @     
# ⭐️ ⭐️ ⭐️ @   
# ⭐️ ⭐️ ⭐️ ⭐️ @ 


#//! primary diagnal

# for i in range(1,6):
#     for j in range(1,6):
#         if(i == j):
#             print('@',end=' ')
#         elif(i < j):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# @ * * * * 
#   @ * * * 
#     @ * * 
#       @ * 
#         @ 


#//! primary diagnal

# for i in range(1,6):
#     for j in range(1,6):
#         if(i == j or i < j):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 


#//! primary diagnal

# for i in range(1,5):
#     for j in range(1,5):
#         if(i == j):
#             print('@',end='  ')
#         elif(i > j):
#             print('#',end='  ')
#         else:
#             print('*',end='  ')
#     print()

# --> @ * * * 
# --> # @ * * 
# --> # # @ * 
# --> # # # @ 


#//! primary diagnal

# for i in range(1,6):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 


# or 

#//! primary diagnal

# for i in range(1,6):
#     for j in range(i):
#         if(i == j or i > j):
#             print(i, end=' ')
#     print()

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 



#//! primary diagnal

# for i in range(1,6):
#     for j in range(1,6):
#         if(i == j):
#             print(1,end=' ')
#         elif(i < j):
#             print(0,end=' ')
#         else:
#             print(' ',end=' ')
    # print()

# 1 0 0 0 0 
#   1 0 0 0 
#     1 0 0 
#       1 0 
#         1 


# n = 10

# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(' ',end=' ')
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()

                  # * 
#                 * * 
#               * * * 
#             * * * * 
#           * * * * * 
#         * * * * * * 
#       * * * * * * * 
#     * * * * * * * * 
#   * * * * * * * * * 
# * * * * * * * * * * 

# a = 5

# for i in range(1,a+1):
#     for j in range(1,a-i+1):
#         print(' ',end=' ')
#     for k in range(1,i*2):
#         print('*',end=' ')
#     print()

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * *


# a = 5

# for i in range(1,a+1):
#     for j in range(a-i+1):
#         print(' ',end=' ')
#     for k in range(i*2-1):
#         print('*',end=' ')
#     print()

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 

# n = 5

# for i in range(n,0,-1):
#     for k in range(n - i+1):
#         print(' ',end=' ')
#     for j in range(i*2-1):
#         print('*',end=' ')
#     print()


#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 

# a = 5

# for i in range(1,a+1):
#     for j in range(a-i+1):
#         print('  ',end='')
#     for k in range(i*2-1):
#         print('*',end=' ')
#     print()
# for l in range(a,0,-1):
#     for m in range(a-l+1):
#         print(' ',end=' ')
#     for n in range(l*2-1):
#         print('*',end=' ')
#     print()


#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 

# a = [1, 2, 6, 8, 5, 7]

# largest = a[0]
# second_largest = a[0]

# for i in a:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i

# print("Second largest:", second_largest)




