# This is python program  to understand the concept of recursion.
# for solving the problem of TOWER OF HANOI.

count = 0
def tower_of_hanoi(beg,mid,end,rings):
 # count for counting the turn required for solving the problem of TOH.
    if rings >= 1 :
        tower_of_hanoi(beg,end,mid,rings-1)
        global count
        count = count + 1
        print(f"step{count}: {beg} to {end}.")
        tower_of_hanoi(mid,beg,end,rings-1)



tower_of_hanoi("first","second","third",3)