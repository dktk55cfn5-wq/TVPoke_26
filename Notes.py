
# This file is for the porpose of gathering and remembering Imformation

#----------------------------------------------------------------------------

# Colors of importants (RGB)
# + IMPORTANT : 255 is the highest posible number for colors
#   - Black : (0,0,0)
#   - White : (255,255,255)
#   - Pale Peach : (255,215,190)
#   - Magenta : (230,50,210)
#   - Fire Magenta / Pinky Red : (255,40,80)
#   - Red Orange : (255,85,55)
#   - Fire Yellow : (250,150,0)
#   - Gold : (220,200,0)
#   - Cream : (240,230,170)
#   - Teal : (0,200,200)
#   - Pale Blue : (130,200,220)
#   - Dark Blue : (20,70,255)
#   - Navy Blue : (0,0,20)
#   - Purple(Blue) : (110,0,225)
#   - Purple(Crystal) : (100,70,200)
#   - Black(Purple) : (10,0,40)

# Location Hints
#   - x > 50 = Right
#   - x < 50 = Left
#   - y > 50 = Up
#   - y < 50 = Down

# Object Hints
#   + Buttons
#      - Location : (x,y)
#      - Width : int
#      - Hight : int
#      - Text : str
#      - TextColor : (R,G,B)
#      - BackroundColor : (R,G,B)
#   + Images
#      - Location : (x,y)
#      - Width : int
#      - Hight : int
#      - ImagePath : './folder/name'
#   + Labels 
#      - Location : (x,y)
#      - Width : int
#      - Hight : int
#      - Text : str
#      - TextSize : int (Defalt:14)
#      - TextColor : (R,G,B) (Defalt:Black)
#      - BackroundColor : (R,G,B) (Defalt:None)
#      = Example : Label((50,50),40,50,'',20),

#---------------------------------------------------------------
# NOTES
#  - Positions:
#     + relection on eather side
#     + active poke larger and at the bottom
#     + non active poke above active small and in a row
#     + bellow it display the move buttons
#     + above display health and name (other information too)
#  - Backround:
#     + backround should be a poke stadium
#     + if color it should be a subdued green
#  - Methods:
#     + 
