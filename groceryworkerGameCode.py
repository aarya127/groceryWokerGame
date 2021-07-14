##
# Pygame base template for opening a window - MVC version
# Simpson College Computer Science
# http://programarcadegames.com/
##
#This program will be a game where user gets to be in the shoes of a grocery worker
#
#@author: Aarya Shah
#@course: ICS3UI-03
#@date: 2020/05/30
#
# Import a library of functions called 'pygame'
import pygame
import random
pygame.init()
import time

#LIST OF COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE= (255,140,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKYBLUE=(135,206,235)

GRAY=(128, 128, 128)
LIGHTBROWN = (255,211,155)
BROWN = (156,102,31)
DARKBROWN = (139,101,8)
GOLD=(255,215,0)
GRAY = (200,200,200)
YELLOW = (255,255,0)
DARK_GRAY = (50,50,50)
REDISH=(139,62,47)


x_speed = 0
y_speed = 0

# Set the height and width of the screen
size =  (1200, 700)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Grocery Worker Game")

# Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 90

#design/backround

def floor():
    for x_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0 +x_offset ,210, 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+x_offset,210, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,240 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,240, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,270 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,270, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,300 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,300, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,330 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,330, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,360 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,360, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,390 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,390, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,420 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,420, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,450 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,450, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,480 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,480, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,510 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,510, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,540 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,540, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,570 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,570, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,600 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,600, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,630 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,630, 80, 30],2)
    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,660 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,660, 80, 30],2)

    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [0+y_offset ,690 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [0+y_offset,690, 80, 30],2)

    for y_offset in range(0, 1250, 80):
        pygame.draw.rect(screen, BROWN, [39+y_offset ,720 , 80, 30],)
        pygame.draw.rect(screen, BLACK, [39+y_offset,720, 80, 30],2)

        #BACK WALL
    pygame.draw.rect(screen, WHITE, [00,0, 1200, 210],)
    pygame.draw.line(screen, RED, [0, 25], [1200, 25],9)
    pygame.draw.line(screen, GREEN, [0, 55], [1200, 55],9)




def machine():
#vending machines
    for y_offset in range(410, 1250, 200):
        pygame.draw.rect(screen, GRAY, [000 +y_offset,10, 190, 210],)

        pygame.draw.rect(screen, SKYBLUE, [6 +y_offset,20, 140, 160],)
        pygame.draw.rect(screen, DARK_GRAY, [6 +y_offset,60, 140, 5],)
        pygame.draw.rect(screen, DARK_GRAY, [6 +y_offset,113, 140, 5],)
        pygame.draw.rect(screen, DARK_GRAY, [6 +y_offset,173, 140, 5],)
        pygame.draw.rect(screen, DARK_GRAY, [6 +y_offset,190, 140, 20],)
        pygame.draw.rect(screen, GOLD, [153 +y_offset,80, 30, 50],)
        pygame.draw.rect(screen, BLACK, [153 +y_offset,80, 30, 50],3)
        pygame.draw.rect(screen, SKYBLUE, [153 +y_offset,60, 30, 20],)
        pygame.draw.rect(screen, DARK_GRAY, [153 +y_offset,60, 30, 20],3)

        #books
        pygame.draw.rect(screen, GREEN, [6 +y_offset,20, 30, 40],)
        pygame.draw.rect(screen, RED, [6 +y_offset,20, 30, 40],4)
        pygame.draw.rect(screen, RED, [6 +y_offset,20, 30, 10],)




        pygame.draw.rect(screen, BLUE, [106 +y_offset,20, 30, 40],)
        pygame.draw.rect(screen, DARKBROWN, [106 +y_offset,20, 30, 40],4)
        pygame.draw.rect(screen, DARKBROWN, [106 +y_offset,20, 30, 10],)

        pygame.draw.rect(screen, YELLOW, [6 +y_offset,70, 30, 40],)
        pygame.draw.rect(screen, BROWN, [6 +y_offset,70, 30, 40],4)
        pygame.draw.rect(screen, BROWN, [6 +y_offset,70, 30, 10],)

        pygame.draw.rect(screen, RED, [56 +y_offset,70, 30, 40],)
        pygame.draw.rect(screen, BLACK, [56 +y_offset,70, 30, 40],4)
        pygame.draw.rect(screen, BLACK, [56 +y_offset,70, 30, 10],)

        pygame.draw.rect(screen, ORANGE, [106 +y_offset,70, 30, 40],)
        pygame.draw.rect(screen, DARK_GRAY, [106 +y_offset,70, 30, 40],4)
        pygame.draw.rect(screen, DARK_GRAY, [106 +y_offset,70, 30, 10],)




        pygame.draw.rect(screen, GREEN, [56 +y_offset,130, 30, 40],)
        pygame.draw.rect(screen, BROWN, [56 +y_offset,130, 30, 40],4)
        pygame.draw.rect(screen, BROWN, [56 +y_offset,130, 30, 10],)

        pygame.draw.rect(screen, GOLD, [106 +y_offset,130, 30, 40],)
        pygame.draw.rect(screen, BLACK, [106 +y_offset,130, 30, 40],4)
        pygame.draw.rect(screen, BLACK, [106 +y_offset,130, 30, 10],)




def cashier():
    pygame.draw.rect(screen, DARK_GRAY, [0 ,300, 300, 40],)
    pygame.draw.rect(screen, GRAY, [0 ,340, 300, 30],)
    pygame.draw.rect(screen, DARK_GRAY, [250 ,340, 50, 290],)
    pygame.draw.rect(screen, DARK_GRAY, [0 ,580, 300, 40],)
    pygame.draw.rect(screen, GRAY, [0 ,620, 300, 30],)

    pygame.draw.rect(screen, LIGHTBROWN, [250,400, 50, 100],)
    pygame.draw.rect(screen, BLACK, [250,400, 50, 100],3)


def shelves():
    for y_offset in range(610, 1250, 400):
        pygame.draw.rect(screen, DARK_GRAY, [000 +y_offset,410, 190, 210],)

        pygame.draw.rect(screen,GRAY, [16 +y_offset,420, 150, 160],)
        pygame.draw.rect(screen, DARK_GRAY, [16 +y_offset,460, 150, 5],)
        pygame.draw.rect(screen, DARK_GRAY, [16 +y_offset,513, 150, 5],)
        pygame.draw.rect(screen, DARK_GRAY, [16 +y_offset,573, 150, 5],)
        pygame.draw.rect(screen, DARK_GRAY, [16 +y_offset,590, 150, 20],)

        pygame.draw.circle(screen,ORANGE, [35 + y_offset,440], 20)
        pygame.draw.circle(screen,GOLD, [65 + y_offset,440], 20)

        pygame.draw.circle(screen,GREEN, [145 + y_offset,440], 20)

        pygame.draw.rect(screen, BLUE, [16 +y_offset,530, 50, 40],)
        pygame.draw.rect(screen, GOLD, [46 +y_offset,530, 50, 40],)
        pygame.draw.rect(screen,  RED, [76 +y_offset,530, 50, 40],)






##classes


class Player():
    def __init__(self):
        self.x = 45
        self.y = 360
        self.height = 10
        self.width= 15
        #Collision boxes
        self.hit = pygame.Rect(self.x-13, self.y-45,self.width+25,self.height+15)
        self.arm = pygame.Rect(self.x,self.y+ 40, self.width + 60,self.height+ 40)
        #rectangle movement
        self.change_x = 5
        self.change_y = 0

        self.color = [0,0,0]


    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        self.hit = pygame.Rect(self.x-13, self.y-45,self.width+25,self.height+15)
        self.arm = pygame.Rect(self.x,self.y+ 40, self.width + 60,self.height+ 40)


    #Drawing
    def draw(self, screen):
        #Hitting the box(arms)
        pygame.draw.rect(screen, ORANGE, (self.arm))

        pygame.draw.rect(screen, ORANGE, [self.x + 25,self.y+20, self.width+5, self.height+30],)

        pygame.draw.rect(screen, RED, [self.x + 15,self.y+40, self.width+25, self.height+40],)
        pygame.draw.rect(screen, BLUE, [self.x + 15,self.y+90, self.width+25, self.height+30],)
        pygame.draw.rect(screen,BLACK, [self.x + 15,self.y+130, self.width+25, self.height],)



        pygame.draw.polygon(screen, GOLD, [[self.x + 15, self.y+ 40], [self.x + 55, self.y +40], [self.x + 15, self.y+ 90],[self.x + 55,self.y + 90]], )
        #head
        pygame.draw.circle(screen,ORANGE, [self.x + 35, self.y+20], 20)


        pygame.draw.rect(screen,BLACK, [self.x + 15,self.y, self.width+25, self.height],)


worker_List = []
worker = Player()

worker_List.append(worker)


##Classes for collision
class Customer(Player):


    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, [self.x-13, self.y-35,self.width+25,self.height+25])#(100,200,30,30)
        pygame.draw.rect(screen, ORANGE, [self.x-8, self.y-35,self.width+15,self.height+15])#(105,200,20,20)
        pygame.draw.rect(screen, BLACK, [self.x,self.y-25,self.width,self.height])
        pygame.draw.rect(screen, BLACK, [self.x+8,self.y-25,self.width,self.height])
        pygame.draw.rect(screen, ORANGE, [self.x-8, self.y-12,self.width+15,self.height])#(105,223,20,5)
        pygame.draw.rect(screen, self.color, [self.x-13, self.y-45,self.width+25,self.height+15])#(100,190,30,20)


        pygame.draw.rect(screen,self.color, [self.x-13, self.y-5,self.width+25,self.height+25])#(100,230,30,30)
        pygame.draw.rect(screen, GOLD, [self.x, self.y,self.width,self.height]) #(113,235,5,5, button)

        pygame.draw.rect(screen, BLACK, [self.x , self.y+10,self.width-5,self.height+25])#(100,250,30,5)
        pygame.draw.rect(screen, ORANGE, (self.hit))

#design for item to be stocked
class Objects():
    def __init__(self):
        self.x = 0
        self.y = 400
        self.height = 10
        self.width= 15

        #Collision boxes
        self.obj = pygame.Rect(self.x + 10,  self.y+ 0,  self.width + 35, self.height+ 50)
        self.balls = pygame.Rect(self.x+ 100, self.y +0,self.width+20, self.height + 30)
        #rectangle movement
        self.change_x = 5
        self.change_y = 0

        self.color = [0,0,0]


    def move(self):
        self.x += self.change_x
        self.y += self.change_y



    #Drawing
    def draw(self, screen):
        #Hitting the box
        pygame.draw.ellipse(screen, BLUE, (self.obj), )



object_List = []


object = Objects()

object_List.append(object)


#design for where item will be stocked
class Ballshelv(Objects):

    def draw(self,screen):
       pygame.draw.ellipse(screen,BLACK,(self.balls))


ball_List = []

ball = Ballshelv()
ball_List.append(ball)

#design for item to be stocked
class Shelves():
    def __init__(self):
        self.x = 920
        self.y = 0
        self.height = 0
        self.width= 0
         #Collision boxes
        self.check1 = pygame.Rect(self.x + 106 , self.y +130,self.width+ 30, self.height + 40)
        self.item = pygame.Rect(self.x - 874, self.y + 500, self.width + 50,self.height +40)
         #rectangle movement
        self.change_x = 5
        self.change_y = 0

        self.color = [0,0,0]
        self.check1 = pygame.Rect(self.x + 106 , self.y +130,self.width+ 30, self.height + 40)
        self.item = pygame.Rect(self.x - 874, self.y + 500, self.width + 50, self.height +40)
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):


        pygame.draw.rect(screen, BLACK,(self.check1 ),)


bookcheck_List =[]
bookcheck= Shelves()

bookcheck_List.append(bookcheck)





#design for item to be stocked
class Book(Shelves):

    def draw(self,screen):
           pygame.draw.rect(screen, GOLD, (self.item),)



book_List = []


book = Book()

book_List.append(book)
# List to creat multiple customers/change attributes (Bots)

customer_List1 = []

for i in range(15):
    customer = Customer()
    customer.x = random.randint(-1250,0)
    customer.y = 210
    customer.change_x = random.randint(1,3)

    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    customer.color = [r,g,b]
    customer_List1.append(customer)







class Blockshelv():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.width= 0
        self.blockchecks = pygame.Rect(self.x + 820, self.y + 130, self.width+ 30, self.height  +40)
        self.blockitem = pygame.Rect(self.x + 150, self.y + 630, self.width+ 30, self.height  +40)

         #rectangle movement
        self.change_x = 5
        self.change_y = 0




    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
         pygame.draw.rect(screen, BLACK, (self.blockchecks),)



blockcheck_List =[]
blockcheck= Blockshelv()

blockcheck_List.append(blockcheck)


class Block(Blockshelv):

    def draw(self, screen):
         pygame.draw.rect(screen, GREEN, (self.blockitem),)

block_List =[]
block= Block()

block_List.append(block)


#design for item to be stocked


## MAIN
# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            # User pressed down on a key
            screen.fill(BROWN)
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0



 # Go ahead and update the screen with what we've drawn.

    floor()
    machine()
    cashier()
    shelves()

#Calling objects wih collion boxes
    for block in block_List:
        block.draw(screen)
        block.blockitem = pygame.Rect( block.x + 150,  block.y + 630,  block.width+ 30,  block.height  +40)



    for blockcheck in blockcheck_List:
        blockcheck.draw(screen)
        blockcheck.blockchecks = pygame.Rect(blockcheck.x + 820, blockcheck.y + 130, blockcheck.width+ 30, blockcheck.height  +40)


    for bookcheck in bookcheck_List:
        bookcheck.draw(screen)
        bookcheck.check1 = pygame.Rect( bookcheck.x + 206 ,  bookcheck.y +530, bookcheck.width+ 30, bookcheck.height + 40)


    for book in book_List:
        book.draw(screen)
        book.item = pygame.Rect(book.x - 874, book.y + 500, book.width + 50, book.height +40)


    for object in object_List:
        object.draw(screen)
        object.obj = pygame.Rect(object.x + 10,  object.y+ 0,  object.width + 35, object.height+ 50)

    for ball in ball_List:
        ball.draw(screen)
        ball.balls = pygame.Rect(ball.x+ 690, ball.y + 20,ball.width+20, ball.height + 30)





#make player return if he goes out off screen/calling others it in
    for worker in worker_List:
        worker.draw(screen)
        worker.arm = pygame.Rect(worker.x,worker.y+ 40, worker.width + 60,worker.height+ 40)
        worker.x+= x_speed
        worker.y+= y_speed

        if worker.x>1250:
            worker.x=0


        if worker.x<0:
            worker.x=1200



    for customer in customer_List1:
        customer.draw(screen)
        customer.move()
        customer.hit = pygame.Rect(customer.x-13, customer.y-45,customer.width+25,customer.height+15)


    for customer in customer_List1:
        customer.move()
        customer.draw(screen)


        if customer.x > 400:
            customer.change_x= 0
            customer.change_y= 3

        if customer.y >600:
            customer.change_x = 3
            customer.change_y =0

        if customer.x >1250:
            customer.x=0
            customer.y = 200














##colisions
        if worker.arm.colliderect(customer.hit):
            raise SystemExit(" !!!! YOU WERENT SOCIAL DISTANCING !!!! To play again reset your shell and try again ")

        if worker.arm.colliderect(block.blockitem):
            block.blockitem = pygame.Rect( block.x + 150,  block.y + 630,  block.width+ 30,  block.height  +40)
            block.x+= x_speed
            block.y+= y_speed


        if worker.arm.colliderect(book.item):

            book.item = pygame.Rect(book.x - 874, book.y + 500, book.width + 50, book.height +40)
            book.x+= x_speed
            book.y+= y_speed


        if worker.arm.colliderect(object.obj):

            object.obj = pygame.Rect(object.x + 10,  object.y+ 0,  object.width + 35, object.height+ 50)
            object.x+= x_speed
            object.y+= y_speed

#object disapears
        if ball.balls.colliderect(object.obj):
            object.x+= 1000
            object.obj = pygame.Rect(object.x + 10,  object.y+ 0,  object.width + 35, object.height+ 50)


        if bookcheck.check1.colliderect(book.item):
            book.x+= 1000
            book.item = pygame.Rect(book.x - 874, book.y + 500, book.width + 50, book.height +40)

        if  blockcheck.blockchecks.colliderect(block.blockitem):
             raise SystemExit(" CONGRATULATIONS YOU WIN")
             block.blockitem = pygame.Rect( block.x + 150,  block.y + 630,  block.width+ 30,  block.height  +40)

















    ##Timer
    # Calculate total seconds
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60


    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, BLACK)

    screen.blit(text, [150, 80])

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 3



    if minutes == seconds == 0:
        raise SystemExit(" YOU RAN OUT OF TIME!!! To play again reset your shell and try again")
    # Limit frames per second
    clock.tick(frame_rate)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    screen.fill(BROWN)
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()




