#!/user/bin/python

### Calculate a sum of squares of list of integers, excepting negatives ###
# First line of input is N (1 <= N <= 100)
# Each of the following N test cases:
#   One line contans an integer X (X <= 100)
#   Next line contains X integers space-separated
# Each test case, calculate sum of squares of integers excepting negatives
# Input and output from standard input and standard output respectively

def process_list(str):
    number = int(str)
    if number <= 0:
        return 0
    else:
        return number**2

def recur(N):
    if N == 0:
        return
    X = int(raw_input())
    result = sum(map(process_list, raw_input().split()))
    print result
    recur(N-1)

def main():
    N = int(raw_input())
    recur(N)

if __name__ == "__main__":
    main()
