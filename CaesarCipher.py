while(True):
    inp = int(input("\n1.Encrypt\n2.Decrypt\nEnter your choice(1/2) : "))
    if inp == 1:
        plainText = input("Enter the message : ")
        safe = plainText.upper().replace(" ","")
        enc = ""
        key = int(input("Enter the key : "))
        for i in safe:
            val = (int(ord(i)-65)+key)
            if val > 25:
                val %= 26
            enc += chr(val+65)    
        print("The Encrypted Message : "+enc)
    else:
        encryptedText = input("Enter the Encrypted message : ").upper().replace(" ","")
        dec = ""
        key = int(input("Enter the key : "))
        for i in encryptedText:
            val = (ord(i)-65)-key
            while val < 0:
                val += 26
            dec += chr(val+65)
        print("The Message is : "+dec)
