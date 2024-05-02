"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 9
    April 30 2024

    ------
    Description:    Silent Auction - Pass the console bidding
    ------
    
    ------
    Inputs:         Console input (bids)
    ------
    
    ------
    Outputs:        Console output (winner)
    ------
    
    ------
    Dependencies:   Os 
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

import os # needed for clearing the console

def main():

    """
    
    Description -   Run auction display winner
    ----------
    Input -         Console
    ----------
    Output -        Console
    -------

    """ 
    
    art = """
                                                                                                 
 ad88888ba   88  88           88888888888  888b      88  888888888888                        
d8"     "8b  88  88           88           8888b     88       88                             
Y8,          88  88           88           88 `8b    88       88                             
`Y8aaaaa,    88  88           88aaaaa      88  `8b   88       88                             
  `"xxxx8b,  88  88           88xxxxx      88   `8b  88       88                             
        `8b  88  88           88           88    `8b 88       88                             
Y8a     a8P  88  88           88           88     `8888       88                             
 "Y88888P"   88  88888888888  88888888888  88      `888       88                             
                                                                                             
                                                                                             
                                                                                             
       db        88        88    ,ad8888ba,  888888888888  88    ,ad8888ba,    888b      88  
      d88b       88        88   d8"'    `"8b      88       88   d8"'    `"8b   8888b     88  
     d8'`8b      88        88  d8'                88       88  d8'        `8b  88 `8b    88  
    d8'  `8b     88        88  88                 88       88  88          88  88  `8b   88  
   d8YaaaaY8b    88        88  88                 88       88  88          88  88   `8b  88  
  d8""""""""8b   88        88  Y8,                88       88  Y8,        ,8P  88    `8b 88  
 d8'        `8b  Y8a.    .a8P   Y8a.    .a8P      88       88   Y8a.    .a8P   88     `8888  
d8'          `8b  `"Y8888Y"'     `"Y8888Y"'       88       88    `"Y8888Y"'    88      `888  
                                                                                             
                                                                                             
    """
    
    bid_winner, largest_bid = auction_loop( art )
    
    print(art)
    
    print(f'And the winner is.. {bid_winner}')
    
    print(f'{bid_winner} owes: {largest_bid}')
        

def auction_loop( art ):
        
    """
    
    Description -   Requests bids and names, finds winner
    ----------
    Pseduo Code -
    ----------
    
        # if there are no other bidders, calculate winner 
            # loop through dict to see who made the highest bid          
            # look up the name of the person who made that large bid amount        
            # display the winners information into the console
            
        # if there are more bidders, take down their name and bid amount    
            # ask their name       
            # ask their bid amount     
            # add name and bid amount into the dictionary
            
    ----------
    Input -        Name, bid amount
    ----------
    Output -       winners name, and the winning bid
    -------

    """ 
        
    bids = {} # holds name and amount of bid 
    bid_winner = 'Nobody.'
    end_loop = False
    
    while end_loop == False:    
        
        print(art)
        more_bidders = request_yes_or_no()
        
        if more_bidders == 'no': # loop ends
            
            if bids == {}:
                print(art)
                print('This item did not get any bids')
                
            else: 
                bid_amounts = bids.keys()           
                largest_bid = 0
                
                for bid in bid_amounts:            
                    if bid >= largest_bid:
                        largest_bid = bid   
                        
                bid_winner = bids[largest_bid]  
                return bid_winner, largest_bid

            end_loop = True # Script will end here

        if more_bidders == 'yes': # loop continues    
            print(art)
            name = input('Bidder name: ')                 
            amount = request_amount( name )      
            bids[amount] = name        
            os.system('clear')
            
        #print(bids)
    
    
def request_amount( name ):
    
    """
    
    Description -   Input func modified to only integers certain values,
    ----------
    Input -         User input
    ----------
    Output -        error messages in console, or acceptable response using input func to be saved to var in main
    -------

    """ 
            
    while True:
        
        try:
            
            user_input = int( input( f'Place your bid, {name}: ' ) ) # parse string into int
            
            if type(user_input) == int:
            
                        return user_input
            
            else:
                print('Type a number')
            
        except ValueError:
            
            print( "Try again." )
            
            continue
                
def request_yes_or_no():
        
    """
    
    Description -   Input func modified to only accept yes or no
    ----------
    Input -         User input
    ----------
    Output -        error messages in console, or acceptable response using input func to be saved to var in main
    -------

    """ 
 
    while True:

        user_input = input( 'Does anybody want to place a bid? ' ) # parse string into int
        
        if user_input == 'yes':
            
            return user_input
                
        elif user_input == 'no':
            
            return user_input
        
        else:
            print('Please type either yes or no.')
    
            continue
    
    
if __name__ == '__main__':
    main()