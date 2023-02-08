#continue-->takes come back to the for loop rest of the statement after the continue will not execute for that cycle.
#statement--> The continue statement is used to skip the rest of the code inside a loop for current iteration only.
#loop does not terminate but continues on with the next iteration.
for i in range(1,10):
    if(i==5):
        continue
    print(i)