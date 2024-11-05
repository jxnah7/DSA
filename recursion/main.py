def walk(steps):    #function created, named walk, with steps as a parameter
  if steps < 1: #base case, if steps are less than 1
    print("Reached the base case, (steps < 1)") #then print its less than 1
    return  #and end the function, ensuring not an infinite loop
  print("You take a step")  #otherwise, print that we are taking a step
  walk(steps - 1)  #recursive case, then continue the function taking back in steps from parameter subtracting 1, continue until reach base case

#walk(5) Uncomment to check output

          
# We iterate through walk starting at 5 , slowly subtracting 1 until we reach
# the base case.



#HERES AN EXAMPLE OF AN ITERATIVE APPROACH
def walking(stepping):
  for stepping in range(1, stepping + 1):
    print(f"You take step #{stepping}")

# walking(100) Uncomment to check output