import pygame
from random import randint

blue=pygame.image.load('BLUE.png')
cyan=pygame.image.load('CYAN.png')
green=pygame.image.load('GREEN.png')
magenta=pygame.image.load('MAGENTA.png')
orange=pygame.image.load('ORANGE.png')
red=pygame.image.load('RED.png')
yellow=pygame.image.load('YELLOW.png')
black=pygame.image.load('BLACK.png')
white=pygame.image.load('WHITE.png')


GREY = (192,192,192)
BLACK     = (  0,  0,  0)                       
RED       = (255,  0,  0)                     
GREEN     = (  0,255,  0)                     
BLUE      = (  0,  0,255)                     
ORANGE    = (255,127,  0)               
CYAN      = (  0,183,235)                   
MAGENTA   = (255,  0,255)                   
YELLOW    = (255,255,  0)
WHITE     = (255,255,255) 
COLOURS   = [ BLACK,  RED,  GREEN,  BLUE,  ORANGE,  CYAN,  MAGENTA,  YELLOW,  WHITE ]
CLR_names = ['black','red','green','blue','orange','cyan','magenta','yellow','white']
figures   = [  None , 'Z' ,  'S'  ,  'J' ,  'L'   ,  'I' ,   'T'   ,   'O'  , None  ]
appendedPics=[black,red,green,blue,orange,cyan,magenta,yellow,white]


class Block(object):                    
    """ A square - basic building block
        data:               behaviour:
            col - column        move left/right/up/down
            row - row           draw
            clr - colour
    """
    def __init__(self, col = 1, row = 1, clr = 1):
        self.col = col                  
        self.row = row                  
        self.clr = clr

    def __str__(self):                  
        return '('+str(self.col)+','+str(self.row)+') '+CLR_names[self.clr]

    def draw(self, surface, gridsize=20):                     
        x = self.col * gridsize        
        y = self.row * gridsize
        CLR = COLOURS[self.clr]
        
        blueT=pygame.transform.scale(blue,(gridsize,gridsize))
        cyanT=pygame.transform.scale(cyan,(gridsize,gridsize))
        greenT=pygame.transform.scale(green,(gridsize,gridsize))
        magentaT=pygame.transform.scale(magenta,(gridsize,gridsize))
        orangeT=pygame.transform.scale(orange,(gridsize,gridsize))
        redT=pygame.transform.scale(red,(gridsize,gridsize))
        yellowT=pygame.transform.scale(yellow,(gridsize,gridsize))
        blackT=pygame.transform.scale(black,(gridsize,gridsize))
        whiteT=pygame.transform.scale(white,(gridsize,gridsize))
        images=[blackT,redT,greenT,blueT,orangeT,cyanT,magentaT,yellowT,whiteT]
        #images=pictures[self.clr]
       # pygame.draw.rect(surface,CLR,(x,y,gridsize,gridsize), 0)
        #pygame.draw.rect(surface, WHITE,(x,y,gridsize+1,gridsize+1), 1)
        surface.blit(images[self.clr],(x,y))



    def move_up(self):
        self.row-=1
    def move_down(self):
        self.row+=1


        

    def drawGreyBlocks(self,screen,gridsize=20):
        x = self.col * gridsize        
        y = self.row * gridsize
        pygame.draw.rect(screen,CYAN,(x,y,gridsize,gridsize),2)

#---------------------------------------#
class Cluster(object):
    """ Collection of blocks
        data:
            col - column where the anchor block is located
            row - row where the anchor block is located
            blocksNo - number of blocks
    """
    def __init__(self, col = 1, row = 1, blocksNo = 1):
        self.col = col                    
        self.row = row                   
        self.clr = 0                          
        self.blocks = [Block()]*blocksNo      
#LEARN ABOUT... auxiliary attributes(attributes that are not accessible from the game template, but exist only inside the class)
#           _colOffsets - list of horizontal offsets for each block, in reference to the anchor block
#           _rowOffsets - list of vertical offsets for each block, in reference to the anchor block
##########################################################################################################################################
# 2. Rename blocksXoffset into _colOffsets and blocksYoffset into _rowOffsets THROUGHOUT THE WHOLE TEMPLATE. 
#    Rename update(self) method to _update(self) to show that it is private. Make the necessary changes THROUGHOUT THE WHOLE TEMPLATE.
##########################################################################################################################################
        self._colXoffset = [0]*blocksNo  #@@
        self._rowYoffset = [0]*blocksNo  #@@

    def _update(self):
        for i in range(len(self.blocks)):
            blockCOL = self.col+self._colXoffset[i] #@@
            blockROW = self.row+self._rowYoffset[i] #@@
            blockCLR = self.clr
            self.blocks[i]= Block(blockCOL, blockROW, blockCLR)

    def draw(self, surface, gridsize):                     
        for block in self.blocks:
            block.draw(surface, gridsize)

    def collides(self, other):
        """ Compare each block from a cluster to all blocks from another cluster.
            Return True only if there is a location conflict.
        """
        for block in self.blocks:
            for obstacle in other.blocks:
                if block.col == obstacle.col and block.row == obstacle.row:
                    return True
        return False
    
    def append(self, other): 
        """ Append all blocks from another cluster to this one.
        """
###########################################################################################
# 9.  Add code here that appends the blocks of the other object to the self.blocks list.
#     Use a for loop to take each individual block from the other.blocks list 
############################################################################################
        for i in other.blocks:
            self.blocks.append(i)

#---------------------------------------#
class Obstacles(Cluster):
    """ Collection of tetrominoe blocks on the playing field, left from previous shapes.
        
    """        
    def __init__(self, col = 0, row = 0, blocksNo = 0):
        Cluster.__init__(self, col, row, blocksNo)      # initially the playing field is empty(no shapes are left inside the field)

    def show(self):
        print("\nObstacle: ")
        for block in self.blocks:
            print (block)

    def findFullRows(self, top, bottom, columns):
        fullRows = []
        rows = []
        for block in self.blocks:                       
            rows.append(block.row)                      # make a list with only the row numbers of all blocks
            
        for row in range(top, bottom):                  # starting from the top (row 0), and down to the bottom
            if rows.count(row)== columns:              # if the number of blocks with certain row number
                fullRows.append(row) # equals to the number of columns -> the row is full
        return fullRows                                 # return a list with the full rows' numbers

    def removeFullRows(self, fullRows):
        for row in fullRows:                            # for each full row, STARTING FROM THE TOP (fullRows are in order)
            for i in reversed(range(len(self.blocks))): # check all obstacle blocks in REVERSE ORDER,
                                                        # so when popping them the index doesn't go out of range !!!
                if self.blocks[i].row == row:
                    self.blocks.pop(i)                  # remove each block that is on this row
                elif self.blocks[i].row <row:
                    self.blocks[i].move_down()


        
#---------------------------------------#
class Shape(Cluster):                     
    """ A tetrominoe in one of the shapes: Z,S,J,L,I,T,O; consists of 4 x Block() objects
        data:               behaviour:
            col - column        move left/right/up/down
            row - row           draw
            clr - colour        rotate
                * figure/shape is defined by the colour
            rot - rotation             
    """
    def __init__(self, col = 1, row = 1, clr = 1):
        Cluster.__init__(self, col, row, 4)
        self.clr = clr
############################################################################################
# 3.  Protect(Rename) variable rot to _rot, as there is no need to access it from outside. 
#     The entire rotation process should be handled INSIDE the object ONLY
############################################################################################
        self._rot = 1
        self._colXoffset = [-1, 0, 0, 1] #@@
        self._rowYoffset = [-1,-1, 0, 0] #@@
        self._rotate() #@@
        
    def __str__(self):                  
        return figures[self.clr]+' ('+str(self.col)+','+str(self.row)+') '+CLR_names[self.clr]

############################################################################################
# 4.  Protect(Rename) method rotate to _rotate, as there is no need to invoke it from outside 
#     the space bar action will be eventually removed
############################################################################################# 

    def _rotate(self):
        """ offsets are assigned starting from the farthest (most distant) block in reference to the anchor block """
        if self.clr == 1:    #           (default rotation)    
                             #   o             o o                o              
                             # o x               x o            x o          o x
                             # o                                o              o o
            _colXoffset = [[-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0], [ 1, 0, 0,-1]] #
            _rowYoffset = [[ 1, 0, 0,-1], [-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0]] #       
        elif self.clr == 2:  #
                             # o                 o o           o              
                             # o x             o x             x o             x o
                             #   o                               o           o o
            _colXoffset = [[-1,-1, 0, 0], [ 1, 0, 0,-1], [ 1, 1, 0, 0], [-1, 0, 0, 1]] #
            _rowYoffset = [[-1, 0, 0, 1], [-1,-1, 0, 0], [ 1, 0, 0,-1], [ 1, 1, 0, 0]] #                                                                    
        elif self.clr == 3:  # 
                             #   o             o                o o              
                             #   x             o x o            x           o x o
                             # o o                              o               o
            _colXoffset = [[-1, 0, 0, 0], [-1,-1, 0, 1], [ 1, 0, 0, 0], [ 1, 1, 0,-1]] #
            _rowYoffset = [[ 1, 1, 0,-1], [-1, 0, 0, 0], [-1,-1, 0, 1], [ 1, 0, 0, 0]] #            
        elif self.clr == 4:  #  
                             # o o                o             o              
                             #   x            o x o             x           o x o
                             #   o                              o o         o
            _colXoffset = [[-1,0,0,0], [1,1, 0,-1], [1, 0, 0,0], [-1, -1, 0,1]] #
            _rowYoffset = [[-1,-1,0,1], [-1,0,0,0], [1,1, 0,-1], [1,0,0,0]] #
        elif self.clr == 5:  #   o                              o
                             #   o                              x              
                             #   x            o x o o           o          o o x o
                             #   o                              o              
            _colXoffset = [[ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0], [-2,-1, 0, 1]] #
            _rowYoffset = [[-2,-1, 0, 1], [ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0]] #           
        elif self.clr == 6:  #
                             #   o              o                o              
                             # o x            o x o              x o         o x o
                             #   o                               o             o 
            _colXoffset = [[ 0,-1, 0, 0], [-1, 0, 0, 1], [ 0, 1, 0, 0], [ 1, 0, 0,-1]] #
            _rowYoffset = [[ 1, 0, 0,-1], [ 0,-1, 0, 0], [-1, 0, 0, 1], [ 0, 1, 0, 0]] #
        elif self.clr == 7:  # 
                             # o o            o o               o o          o o
                             # o x            o x               o x          o x
                             # 
            _colXoffset = [[-1,-1, 0, 0], [-1,-1, 0, 0], [-1,-1, 0, 0], [-1,-1, 0, 0]] #@@
            _rowYoffset = [[ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1]] #@@
        self._colXoffset =_colXoffset[self._rot] #@@
        self._rowYoffset =_rowYoffset[self._rot] #@@
        self._update() #@@

    def move_left(self):                
        self.col = self.col - 1                   
        self._update() #@@
        
    def move_right(self):               
        self.col = self.col + 1                   
        self._update() #@@
        
    def move_down(self):                
        self.row = self.row + 1                   
        self._update() #@@
        
    def move_up(self):                  
        self.row = self.row - 1                   
        self._update() #@@

    def rotateClkwise(self):
        self._rot=(self._rot+1)%4
        self._rotate()
###################################################################################################################
# 5.  Add code here that rotates the shape one step clockwise. Use the rotation section from the previous template
###################################################################################################################

    def rotateCntclkwise(self):
##        if self.clr==1:
##            _colXoffset= [[-1,-1,0,0], [ 1, 0, 0,-1], [ 1, 1, 0, 0], [-1, 0, 0, 1]]
##            _rowYoffset= [[ 1, 0, 0,-1],[ 1, 1, 0, 0],[-1, 0, 0, 1], [-1,-1, 0, 0]]
##
##        elif self.clr==2:
##            _colXoffset=[[-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0],[ 1, 0, 0,-1]]
##            _rowYoffset=[[-1, 0, 0, 1], [ 1, 1, 0, 0],[ 1, 0, 0,-1],[-1,-1, 0, 0]]
##
##        elif self.clr==3:
##            _colXoffset=[[-1, 0, 0, 0],[ 1, 1, 0,-1], [ 1, 0, 0, 0],[-1,-1, 0, 1]]
##            _rowXoffset=[[ 1, 1, 0,-1], [ 1, 1, 0,-1], [ 1, 0, 0, 0],[-1, 0, 0, 0]]
##
##        elif self.clr==4:
##            _colXoffset=[[-1,0,0,0], [-1, -1, 0,1], [1, 0, 0,0], [1,1, 0,-1]]
##            _rowYoffset=[[-1,-1,0,1],[1,0,0,0], [1,1, 0,-1], [-1,0,0,0]]
##
##        elif self.clr==5:
##            _colXoffset=[[ 0, 0, 0, 0], [-2,-1, 0, 1], [ 0, 0, 0, 0], [ 2, 1, 0,-1]]
##            _rowYoffset=[[-2,-1, 0, 1],[ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0]]
##
##        elif self.clr==6:
##            _colXoffset=[[ 0,-1, 0, 0], [ 1, 0, 0,-1],[ 0, 1, 0, 0], [-1, 0, 0, 1]]  
##            _rowYoffset=[[ 1, 0, 0,-1],[ 0, 1, 0, 0], [-1, 0, 0, 1], [ 0,-1, 0, 0]]
##
##        elif self.clr==7:
##            _colXoffset=[[-1,-1, 0, 0], [-1,-1, 0, 0],  [-1,-1, 0, 0], [-1,-1, 0, 0]]
##            _rowYoffset=[[ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1]]
##        self._collXoffset=_colXoffset[self._rot]
##        self._rowYoffset=_rowYoffset[self._rot]
        self._rot=-(self._rot+1)%4
        self._rotate()
        self._update()
##########################################################################################################################
# 6.  Add code here that rotates the shape one step counterclockwise. Use the rotation section from the previous template
##########################################################################################################################


#---------------------------------------#
class Floor(Cluster):
    """ Horizontal line of blocks
        data:
            col - column where the anchor block is located
            row - row where the anchor block is located
            blocksNo - number of blocks 
    """
    def __init__(self, col = 1, row = 1, blocksNo = 1):
        Cluster.__init__(self, col, row, blocksNo)
        for i in range(blocksNo):
            self._colXoffset[i] = i  #@@
        self._update() #@@        
            
#---------------------------------------#
class Wall(Cluster):
    """ Vertical line of blocks
        data:
            col - column where the anchor block is located
            row - row where the anchor block is located
            blocksNo - number of blocks 
    """
    def __init__(self, col = 1, row = 1, blocksNo = 1):
        Cluster.__init__(self, col, row, blocksNo)
        for i in range(blocksNo):
            self._rowYoffset[i] = i #@@
        self._update() #@@

class Shadow(Shape):
    def __init__(self, col , row,clr):
        Shape.__init__(self,col,row,clr)
        self.col=col
        self.row=row
        self.clr=clr
        self.shapes=[Shape()]
        
    def drawGreyBlocks(self,screen,gridsize=20):
        x = self.col * gridsize        
        y = self.row * gridsize
        pygame.draw.rect(screen,CYAN,(x,y,gridsize,gridsize),2)
        
    def draw(self, surface,gridsize):
        for block in self.blocks:
            block.drawGreyBlocks(surface, gridsize)

    def move_left(self):
        self.col-=1
        self._update()

    def move_right(self):
        self.col+=1
        self._update()

    def _rotate(self):
        if self.clr == 1:    #           (default rotation)    
                             #   o             o o                o              
                             # o x               x o            x o          o x
                             # o                                o              o o
            _colXoffset = [[-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0], [ 1, 0, 0,-1]] #
            _rowYoffset = [[ 1, 0, 0,-1], [-1,-1, 0, 0], [-1, 0, 0, 1], [ 1, 1, 0, 0]] #       
        elif self.clr == 2:  #
                             # o                 o o           o              
                             # o x             o x             x o             x o
                             #   o                               o           o o
            _colXoffset = [[-1,-1, 0, 0], [ 1, 0, 0,-1], [ 1, 1, 0, 0], [-1, 0, 0, 1]] #
            _rowYoffset = [[-1, 0, 0, 1], [-1,-1, 0, 0], [ 1, 0, 0,-1], [ 1, 1, 0, 0]] #                                                                    
        elif self.clr == 3:  # 
                             #   o             o                o o              
                             #   x             o x o            x           o x o
                             # o o                              o               o
            _colXoffset = [[-1, 0, 0, 0], [-1,-1, 0, 1], [ 1, 0, 0, 0], [ 1, 1, 0,-1]] #
            _rowYoffset = [[ 1, 1, 0,-1], [-1, 0, 0, 0], [-1,-1, 0, 1], [ 1, 0, 0, 0]] #            
        elif self.clr == 4:  #  
                             # o o                o             o              
                             #   x            o x o             x           o x o
                             #   o                              o o         o
            _colXoffset = [[-1,0,0,0], [1,1, 0,-1], [1, 0, 0,0], [-1, -1, 0,1]] #
            _rowYoffset = [[-1,-1,0,1], [-1,0,0,0], [1,1, 0,-1], [1,0,0,0]] #
        elif self.clr == 5:  #   o                              o
                             #   o                              x              
                             #   x            o x o o           o          o o x o
                             #   o                              o              
            _colXoffset = [[ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0], [-2,-1, 0, 1]] #
            _rowYoffset = [[-2,-1, 0, 1], [ 0, 0, 0, 0], [ 2, 1, 0,-1], [ 0, 0, 0, 0]] #           
        elif self.clr == 6:  #
                             #   o              o                o              
                             # o x            o x o              x o         o x o
                             #   o                               o             o 
            _colXoffset = [[ 0,-1, 0, 0], [-1, 0, 0, 1], [ 0, 1, 0, 0], [ 1, 0, 0,-1]] #
            _rowYoffset = [[ 1, 0, 0,-1], [ 0,-1, 0, 0], [-1, 0, 0, 1], [ 0, 1, 0, 0]] #
        elif self.clr == 7:  # 
                             # o o            o o               o o          o o
                             # o x            o x               o x          o x
                             # 
            _colXoffset = [[-1,-1, 0, 0], [-1,-1, 0, 0], [-1,-1, 0, 0], [-1,-1, 0, 0]] #@@
            _rowYoffset = [[ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1], [ 0,-1, 0,-1]] #@@
        self._colXoffset =_colXoffset[self._rot] 
        self._rowYoffset =_rowYoffset[self._rot] 
        self._update()
        
    def rotateClkwise(self):
        self._rot=(self._rot+1)%4
        self._rotate()

        
    def rotateCntclkwise(self):
        self._rot=-(self._rot+1)%4
        self._rotate()

    def collides(self,other):
        for block in self.blocks:
            for obstacle in other.blocks:
                if block.col == obstacle.col and block.row == obstacle.row:
                    return True
        return False
        

