'''
Created on 12-04-2012

@author: Marta and Dawid Ireno
'''

'''
    The Game of Life, also known simply as Life, is a cellular automaton devised by the British 
    mathematician John Horton Conway in 1970.[1]
    The "game" is a zero-player game, meaning that its evolution is determined by its initial state,
    requiring no further input. 
    One interacts with the Game of Life by creating an initial configuration and observing how it evolves.
    
    by Wikipedia
'''

class Board:
    '''    
    Board is a infinitive list of coordiantes. Active cells are stored in 
    cells variable. A 'tick' moves the game state to the next stage in live
    '''
    
    def __init__(self):
        self.cells = []
    
    def gen_dict(self):
        '''
        Generates a neighbourship relations dictionary. Keys are tuples of coordiantes
        '''
        result = {}
        for x, y in self.cells:
            nbrs = [(x-1, y-1), (x, y-1), (x+1, y-1),
                    (x-1, y),  (x+1, y),
                    (x-1, y+1), (x, y+1), (x+1, y+1)]
            for a, b in nbrs:
                if result.has_key((a,b)):
                    result[(a,b)] += 1
                else:
                    result[(a,b)] = 1
        return result
    
    def should_live(self, count, active):
        return (active and (count == 2)) or (count == 3)
    
    def tick(self):
        '''
        Method that moves to the next generation.
        '''
        new_cells = []
        neighbour_relations = self.gen_dict()
        for key, neighbour_count in neighbour_relations.iteritems():
            active = key in self.cells
            if self.should_live(neighbour_count, active):
                new_cells.append(key)
        self.cells = new_cells
        return new_cells