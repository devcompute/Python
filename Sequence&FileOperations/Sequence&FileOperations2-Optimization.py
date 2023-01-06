'''
Business challenge/requirement
LifeTel Telecomis the latest entrant in the highly competitive Telecom market of Singapore.
It issues SIM to the verified users.
Till now verification was manual through the photocopy of approved id card document.
However government has recently introduced Social ID called Reference ID which is mapped to fingerprint of user.
LifeTel should now verify user against the fingerprint and Reference ID.

Key issues
Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID and finger print.

Considerations
System should be secure.

Data volume
-NA

Additional information
-NA

Business benefits
Company will be able to quickly issue SIM to user and expected gain in volume is approximately 10 times as the manual process of verification is replaced with secure automated system
'''

#To make this work one would need to prompt the user to enter their Reference ID with the 'input()' function.
#Next step is see if the length of the ID is valid according to specifications using the 'len()' function.
    #Use 'isalpha()', 'isadigit()', or 'isalnum()' of str class to measure the ID digits for numbers, letters, and special characters.
#Now the ID is valid encrypt it from hackers of mapping and fingerpritns of the user by using 'pycrypto' library.
#Once the Reference ID is encrypted you can print it for reference and have the user decrypt the ID if they would like.
#Now use the reference ID to verify the user fingerprint by comparing the reference ID to the fingerprint database storage.
#If everything matches then the user can use the SIM and if not the user would need to retry or manually verify themselves.