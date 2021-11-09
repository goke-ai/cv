'''
 import a module for accessing commandline arguement or parameter passed.
 find sum

'''
import sys

print("commandline argument array \n", sys.argv)
print()
print("first argument: ", sys.argv[0])

# check if arguement passed is up to 3

if len(sys.argv) >= 3:
    print("second argument: ", sys.argv[1])
    print("second argument: ", sys.argv[2])

    # get the numbers to add
    par1 = int(sys.argv[1])
    par2 = int(sys.argv[2])

    sum = par1 + par2

    # print result
    print('sum = ', sum)
else:
    print()
    print('insufficient arguement')