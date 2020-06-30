# Print the steps to solve the tower of hanoi problem for n disks.
step = 0
def toh(s, d, h, n):
    global step

    # Base Condition: If there was only one disk left, you would transfer it directly from source to destination
    if n == 1:
        # Increment the number of steps
        step += 1   
        print("Step ", step, ": Move disk", n,  "from", s, "to", d)
        return


    # Transfer the n - 1 discs, from the top, from source tower to helper tower with the help of destination tower
    toh(s, h, d, n-1)

    # Increment the number of steps
    step += 1

    # Transfer the last disc from source tower to destination tower 
    print("Step ", step, ": Move disk", n, "from", s, "to", d)

    # Transfer the n - 1 discs, which were previously transferred to helper tower, to destination tower.
    # This means transferring all the discs from helper tower to destination tower.
    toh(h, d, s, n-1)

toh("source", "destination", "helper", 3)