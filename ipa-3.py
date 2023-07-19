'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
from_member = str(input("Username of user here:"))
to_member = str(input("Username of other user here:"))

def relationship_status(from_member, to_member, social_graph):
    # Check if fromMember follows toMember
    if to_member in social_graph.get(from_member).get("following"):
        # Check if toMember follows fromMember
        if from_member in social_graph.get(to_member).get("following"):
            return "friends"
        else:
            return "follower"
    # Check if toMember follows fromMember
    elif from_member in social_graph.get(to_member).get("following"):
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
    
    for i in range(len(board)):

        if all(value == 'X' for value in board[i]):
             return 'X'
        elif all(value == 'O' for value in board[i]):
             return 'O'

        if all(row[i] == 'X' for row in board):
             return 'X'
        elif all(row[i] == 'O' for row in board):
             return 'O'


    check_diagonal = [board[i][i] for i in range(len(board))]
    if all(value == 'X' for value in check_diagonal):
        return 'X'
    elif all(value == 'O' for value in check_diagonal):
        return 'O'

    check_diagonal2 = [board[i][len(board) - i - 1] for i in range(len(board))] 
    if all(value == 'X' for value in check_diagonal2):
        return 'X'
    elif all(value == 'O' for value in check_diagonal2):
        return 'O'

    else: 
        return 'NO WINNER'
    
tic_tac_toe(board1)

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

first_stop = "upd"
second_stop = "dlsu"
route_map = legs
def eta(first_stop, second_stop, route_map):
    if first_stop == second_stop:
        return 0
    
    travel_time = 0
    current_stop = first_stop
    while current_stop != second_stop: #tells the function to keep on looping until it reaches the last stop
        for key in route_map.keys():
            if current_stop == key[0]:
                travel_time += route_map[key]["travel_time_mins"]
                current_stop = key[1] #makes current_stop be the key[1] of the key, like if its ("upd","admu"), "upd" will now become "admu" and make a new current_stop, which makes sure that it will go to the next key
                break
            else:
                continue
    return travel_time

eta(first_stop, second_stop, route_map)