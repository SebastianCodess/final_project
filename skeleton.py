def leaderboard(): 
    """ 
    Shows the leaderboard in a form of dictionary 
    
    Args:
        score (tuple of int): player 1's score and player 2's score

    Returns:
        leaderboard (dictionary): players' names as key and players' status as value
    """

def word_list(filename):
    """
    This method will open a file using a with statement, read the words in each 
    line within the file, and append those words to a list.
    
    Simple Values:
        str: This method will contain strings in the name of the file as an
        argument.
    
    Files:
        utf-8: The list of words in the textfile should be UTF-8 encoded. If the
        the file is not utf-8 encoded, than we will change the encoding to match 
        the text file. We will be retrieving the word list from Aric. Each line
        of the file should consist of a word. 
    
    Containers:
        list: this method will contain a list of words being read from a text 
        file.
    
    Args: 
        filename(str): this is a string that indicates the name of the text file. 
    
    Returns:
        wordlist(list of str): this is a list that will contain all the words 
        read from the text file. 
    
    """
    dalist = list()
    with open (filename, "r", encoding = "utf8") as f: 
        for word in f:
          freshwords = word.strip().split()
          dalist.append(freshwords)
          
    return dalist
          
    pass
          
          
def main(player1,player2):
    """ 
    The main function will call two classes and create an instance of both classes. 
    It will print the score of both players after both of their sessions have
    finished.
    
    Args:
        player1(Word object): this is the first player in the game.
        player2(Word object): this is the second player in the game. 
        
    
    Side effects: 
            This function will print out the scores and names of both players 
            using an F-string. 
    """
    
    
if __name__ == "__main__":
    
