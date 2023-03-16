
text_to_encrypt = input("Text: ")
# Key for characters text_1
# key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
# Key for characters text_2
# key = "KXVMCNOPHQRSZYIJADLEGWBUFTkxvmcnophqrszyijadlegwbuft"
# Key for characters text_3
# key = "EBFASWLYGQTZOHDKUCPRNXIVMJebfaswlygqtzohdkucprnxivmj"
# Key for characters text_4
# key = "HMFTKQDERYZJBGPUAWOSNXICVLhmftkqderyzjbgpuawosnxicvl"
# Key for characters text_5
key = "CTLSXAHGBPREQJUMKOWVIFDYZNctlsxahgbpreqjumkowvifdyzn"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

mapping = str.maketrans(alphabet, key)
text_to_encrypt = text_to_encrypt.translate(mapping)


print("Encrypted Text >> ", text_to_encrypt)
