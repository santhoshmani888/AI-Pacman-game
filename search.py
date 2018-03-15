# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        #util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
	
def depthFirstSearch(problem):
    presentpos = problem.getStartState() # present state 
    vnode,moves = [],[]        # visisted nodes,moves taken to reach present node
    # Stack is used to get LIFO  
    nodestack=util.Stack()
	#push the initial state to stack
    nodestack.push((presentpos, moves))
    while nodestack:
        node, move_dir = nodestack.pop()
        if  node not in vnode:
            vnode.append(node)
            if problem.isGoalState(node):
                return move_dir
            nextnode = problem.getSuccessors(node)
            for n in nextnode:
                pos, direct, pathcost = n
                newmov=(move_dir+[direct])
                
                #Foreach successor node update new action
                nodestack.push((pos, newmov))
    return []


def breadthFirstSearch(problem):
    presentpos = problem.getStartState() # present state 
    vnode,moves = [],[]        # visisted nodes,moves taken to reach present node
    # queue is used to get FIFO 
    nodestack=util.Queue()
	#push the initial state to stack
    nodestack.push((presentpos, moves))
    while nodestack:
        node, move_dir = nodestack.pop()
        if  node not in vnode:
            vnode.append(node)
            if problem.isGoalState(node):
                return move_dir
            nextnode = problem.getSuccessors(node)
            for n in nextnode:
                pos, direct, pathcost = n
                newmov=(move_dir+[direct])
                
                #Foreach successor node update new action,cost
                nodestack.push((pos, newmov))
    return []



def uniformCostSearch(problem):
    presentpos = problem.getStartState() # present state 
    vnode,moves = [],[]        # visisted nodes,moves taken to reach present node
    #priority queue is used to get min cost path 
    nodestack=util.PriorityQueue()
	#push the initial state to stack
    nodestack.push((presentpos, moves),0)
    while nodestack:
        node, move_dir = nodestack.pop()
        if  node not in vnode:
            vnode.append(node)
            if problem.isGoalState(node):
                return move_dir
            nextnode = problem.getSuccessors(node)
            for n in nextnode:
                pos, direct, pathcost = n
                newmov=(move_dir+[direct])
                newcost=(problem.getCostOfActions(newmov))
                #Foreach successor node update new action,cost
                nodestack.push((pos, newmov),newcost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    presentpos = problem.getStartState() # present state 
    vnode,moves = [],[]        # visisted nodes,moves taken to reach present node
    #priority queue is used to get min cost path 
    nodestack=util.PriorityQueue()
	#push the initial state to stack
    nodestack.push((presentpos, moves), heuristic(presentpos, problem))
    while nodestack:
        node, move_dir = nodestack.pop()
        if  node not in vnode:
            vnode.append(node)
            if problem.isGoalState(node):
                return move_dir
            nextnode = problem.getSuccessors(node)
            for n in nextnode:
                pos, direct, pathcost = n
                newmov=(move_dir+[direct])
                newcost=(problem.getCostOfActions(newmov) + heuristic(pos, problem))
                #Foreach successor node update new action,cost
                nodestack.push((pos, newmov),newcost)
    return []


 




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
