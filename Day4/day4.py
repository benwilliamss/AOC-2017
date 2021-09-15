def repeat_words_check(words):
    """
    function checks the whole line for repeats,
    returns false if no repeats are found
    True if there are repeated values
    """
    list_max_length = len(words)
    
    for index_one in range(0, list_max_length):
        for index_two in range(index_one+1,list_max_length):
            #condition to compare equality of words for repeats
            if words[index_one] ==  words[index_two]:
                #repeat value
                return True

    #no repeats
    return False



           
def anagram_check(word_one, word_two):

    if len(word_one) != len(word_two):
        #differennce in length, thus not anagrams
        return False
    word_being_compared = word_two #might not be necessary 
     
    
    for char in word_one:
        
        if word_being_compared.find(char) >= 0: #returns index, or -1 if not present
            
            word_being_compared = word_being_compared.replace(char,'',1)
            
            #removed so the same char is not considered twice
        
        else:
            #does not contain the same chars, hence no anagram 
            return False 

    

    return True #both words are anagrams





def anagram_line_check(words):
    """
    if the function contains no pairs,
    return 1 to add to valid passphrases
    else return 0 as passphrase not valid
    """

    list_max_length = len(words)
    
    for index_one in range(0, list_max_length):
        word_one = words[index_one]
        for index_two in range(index_one+1,list_max_length):

            #iterate each word against another word to check if theyre anagrams
            word_two = words[index_two]
            if anagram_check(word_one, word_two): #returns true if they are anagrams 
                return 0

            
    #no anagrams in the line
    return 1




                    

            
           
      




with open("input.txt","r") as f:
    list_of_lines = f.readlines()

    
    
    #count for valid passphrases
    passphrases_valid_no_repeats = 0
    passphrases_valid_no_anagrams =0 

   
    for line in list_of_lines:
        words=line.split()
        if not repeat_words_check(words): 
            #cant have repeats and be an anagram
            passphrases_valid_no_repeats +=1
            passphrases_valid_no_anagrams += anagram_line_check(words)
            
            

    print("valid passphrases (no repeats):", passphrases_valid_no_repeats)
    print("valid passphrases (no anagrams):", passphrases_valid_no_anagrams)


