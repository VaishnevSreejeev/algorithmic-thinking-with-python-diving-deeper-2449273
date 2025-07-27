while True:
    puzzle_nums = list(map(int, input("Enter nums: ").split()))
    puzzle = input("Enter puzzle: ")


    puzzle = [x for x in puzzle if x in ('<','>')]

    sol = []
    for i in puzzle :
        if i == '<':
            sol.append(puzzle_nums.pop(puzzle_nums.index(min(puzzle_nums))))
        else:
            sol.append(puzzle_nums.pop(puzzle_nums.index(max(puzzle_nums))))
    sol.extend(puzzle_nums)

    for x in sol:
        print(x, end =' ')
    print()

    #/home/codespace/.python/current/bin/python 