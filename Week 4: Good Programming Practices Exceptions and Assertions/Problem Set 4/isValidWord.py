def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    newHand = hand.copy()
    wordCheck = False
    if word in wordList:
      wordCheck = True
    
    letterCheck = set(list(word)) <= set(newHand.keys())

    for letter in word:
      if letter in newHand.keys():
        newHand[letter] -= 1

    valueCheck = all(i >= 0 for i in output.values())

    if wordCheck == True and letterCheck == True and valueCheck == True:
      return True
    else:
      return False
