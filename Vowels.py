"""
A program to take a string and the count the number of vowels
"""

class Vowels():


    def main(self):

        numA = 0
        numE = 0
        numI = 0
        numO = 0
        numU = 0

        vowels = ["a", "e", "i", "o", "u"]
        text = "This sentence will serve to count the number of vowels. Also, it will count them."

        list(text)

        for i in text:
            if i.lower() in vowels:
                if i.lower() == vowels[0]:
                    numA += 1
                elif i.lower() == vowels[1]:
                    numE += 1
                elif i.lower() == vowels[2]:
                    numI += 1
                elif i.lower() == vowels[3]:
                    numO += 1
                else:
                    numU += 1


        print("The number are vowels are:")
        print("Number of A's", numA)
        print("Number of E's", numE)
        print("Number of I's", numI)
        print("Number of O's", numO)
        print("Number of U's", numU)



def words():

    word = Vowels()

    word.main()

words()