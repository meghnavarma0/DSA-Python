# Print the steps to solve the tower of hanoi problem for n disks.
step = 0
def toh(s, d, h, n):
    global step
    if n == 1:
        step += 1   
        print("Step ", step, ": Move disk", n,  "from", s, "to", d)
      
        return
    
    toh(s, h, d, n-1)

    step += 1
    print("Step ", step, ": Move disk", n, "from", s, "to", d)

    toh(h, d, s, n-1)

toh("source", "destination", "helper", 3)