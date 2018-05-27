"""
Practice problems for python
"""

def main():

    answer = input("Please enter a word to use for pig latin.")

    latin = list(answer)

    latin.append('-')

    latin.append(latin[0])

    del latin[latin.index(latin[0])]

    latin.append('ay')

    

    print("".join(latin))


main()

    
