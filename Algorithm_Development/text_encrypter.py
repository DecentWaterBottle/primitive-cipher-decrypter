
text_to_encrypt = input("Text: ")
# Key for characters text_1.txt.txt.txt.txt.txt.txt.txt.txt
# key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
# Key for characters text_2.txt.txt.txt.txt.txt.txt.txt.txt
# key = "KXVMCNOPHQRSZYIJADLEGWBUFTkxvmcnophqrszyijadlegwbuft"
# Key for characters text_3.txt.txt.txt.txt.txt.txt.txt.txt
# key = "EBFASWLYGQTZOHDKUCPRNXIVMJebfaswlygqtzohdkucprnxivmj"
# Key for characters text_4.txt.txt.txt.txt.txt.txt.txt.txt
# key = "HMFTKQDERYZJBGPUAWOSNXICVLhmftkqderyzjbgpuawosnxicvl"
# Key for characters text_5.txt.txt.txt.txt.txt.txt.txt.txt
key = "CTLSXAHGBPREQJUMKOWVIFDYZNctlsxahgbpreqjumkowvifdyzn"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

mapping = str.maketrans(alphabet, key)
text_to_encrypt = text_to_encrypt.translate(mapping)


print("Encrypted Text >> ", text_to_encrypt)
