from enum import Enum
from unittest import result

class Result(Enum):
        EQUAL = 0
        WINS = 1
        LOSES = 2

class Play(object):
    """ Representa una jugada """
    def description(self):
        pass

    def compare(self, otherPlay):
        """ Se compara con la otra jugada y devuelve un Result de la comparación """
        pass

class Paper(Play):
    def description(self):
        return "Paper 🧻 "
    
    def compare(self, otherPlay):
        result = None
        if type(otherPlay) == Rock or type(otherPlay) == Spock:
            result = Result.WINS
        elif type(otherPlay) == Scissors or type(otherPlay) == Lizard:
            result = Result.LOSES
        else:
            result = Result.EQUAL
        return result

class Scissors(Play):
    def description(self):
        return "Scissors ✂️ "

    def compare(self, otherPlay):
        if self.__class__ == otherPlay.__class__:
            return Result.EQUAL
        elif type(otherPlay) == Paper or type(otherPlay) == Lizard:
            return Result.WINS
        else:
            return Result.LOSES

class Rock(Play):
    def description(self):
        return "Rock 🪨 "

    def compare(self, otherPlay):
        result = None
        if type(otherPlay) == Scissors or type(otherPlay) == Lizard:
            result = Result.WINS
        elif type(otherPlay) == Paper or type(otherPlay) == Spock:
            result = Result.LOSES
        else:
            result = Result.EQUAL
        return result

class Lizard(Play):
    def description(self):
        return "Lizard 🦎 "

    def compare(self, otherPlay):
        result = None
        if type(otherPlay) == Paper or type(otherPlay) == Spock:
            result = Result.WINS
        elif type(otherPlay) == Rock or type(otherPlay) == Scissors:
            result = Result.LOSES
        else:
            result = Result.EQUAL
        return result

class Spock(Play):
    def description(self):
        return "Spock 🖖 "

    def compare(self, otherPlay):
        result = None
        if type(otherPlay) == Scissors or type(otherPlay) == Rock:
            result = Result.WINS
        elif type(otherPlay) == Paper or type(otherPlay) == Lizard:
            result = Result.LOSES
        else:
            result = Result.EQUAL
        return result
