import pyautogui
import pygame

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    
# These can be freely modified to suit your needs
quickchats = [
    #Game Chat Compliments
    'Amazing Shot, Keep it up! I love you.',
    'Keep doing those passes or whatever... Good Job too.',
    'Thanks a lot!',
    'Good attempt! Better luck next time.',
    
    #Game Chat Apologies
    'I goofed up.',
    'You obviously had no fault in this, none at all...',
    'I assure you I did not mean to do that.',
    'Im just bad.',
    
    #Game Chat Reactions
    'Okay, what the $#@%! is happening.',
    'Obviously meant to do that.',
    'Goalie? Where is he >_>? What are you doing?',
    'My disappointment is immeasurable and my day is ruined.',
    
    #Team Chat
    'The ball is mine',
    'Where the $#@%! is the boost, I need it!',
    'All you buddy, I probably got no boost if im saying this.',
    
    #Shamless Self Promotion
    'https://github.com/RLAlpha49', 
]

buttons = {
    'A': 0,
    'B': 1,
    'X': 2,
    'Y': 3,
    'Left Bumper': 4,
    'Right Bumper': 5,
    'Back Button': 6,
    'Start Button': 7,
    'L. Stick In': 8,
    'R. Stick In': 9,
    'Guide Button': 10,
}

dpad = {
    'Up': (0, 1),
    'Down': (0, -1),
    'Left': (-1, 0),
    'Right': (1, 0)
}

def keybind(button1, button2):
    if joysticks[0].get_button(buttons[button1]) and joysticks[0].get_hat(0) == dpad[button2]:
        return True
    else:
        return False

def quickchat(text, spam=1, team=0):
    if team == 1:
        bool = True
    else:
        bool = False
    for i in range(spam):
        if bool == True:
            pyautogui.press('y')
        else:
            pyautogui.press('t')
        pyautogui.write(text, interval=0.001)
        pyautogui.press('enter')
        print(f'{text}\n')


for controller in joysticks:
    if controller.get_init() == True:
        print(f"\n\n{controller.get_name()} detected")

while True:
    try:
        for event in pygame.event.get():

            # Game Chat Compliments
            if keybind('Y', 'Left'):
                quickchat(quickchats[0], 1, 2)
                break
            
            elif keybind('X', 'Left'):
                quickchat(quickchats[1], 1, 2)
                break
            
            elif keybind('B', 'Left'):
                quickchat(quickchats[2], 1, 2)
                break
            
            elif keybind('A', 'Left'):
                quickchat(quickchats[3], 1, 2)
                break
            
            #Game Chat Apoligies
            elif keybind('Y', 'Down'):
                quickchat(quickchats[4], 1, 2)
                break
            
            elif keybind('X', 'Down'):
                quickchat(quickchats[5], 1, 2)
                break
            
            elif keybind('B', 'Down'):
                quickchat(quickchats[6], 1, 2)
                break
            
            elif keybind('A', 'Down'):
                quickchat(quickchats[7], 1, 2)
                break
            
            #Game Chat Reactions
            elif keybind('Y', 'Right'):
                quickchat(quickchats[8], 1, 2)
                break
            
            elif keybind('X', 'Right'):
                quickchat(quickchats[9], 1, 2)
                break
            
            elif keybind('B', 'Right'):
                quickchat(quickchats[10], 2, 2)
                break
            
            elif keybind('A', 'Right'):
                quickchat(quickchats[11], 1, 2)
                break
            
            # Team Chat
            elif keybind('Y', 'Up'):
                quickchat(quickchats[12], 1, 1)
                break
            
            elif keybind('X', 'Up'):
                quickchat(quickchats[13], 1, 1)
                break
            
            elif keybind('B', 'Up'):
                quickchat(quickchats[14], 1, 1)
                break
            
            #Self Promotion of this code
            elif keybind('A', 'Up'):
                quickchat(quickchats[15], 1, 2)
                break
            
    except Exception as e:
        print(e)
        break
