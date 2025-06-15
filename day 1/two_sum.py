from colorama import init, Fore, Style

init()

def two_sum(nums, target):
    for i in range(len(nums)):
        print(f'{Fore.YELLOW}=== For {nums[i]} ==={Fore.RESET}')
        if range(i + 1, len(nums)) == None:
            continue
        for j in range(i + 1, len(nums)):
            compute = nums[i] + nums[j]
            yes_or_no = ""
            if compute != target:
                yes_or_no = f"{Fore.RED}[-]{Fore.RESET}"
            else:
                yes_or_no = f"{Fore.GREEN}[+]{Fore.RESET}"
            print(f'{yes_or_no} {nums[i]} + {nums[j]} = {compute}')

print(two_sum([2, 7, 11, 15], 9))