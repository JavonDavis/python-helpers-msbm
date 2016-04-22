# if __name__ == "__main__":
#     n = raw_input()
#     answers= []
#     for i in range(0,int(n)):
#         count =0
#         j = raw_input()
#         words = j.split(" ")
#         for k in range(0,len(words[0])):
#             if words[0][k] != words[1][k]:
#                 count = count+1;
#         answers.append(count)
#     for i in answers:
#         print i
#


# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# if __name__ == "__main__":
#     n = raw_input()
#     options = []
#     while n != '0 0':
#         options.append(n)
#         n = raw_input()
#
#     for opt in options:
#         nums = opt.split(" ")
#         num1 = int(nums[0])
#         num2 = int(nums[1])
#
#         root1 = int(num1**0.5)
#         root2 = int(num2**0.5)
#         if root1**2<num1:
#             print (num2-num1+1)-((root2)-root1)
#         else:
#             print (num2-num1+1)-((root2+1)-root1)


# if __name__ == "__main__":
#     n = raw_input()
#     (red,blue) = n.split()
#     fashionCount = 0
#     count = 0
#     red = int(red)
#     blue = int(blue)
#     while red > 0 and blue > 0:
#         fashionCount += 1
#         red -= 1
#         blue -= 1
#
#     while red>1:
#         count += 1
#         red -= 2
#
#     while blue > 1:
#         count += 1
#         blue -= 2
#
#     print str(fashionCount) + " " + str(count)

# if __name__ == "__main__":
#     num_houses = raw_input()
#     floors = raw_input()
#     floors = floors.split()
#     answers = []
#
#     floors.reverse()
#     high = floors[0]
#     for i in range(0, len(floors)):
#
#         if int(floors[i]) >= int(high):
#             high = floors[i]
#             answers.append(0)
#         else:
#             answers.append((int(high)-int(floors[i])) + 1)
#
#     answers.reverse()
#
#     for i in answers:
#         print i,
