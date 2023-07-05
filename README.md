
# An Automated Decrypter of Traditional Substitution Ciphers

This project provides an effective solution for decrypting traditional substitution ciphers by using a combination of the hill-climbing algorithm and bigrams/quadgrams. 

The project is broken into two distinct sections:
- Algorithm 
- Web Application

The former focuses on the creation and testing of the decryption algorithm. The latter implements the resulting algorithm into a web application.  

By using the hill-climbing algorithm, we are to iteratively search for the most likely decryption key by choosing a random starting key and making small changes to improve its fitness over time. Both bigrams and quadgrams can be used to assess the keys fitness. A new random key is picked 20 times, and each key is iteratively improved 2000 times. The key providing the highest fitness score is chosen as the most likely contender to be the correct key. 

## Algorithm Effectiveness
In addition to the practical implementation, the project also includes a section to thouroughly test and assess the accuracy of the decryption process for varying lengths of texts. A brute-force frequency analysis approach is used as a baseline to test against. 

![Algorithm Accuracies](https://github.com/DecentWaterBottle/primitive-cipher-decrypter/blob/master/images/algorithm-accuracy.png)
