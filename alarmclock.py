import time
import pygame
import datetime
                                      


def set_alarm(alarm_time):
    print(f'Alarm set for {alarm_time}')
    sound_file = 'tune.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)

    is_running = True
    while is_running:
        current_time = time.strftime("%I:%M %p")
        print(current_time)
        time.sleep(1)

        if alarm_time == current_time:
            print('wake up!!')
            print('press *q* to stop playing')
            pygame.mixer.music.play()
            dec = input(' ').lower()
            if dec == 'q':
                pygame.mixer.music.stop()
                is_running= False
            elif dec != 'q':
                dec = input('press *q* to QUIT...').lower()
                if dec == 'q':
                    pygame.mixer.music.stop()
                    is_running= False
                else:
                    pygame.mixer.music.stop()
                    extend = input('Extend alarm?(y/n): ')
                    if extend == 'y':
                        new_alarm  = input('enter the alarm time (HH:MM AM/PM): ').upper()
                        alarm_time = new_alarm
                        set_alarm(new_alarm)
                    elif extend == 'n':
                        pygame.mixer.music.stop()
                        is_running= False
        elif alarm_time<current_time:
            print(f'The ALARM TIME-{alarm_time} cannot be less than CURRENT TIME-{current_time}')  
            is_running= False   
if __name__ == '__main__':
    alarm_time= input('enter the alarm time (HH:MM AM/PM): ').upper()
    set_alarm(alarm_time)