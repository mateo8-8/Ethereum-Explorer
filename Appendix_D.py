#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:07:46 2022

@author: matthewmccreary
"""
import random
import time

# timer to show execution times
create_hash_start = time.time()

#open a file to write the output logs
#f = open("2-digit-brute.py.out.txt", "w")

# variables for the simple consensus algorithm.
target_hash = 1000005
nonce = 0

print("** Finding Target for Validation **")
yes = False
while yes != True:
    guess_hash = random.randint(1000000,9999999)
    f.write(str(guess_hash))
    f.write("\n")
    nonce += 1
    if guess_hash <= target_hash:
        yes = True
        f.close()
        
print("Target hash solved with: ", guess_hash)       
print("Nonce : ", nonce)
f.close()  
create_hash_end = time.time()


check_hash_start = time.time()
print("** Checking for Verification **")
if guess_hash <= target_hash:
    check_hash_end = time.time()
    print("Our supplied nonce was: ", nonce)
    print("Our found value is: ", guess_hash)
    print("The result is less than or equal to the target: ", target_hash)
    # describe to the user what just happened
print("*****************************************")
print("********** Performance Review ***********")
print("*****************************************")
print("Total execution time to create a valid hash: ", (create_hash_end - create_hash_start))
print("Total execution time to check a valid hash: ", (check_hash_end - check_hash_start))

print("\n ** Verification has been completed, this transaction has been\n", 
          "verified according to our consensus algorithm.  Or in other terms\n",
          "there has been a consensus between at least two nodes that this\n", 
          "transaction and the supplied nonce are correct. **")
print("** To see process log, navigate to the 2-digit-brute.py.out.txt file **")
