import sys 
from argparse import ArgumentParser
import random
import string
import pandas as pd

class WordGame:
    """

    This is a word game. The game generates a specified number of letters for
    the user and allows the user to make words using those characters. 
    
    """
    
    def __init__(self, englishWords , guessedWords, player, player_letters):
        """  Creates the playerScore, playerWords, guessedWords attributes

        Args:
            playerScore (int): the counter for the scores of players.
            englishWords (list): the list that will contain all the choices of words.
            guessedWords (list): the list that will contain all the user's guessed words.
        """
        self.playerScore = 0
        self.guessedWords = guessedWords
        self.Characters = 0
        self.player = player
        self.player_letters = player_letters
        self.dalist = englishWords
        
    def word_checker(self):
        """(Ivan: Set Operators)
        This method will check the validaity of each
        word guessed by the user. This method takes the list of guessed words
        and checks if each word is only made up of the list of 
        generated characters. All of these valid words are then appended into
        a updated_guesses list. From there both updated_guess and the dalist 
        word list are turned into sets so that the & operator can be utilized
        to find commonality between the two. The result is these common words
        is placed in the self.matched attribute so that it can be used in the
        score method.

    
    
        Simple Values:
            str: This method will be comparing strings or words in a list of
            player guessed words and a list of given words 
            from a sample textfile.
    
        Containers:
            list: There will be a list for both the user guessed scores, 
            the list of given words from the textfile, and the list
            of randomly generated letters.
        
            set: The lists will be converted into sets so that set operators can
            be used between the two sets to find commonality. 
            That is how we will check if the guessed word is 
            in the list of words in the game.
        
        
        Side Effects:
            Changes the guessed_words and generated_words list into sets.
            The empty list self.matched is created.
        
        Returns:
            A list of all the matched words.
        """
        updated_guesses = []
        self.matched = []
        
        
        for x in self.guessedWords:
            if all([char in self.player_letters for char in x]):
                updated_guesses.append(x)
        
                        
        self.dalist = set(self.dalist) 
        guesses = set(updated_guesses) 
        
        match = (self.dalist & guesses)
        self.matched = list(match)

        return self.matched
        
        
           
    def Score(self):
        """(Ivan & f-strings)
        This method will find the score of the player based on the correct
        words guessed. The method will find the length of each word and add it
        into the list_of_scores list. The sum of all these lengths will be the 
        users total score.
    
        Simple values:
            str: Each word guessed in the list of guessed words and the words
            from the list of generated words.
        
            int: In each matching word, the length of the word will be the score
            given for that particular word. These scores will then be added up  
            and return the total score for one player.
    
        Containers:
            lists: The individual scores for each word will be added into 
            a list. These values will then be summed together 
            to create the individual score of the player.

        Side Effects:
            Creates a object that contains a value for each individual's score.

        Returns:
            An f-string stating the player's name and their total score.

        """
        list_of_scores = []
        for word in self.matched:
            x=len(word)
            list_of_scores.append(x)
            
        self.playerScore = sum(list_of_scores)
        return f"Hey {self.player}, your final score is {self.playerScore}!"

    def score_list(self):
        """Sorts the player's guesses so the words that are worth the most points
        are first and goes in decending order.
        
        Returns:
            sorted_guesses(list): sorted list of the guesses
        """
        sorted_guesses = sorted(self.guessedWords, key=len, reverse= True)
        return sorted_guesses
                
    def __str__(self):
        """Gets the highest score from the session and who got that score. After
        it prints that out to the user so they can see who won the game.
        
        Returns
            string: player's final score, name, and guesses
        
        Side effects:
            prints to stdout
        """
        return f"""{self.player} got {self.playerScore} points using
                   {self.guessedWords}!"""
        
    def leaderboard(self, player2): 
        """Shows the leaderboard in a form of pandas dataframe
    
        Args:
            score (tuple of int): player 1's score and player 2's score

        Returns:
            leaderboard (dataframe): players' names as key and players' 
            status as value
        """
        leaderboard_score = pd.read_csv("Player Score Leaderboard - Player Score.csv")

        updated_score = leaderboard_score.replace({'Status' : { 'Player 1 Status' : self.playerScore, 'Player 2 Status' : player2.playerScore}})

        print(updated_score)

def parse_args(arglist):
    """Parses command-line arguments.
    
    Expect two mandatory arguments:
        - Filepath: The file that is being read in with the word list
        - Characters: The amount of letters the user wants to use
    The Function also allows for one optional argument:
        - Players: The amount of players that are playing with a max of 2,
        default is 1.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace."""
    parser = ArgumentParser()
    parser.add_argument("Filepath", help="file containing the word list")
    parser.add_argument("Characters", help = """Integer stating the number of
                        characters the user wants""")
    parser.add_argument("Players", help = """The number of players playing the
                        #game""",default=1)
    return parser.parse_args(arglist)

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
                freshwords = word.strip()
                dalist.append(freshwords)  
        return dalist

def randomizer(Characters):
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
        LettersList = ["e","e","e","e","e","a","a","a","a","s","s","s","s","i","i",
                   "i","i","r","r","r","r","n","n","n","n","t","t","t","o","o",
                   "o","l","l","l","c","c","c","d","d","d","u","u","u","u","g",
                 "p","p","m","m","h","h","b","b","y","y","f","f","v","k","w",
                 "z","x","j","q"]
        CharacterList = []
        [CharacterList.append((random.choice(LettersList))) 
         for x in range(1,int(Characters)+1)]
        return CharacterList
          
def main(filename,characters):
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
    player_guesses = []
    random_characters = randomizer(characters)
    
    
    
    #player =  WordGame()

    print("Welcome to our Word Game!")
    name = input("To begin, What is your name? ")
    #name2 = input("To being, What is your name? ")
    print("You will be able to enter up to 10 words. If you would like to end the game: enter the number 1")
            
    print(f"Here are the letters you can build a word from:{random_characters}")
    
    englishWords = (word_list(filename))
    
    
    while True: 
        word = input("Please enter a word with the given letters:")
        if word == "1" or None:
            break
        player_guesses.append(word)
        #if word not in englishWords:
            #print("This word is not in the list of valid words. Try a different word!")
        #continue
    
    #print(player_guesses)
   
    wordgame = WordGame(englishWords,player_guesses,name,random_characters)
    #wordgame2 = WordGame(englishWords,player_guesses,name2,random_characters)

    wordgame.word_checker()
    print(wordgame.Score())
    #print(wordgame2.Score())
        
    
    
        

    
    
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.Filepath, args.Characters)
    
