def print_table(nums):
    """Displays the given list as a table of multiples"""
    print("    ", end=" ")
    for i in nums:
        print("{:<4}".format(i), end=" ")
    print()

    for n in nums:
        count = 0
        print("{:<3}".format(n), end="  ")
        while count < len(nums):
            print("{:<3} ".format(n * nums[count]), end=" ")
            # print(str((n * nums[count])) + " ", end="  ")
            count += 1
        print()

def main():
    size = input("Enter size of table: ")
    nums = [i for i in range(0,int(sizeJ)+1)]
    print_table(nums)

if __name__ == '__main__':
    main()