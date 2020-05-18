# Pomoodoro Timer

## description
Python pomodoro timer based on PyQt5

## function

1. Countdown timer
2. Different modes (Study and Break)
3. Notification sound goes off when the timer is done
4. Settings to change the amount of time you want per mode
5. Setting to toggle the notification sound

## what I learned

1. More Python practice.
2. State machines used to design the timer logic and the different modes.
3. How to add sound through PyQt5.
4. Adding images to PyQt5 to make program look better.
5. Asynchronously run a portion of the program while being able to respond to user input.
6. A little more complex use of signals in order to base the program's behavior on the GUI's info rather than initializing more variables which would complicate things further.

## notes

I've made a pomodoro timer before but the one I made was based on an Arduino circuit and wasn't as complex as this one because this one allowed the option to change the amount of time you want per mode and also had a reset button and a notification sound when the timer ends. A problem I had in my other PyQt5 programs was that whenever the program was running, it wouldn't be able to listen to user input signlas because I used python's time library that would completely halt the program. Instead, for this program I used PyQt5's QTime module that would allow the program to asynchronously run the timer while also being able to listen for user input such as when the user wants to pause, reset and ect. Originally, I thought the program was going to be straightforward, but there were a lot of subtle problems that occured when translating my logic into a GUI compatible format.

[Notification Sound Used](https://notificationsounds.com/message-tones/juntos-607)

## images
Home Menu

![Home Menu](https://cdn.discordapp.com/attachments/563283331345678338/712070157941473310/unknown.png)

Settings Menu

![Settings Menu](https://cdn.discordapp.com/attachments/563283331345678338/712070231023157328/unknown.png)
