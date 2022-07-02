from dataclasses import dataclass
from math import fabs
import re
from copy import copy
import json

@dataclass
class Answer():
    ans: str
    pnt: int
    trig: bool

    def __init__(self, ans, pnt):
        self.ans = ans
        self.pnt = pnt
        self.trig = False
def Answer(ans, pnt):
    answer = {
        "ans": "",
        "pnt": "",
        "trig": False
    }
    answer["ans"] = ans
    answer["pnt"] = pnt
    return copy(answer)

def Round(question=""):
    round = {
        "answers": [],
        "multiply": 1,
        "question": ""
    }
    round["question"] = question
    return copy(round)

@dataclass
class Rounds():
    rounds: list
    def __init__(self):
        self.rounds = []

for i in range(1, 6):
    q_path = f"joc/seria{i}/questions.xml"

    with open(q_path, "r") as f:
        rounds = []
        first_time = True
        lines = f.readlines()
        for line in lines:
            if line.startswith("<question "):
                l = line.split("\"")
                if first_time == True:
                    first_time = False
                else:
                    rounds.append(copy(round))
                round = Round(l[1].replace(".", ". ").strip())
            elif line.startswith("<answer "): # 1, 3
                l = line.split("\"")
                answer = Answer(l[1].strip(), int(l[3]))
                round["answers"].append(answer)
        game = {
            "rounds": rounds,
            "final_round": []
        }

        with open(f'out/explo{i}.json', 'w') as outfile:
            outfile.write(json.dumps(game))

