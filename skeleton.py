import sys 
from argparse import ArgumentParser
import random
import string
import pandas as pd

class WordGame:
    """

    This is a word game. The game generates a specified number of letters for
    the user and allows the user to make words using those characters. 
    
    Attributes:
        playerScore(int): the player's score
        guessedWords(list of str): the player's guessed words
        Characters(int): the amount of random characters to guess the words from
        player(str): the player's name
        player_letters(list of str): the random letters to guess the words from 
        dalist(str): the list of all american english words

    
    """
    
    def __init__(self, englishWords , guessedWords,player_letters,player = "player 1"):
        """(Fadel: Optional Parameter) Creates the playerScore, playerWords, guessedWords attributes

        Args:
            englishWords (list): the list that will contain all the choices of words.
            guessedWords (list): the list that will contain all the user's guessed words.
            player_letters(list of str): the random letters to guess the words from 
            player (str): the name of the player. 
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
        
        
           
    def score(self):
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
        return self.playerScore

    def score_list(self):
        """(Chris: list sorting)
        Sorts the player's guesses so the words that are worth the most points
        are first and goes in decending order.
        
        Containers:    
            list: the user's correctly guessed words sorted by longest to 
                shortest
        
        Returns:
            sorted_guesses(list): sorted list of the guesses
        """
        sorted_guesses = sorted(self.matched, key=len, reverse= True)
        return sorted_guesses
                
    def __str__(self):
        """(Chris: magic methods)
        Gets the highest score from the session and who got that score. After
        it prints that out to the user so they can see who won the game.
        
        Returns
            string: player's final score, name, and guesses
        """
        return f"Hey {self.player}, your final score is {self.score()}!"
        
    def leaderboard(self, player2 = None): 
        """(Fadel: Pandas Concatenate Method) Shows the leaderboard in a form of a dataframe. 
        The objective of using dataframe is to make the score leaderboard visually more appealing. 
        In comparison to using dictionary or tuple, in this case there can be two dataframes (player 1's and player 2') 
        that can be concatenated. 
    
        Args:
            score (tuple of int): player 1's score and player 2's score

        Returns:
            leaderboard (dictionary): players' names as key and players' 
            status as value
        """
        leaderboard_player = pd.read_csv("Player Score Leaderboard - Player Score.csv")
        leaderboard_score = pd.read_csv("Player Score Leaderboard 2 - Score.csv")
        updated_score = leaderboard_player.replace({'Player' : { 'Player 1' : self.player}})
        updated_score2 = leaderboard_score.replace({'Score' : { 'Empty Score' : self.playerScore}})
        combined_score = pd.concat([updated_score, updated_score2], axis=1)

        print(combined_score)

def parse_args(arglist):
    """(Dan:Parse_Args)
    Parses command-line arguments.
    
    Expect one mandatory arguments:
        - Filepath: The file that is being read in with the word list
    The Function also allows for one optional argument:
        - Characters: The amount of characters the user wants to play with,
        default is 7.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace."""
    parser = ArgumentParser()
    parser.add_argument("Filepath", help="file containing the word list")
    parser.add_argument("Characters", help = """Integer stating the number of
                        characters the user wants""", default=7)
    return parser.parse_args(arglist)

def word_list(filename):
    
        """
        (Sebastian, with statement)
        This method will open a file using a with statement, read the words 
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
        """(Dan:List Comprehension)
        If there is a specified number by the user it generates that number
        of characters. If there is not it will by default generate 7 random 
        characters. The letter distribution of scrabble letters was what I used
        to ensure that players get a usable set of letters to play with.

        Args:
            Characters (Int): The amount of characters that the user wants to
        generate to use for making words. Default is 7.
            
        Returns: A list of all of the characters that the user will pick from 
        when making their words.
        """
        LettersList = ["e","e","e","e","e","e","e","e","e","e","e","e","e",
                       "a","a","a","a","a","a","a","a","a","b","b","c","c",
                       "d","d","d","d","f","f","g","g","g","h","h",
                       "i","i","i","i","i","i","i","i","i","j","k","l","l","l",
                       "l","m","m","n","n","n","n","n","n","o","o","o","o",
                       "o","o","o","o","p","p","q","r","r","r","r","r","r",
                       "s","s","s","s","t","t","t","t","t","t","u","u","u","u",
                       "v","v","w","w","x","y","y","z"]
        CharacterList = []
        [CharacterList.append((random.choice(LettersList))) 
         for x in range(1,int(Characters)+1)]
        return CharacterList
          
def main(filename,Characters):
    """ 
    (Sebastian, conditional expressions)
    The main function will allow a user to play the WordGame by inputting words. 
    The main function will check to see if the word a user inputed is valid based 
    on the words in the file. The main function also checks to see if you are
    using the random letters generated to build a word.
    
    Args:
        filename(file): this is a text file containing words.
        characters(int): this is the number of characters a user wants to
                        generate. 
        
    
    Side effects: 
            prints to standard output. 
    """
    player_guesses = []
    random_characters = randomizer(Characters)
    missing_letters = []
    

    print("Welcome to our Word Game!")
    name = input("To being, What is your name? ")
            
    print("If you would like to end the game or cannot think of other words:" 
          " please enter the number 1")
    
    englishWords = (word_list(filename))
    
    
    while True: 
        word = input(f"Please enter a word with the given letters {random_characters} :\n")
        if word == "1":
            print("You have ended the WordGame.\n")
            break
        player_guesses.append(word)
        
        
        for letter in word: 
            if letter not in random_characters:
                missing_letters.append(letter) 
        if missing_letters: 
            print(f"""You have used the letters {missing_letters}, which are not 
                  apart of the letter list. Try a different word please!""")
        elif word in englishWords and not missing_letters: 
            print("You have used the correct letters and this word is valid! This word will be added to your final score!")      
                      
        if word not in englishWords:
            print("""This word is not in the list of valid words and will not be 
              added to your final score. Try a different word!""")
        
        
       
        
        
         

                
            
   
    wordgame = WordGame(englishWords,player_guesses,random_characters,name)

    wordgame.word_checker()
    print(f"These are the valid words you entered sorted by length: {wordgame.score_list()}")
    print("""You guessed a lot of words. 
          Good Job!""") if len(wordgame.score_list()) >= 5 else print(f"""You suck, 
        you only guessed {len(wordgame.score_list())} words, better luck next time!""")

    print(f"{wordgame}\n\n")
    print("Here's your leaderboard:\n")
    wordgame.leaderboard()
    
    print("Thanks for playing!") 
        
    
    
        

    
    
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.Filepath, args.Characters)
    
