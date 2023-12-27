#!/usr/bin/env python
# coding: utf-8

# In[1]:


def process_photos(L, N, photo_dimensions):
    for i in range(N):
        W, H = photo_dimensions[i]

        if W < L or H < L:
            print("UPLOAD ANOTHER")
        elif W == H:
            print("ACCEPTED")
        else:
            print("CROP IT")

# Input
L = int(input("Enter the minimum dimension (L): "))
N = int(input("Enter the number of photos (N): "))

photo_dimensions = []
for i in range(N):
    dimensions_input = input(f"Enter the dimensions (W H) for photo {i + 1}: ").split()
    W, H = int(dimensions_input[0]), int(dimensions_input[1])
    photo_dimensions.append((W, H))

# Process and output
process_photos(L, N, photo_dimensions)


# In[2]:


import random

def guess_game():
   
    secret_number = random.randint(1, 10)

    while True:
     
        guess = int(input("Enter a number between 1 and 10: "))

       
        if guess == secret_number:
           
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")


guess_game()


# In[ ]:




