from argparse import ArgumentParser

class WordGame:
    """

    This is a word game. The game generates a specified number of letters for
    the user and allows the user to make words using those characters. 
    
    """
    
    def __init__(self, playerScore, playerWords, guessedWords):
        """  Creates the playerScore, playerWords, guessedWords attributes

        Args:
            playerScore (int): the counter for the scores of players.
            playerWords (list): the list that will contain all the choices of words.
            guessedWords (list): the list that will contain all the user's guessed words.
        """
        self.playerScore = 0
        self.playerLetters = []
        self.guessedWords = []


    def word_list(filename):
        """This method will open a file using a with statement, read the words 
        in each line within the file, and append those words to a list.
    
        Simple Values:
            str: This method will contain strings in the name of the file as an
            argument.
    
        Files:
            utf-8: The list of words in the textfile should be UTF-8 encoded. 
            If the the file is not utf-8 encoded, than we will change the 
            encoding to match the text file. We will be retrieving the word list
            from Aric. Each line of the file should consist of a word. 
    
        Containers:
            list: this method will contain a list of words being read from a text 
            file.
    
        Args: 
            filename(str): this is a string that indicates the name of the text 
            file. 
    
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
    
    def randomizer(self, Vowels, Consonants):
        """Takes the two numbers given by the user for the numbers of vowels and
        consonants that they want and then generates those characters by using a
        list comprehension.

        Args:
            Vowels (Int): The number of Vowels the user wants in their character
            list
            Consonants (_type_): The number of Consonants the user wants in 
            their character list
            
        Returns: A list of all of the characters that the user will pick from 
        when making their words.
        """
        pass
    
    def word_checker(self):
        """This method will check if the guessed is found in the list of words.
        The method takes the list of guessed words and list of generated words and 
        changes them to sets so that the set operator & can be used to find
        commonality. The method also checks if player guessed a word containing a 
        letter that was not provided in the list of letters shown to the player. If
        that happens then the word is then deleted from the list of guessed words.
    
    
        Simple Values:
            str: This method will be comparing strings or words in a list of player
            guessed words and a list of given words from a sample textfile.
    
        Containers:
            list: There will be a list for both the user guessed scores as well as 
            the list of given words from the textfile.
        
            set: The lists will be converted into sets so that set operators can be
            used between the two sets to find commonality. That is how we will 
            check if the guessed word is in the list of words in the game.
        
        Args:
            guessed_words(list of str): Contains all of the words the player guessed
            generated_words(list of str): Contains all of the words from the 
            textfile used to compare words. 
        
        
        Side Effects:
            Changes the guessed_words and generated_words list into sets.
        
        Returns:
            A set of matching/correct words.
        """
        matched_words = []
        #updated_guesses = [x for x in self.guessedWords if x == self.playerLetters]
        updated_guesses = all([x in self.guessedWords for x in self.playerLetters])
        set(self.dalist) 
        set(updated_guesses) 
        matched_words = list(self.dalist & updated_guesses)
           
    def Score(self):
        """This method will keep track of the score by taking the length of each
        word that matched the generated list of words and create a score.
        The scores will then be added up to create a main score for a single player.
    
        Simple values:
            str: Each word guessed in the list of guessed words and the words
            from the list of generated words.
        
            int: In each matching word, the length of the word will be the score
            given for that particular word. These scores will then be added up and 
            return the total score for one player.
    
        Containers:
            lists: The individual scores for each word will be added into a list.
            These values will then be summed together to create the individual score
            of the player.

        Side Effects:
            Creates a object that contains a value for each individual's score.

        Returns:
            The score of an individual player that is the sum of all the points
            given for every matched words length.
        """
        list_of_scores = []
        for word in matched_words:
            x=len(word)
            list_of_scores.append(x)
            
        self.playerScore = sum(list_of_scores)

    def score_comparison(self, player2 = None):
        """Compares the scores from the two players. It takes the score and puts
        the integers into a tuple that has the player one as the first number
        and player two as the second number. The higher number is declaired the 
        winner and is returned to be used later.
        
        Returns:
            high_score (int): the highest score from the two players
        """
        score = ()
        score = (self.playerScore, player2.playerScore)
        if self.playerScore > player2.playerScore:
            high_score, winner = max(score), "player 1"
            return high_score, winner
        else:
            high_score, winner = max(score), "player 2"
            return high_score, winner
                
    def high_score(self):
        """Gets the highest score from the session and who got that score. After
        it prints that out to the user so they can see who won the game.
        
        Returns
            highest_score (list of int): the highest score from the session
        
        Side effects:
            prints to stdout
        """
        print(f"{winner} won the game with {high_score} points!")
        
    def leaderboard(): 
        """Shows the leaderboard in a form of dictionary 
    
        Args:
            score (tuple of int): player 1's score and player 2's score

        Returns:
            leaderboard (dictionary): players' names as key and players' 
            status as value
        """
        pass
    

def parse_args(arglist):
    """Parses command-line arguments.
    
    Expect three mandatory arguments:
        - Filepath: The file that is being read in with the word list
        - Vowels: The number of vowels the user wants
        - Consonants: The number of consonants the user wants, max of 6 
    The Function also allows for one optional argument:
        - Players: The amount of players that are playing with a max of 2,
        default is 1.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace."""
    parser = ArgumentParser()
    parser.add_argument("Filepath", help="file containing the word list")
    parser.add_argument("Vowels", help = """Integer stating the number of
                        vowels the user wants""")
    parser.add_argument("Consonants", help = """Integer stating the number of
                        Consonants the user wants""")
    parser.add_argument("Players", help = """The number of players playing the
                        game""",default=1)
    return parser.parse_args(arglist)
          
          
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
    pass
    
    
if __name__ == "__main__":
    pass
