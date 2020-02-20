####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'rangers' # Only 10 chars displayed.
strategy_name = 'Choose a one that has bigger collude!'
strategy_description = 'First, check all the rounds that the opponent chose from their history and count the numbers of collude and betrays. Based on the amount of them, choose the one that has bigger value. If the opponents made the same amount of collude and betrays, then it will radomly choose betray or collude'

import random
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    theirb = 0 
    theirc = 0
    actions = ['b', 'c']
    for action in their_history:
      if action == 'b':
        theirb += 1
      if action == 'c':
       theirc += 1
    if theirb > theirc:
      return 'b'
    elif theirb == theirc:
      return random.choices(actions)
    else:
      return 'c'

  