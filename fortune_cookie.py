import random

ask_cookie_yes = True
#ask_cookie_no = False

while(ask_cookie_yes):
    lucky_num = random.randint(1, 100) # lucky num to be displayed on the final output msg
    lucky_text_num = random.randint(1, 5) #num to select what text to display
    lucky_text = '' #empty string that updates 

    if lucky_text_num == 1:
        lucky_text = 'You will be rich today!'
    elif lucky_text_num == 2: 
        lucky_text = 'Time ahead may be dangerous. Keep Caution!'
    elif lucky_text_num == 3: 
        lucky_text = 'Good moments are coming. Be patient.'
    elif lucky_text_num == 4: 
        lucky_text = 'There are demons lurking around. Be careful of who to trust.'
    elif lucky_text_num == 5: 
        lucky_text = 'Big change is coming. YOU should be happy about it.'

    ask_for_cookie = str(input('Do you want a fortune Cookie, Yes or No?\n').lower())

    if ask_for_cookie == 'yes' or ask_for_cookie == 'y':
        print(f'\n{lucky_text} \nYour lucky number is {lucky_num}')
        print('------------------------------------------------------------------')
    elif ask_for_cookie == 'no' or ask_for_cookie == 'n':
        print('\nNo fortune cookie for you...')
        print('------------------------------------------------------------------')
        break
            


# if ask_for_cookie == 'yes' or ask_for_cookie == 'y':
#     print(f'{lucky_text} \nYour lucky number is {lucky_num}')
# if ask_for_cookie == 'no' or ask_for_cookie == 'n':
#     print('No fortune cookie for you...')


    
    

