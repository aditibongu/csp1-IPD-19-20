####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'rangers' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'

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

    if len(my_history)==0:
        return 'c'
    else:
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        if my_history[-1]=='c' and their_history[-1]=='b':
            if random.random()<0.4: 
               return 'c'         
            else:
               return 'b' 

    if len(my_history)%3 == 0:
        return 'b'
    else:
        if random.random()<0.3: 
            return 'b'         
        else:
            return 'c'

    if 'b' in their_history[1:11:2]:
      return 'b'
    elif 'b' in their_history[2:11:2]:
      return 'b'
    else:
      return 'c'