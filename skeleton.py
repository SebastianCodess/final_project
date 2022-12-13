import sys 
from argparse import ArgumentParser
import random
import string

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
        return f"Hey {self.player}, your final score is {self.playerScore}!"

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
            self.highscore, self.winner = max(score), "player 1"
            return self.highscore, self.winner
        else:
            self.highscore, self.winner = max(score), "player 2"
            return self.highscore, self.winner
                
    def __str__(self):
        """Gets the highest score from the session and who got that score. After
        it prints that out to the user so they can see who won the game.
        
        Returns
            highest_score (list of int): the highest score from the session
        
        Side effects:
            prints to stdout
        """
        return f"{self.winner} won the game with {self.highscore} points!"
        
    def leaderboard(self, player2): 
        """Shows the leaderboard in a form of dictionary 
    
        Args:
            score (tuple of int): player 1's score and player 2's score

        Returns:
            leaderboard (dictionary): players' names as key and players' 
            status as value
        """
        score_leaderboard = {"player1": "" , "player2": ""}

        for self.playerScore, player2.playerScore in self.score:
            score_leaderboard["player 1"] = self.playerScore
            score_leaderboard["player 2"] = player2.playerScore

        return score_leaderboard

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
          
def main(filename,Characters=7):
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
    random_characters = randomizer(Characters)
    
    
    
    #player =  WordGame()

    print("Welcome to our Word Game!")
    name = input("To begin, What is your name? ")
    #name2 = input("To being, What is your name? ")
    
            
    print(f"Here are the letters you can build a word from:{random_characters}")
    print("If you would like to end the game or cannot think of other words:" 
          " please enter the number 1")
    
    englishWords = (word_list(filename))
    
    
    while True: 
        word = input("Please enter a word with the given letters or enter the number 1 "
                      "to end the game:")
        if word == "1":
            print("You have ended the WordGame.")
            break
        player_guesses.append(word)
        if word not in englishWords:
            print("This word is not in the list of valid words. Try a different word!")
        continue
    
    #print(player_guesses)
   
    wordgame = WordGame(englishWords,player_guesses,name,random_characters)
    wordgame2 = WordGame(englishWords,player_guesses,name,random_characters)

    wordgame.word_checker()
    print(wordgame.Score())
    print(wordgame2.Score())
        
    
    
        

    
    
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.Filepath, args.Characters)
    
