

def main():
    word_dictionary = {
        'cow': 'A four legged domestic animal.',
        'hen': 'Its a bird.',
        'fish': 'Its a underwater creature.',
        'cat': 'most cute and wild creature on earth ever.',
        'earth': 'a planet in space',
        'dhaka': 'Capital of Bangladesh'
    }

    while True:
        word = input("\nYou have word limitation. You can only ask about cow, hen, fish, cat, earth, dhaka. \n\nEnter the word:   ")
        if word == '':
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])
        
        
        print("\n\nwrite ' e  ' to exit the program")



        if word == 'e' or word == "E":
            print("Program ended") 
            quit() 

main()







