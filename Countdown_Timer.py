
#-----------------------------Countdown Timer--------------------------------


import time

def countdown(user_time):
    
    while user_time >= 0:
        
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\t", timer, end='\r')
        time.sleep(1)
        user_time -= 1
   
    print('\tStop!!!')


if __name__ == '__main__':

    print("------------Welcome to Countdown Timer------------")
    
    while True:
        
        user_time = int(input("Enter a time in seconds: "))
        countdown(user_time)
        
        ch = input("Do you want to run the timer again?[y/n]: ")
        ch = ch.lower()
        if ch != 'y':
            break

