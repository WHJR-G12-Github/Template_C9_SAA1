import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()

# Load the cloud image


bird=pygame.Rect(100,250,30,30)
groundx=0

while True:
    
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
    
  screen.blit(images["bird"],bird)
  
  # Display the cloud image at [300,150]
  
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
