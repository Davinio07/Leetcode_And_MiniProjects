def decode_message(secret_message):
    # Our decryption key (a Dictionary!)
    cipher = {
        'k': 'c',
        '8': 'l',
        's': 'o',
        'x': 'u',
        'z': 'd',
        '1': 'a',
        '2': 'e',
        '3': 'i'
    }
    
    decoded = ""
    
    # We loop through every letter in the secret message
    for letter in secret_message:
        # If we know the secret letter, swap it using our dictionary
        if letter in cipher:
            decoded += cipher[letter]
        # Otherwise, just leave the letter alone
        else:
            decoded += letter
            
    return decoded

# --- Run this to reveal the message ---
print(decode_message("Gr21t job tod1y. W2lkom2 to th2 k8sxz!"))