import os
from euler.problems.page1 import p7


def main():
    problem = p7
    result = problem.problem()
    print("result:", result)


def pass_trough(patt):
    for p in os.listdir(patt):
        if os.path.isdir(os.path.join(patt, p)):
            print('dir:', p)
            pass_trough(p)
        else:
            print('file:', p)


if __name__ == '__main__':
    # main()
    pass_trough(os.getcwd())


