from web3.auto import w3
# Use the file from the keystore to get publically viewable values.
# We open the file, read the values into the variable called "encrypted_key"
with open("<enter your keystore address, file path>") as keyfile:
    encrypted_key = keyfile.read()
    # Then we pass the value into the w3.eth.account.decrypt function (w3 is importants in DApp development)
    # To implement a dictionary attack on the private key, you will need a dictionary, a while loop with an indexer.  
    private_key = w3.eth.account.decrypt(encrypted_key, '<the password you created the account with>')

# This library helps us go from RLPx to Hex values.  Easier for us to read 
import binascii
print("This is your Ethereum private key: ", binascii.b2a_hex(private_key))    
