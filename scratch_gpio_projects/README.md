# Scratch + GPIO lesson

In this lesson, we continue using Scratch, using a special GPIO (General Purpose Input/Output) enabled build. It will be installed on the Raspberry PI.

## Setup instructions
* Have the kids setup the Raspberry PI by connecting the usual connectors (microSD card, HDMI, mouse, keyboard, power).
* You will also connect the header cable to the breakout board, and insert the breakout board into the breadboard.
* Start up the RPI, wait for it to boot.

![Empty Breadboard](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/breadboard_empty.jpg)

![RPI and Breadboard](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/rpi_and_breadboard.jpg)

Through the rest of the lesson, keep the breadboard oriented in a way that the 
lettering on the breakout board is visible to you (i.e. you should see SDA, GND, 
etc).

## Blinking Light (Introduction)
* Take a red LED and a 330 Ohm resistor from the kit, as well as 1 short 
wire.
* Connect one short wire from pin 17 (lower row 6 on the breadboard) to a 
free row on the breadboard, say lower row 22 (yellow cable on picture).
* Take the LED, and connect the longer lead to lower row 22, and the 
shorter lead to lower row 23
* Take the resistor, connect one of its lead to lower row 23, and the other 
one to the "-" side of the 3.3V power rail.
 * You can explain to the students that the resistor slows down the current, to prevent the LED from burning out.
* Use the **ScratchGPIO 6** icon on the deskstop to start up scratch.
* Now create the scratch project (solution is in 
grit_pilot/scratch_gpio_projects/blinking_led.sb)
 * This is a normal Scratch project, except some variables will be 
intepreted as input/output. In this case, we want to broadcast the events 
pin11high and pin11low alternatively. This will set the voltage to 3.3V for 
high (LED on) and 0V for low (LED off).
 * You should see the blinking red LED when starting the Scratch project if 
everything was connected properly.

![Scratch Code](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/scratch_blinking_light.png)

![blinking_led_setup.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/blinking_led_setup.jpg)


## Exploding Birds (Morning)
### Software
The game is similar to angry birds, but with a simpler launch mecanism (angle-based). The bird  is first oriented with the left/right arrow keys, then launched with the space bar, and can explode mid-flight after pressing the push button. Depending on how many monsters were hit, that many LEDs will be lit up. The solution is present in grit_pilot/scratch_gpio_projects/exploding_birds.sb. 

![exploding_birds.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/exploding_birds.jpg)


#### The bird
* Import a new sprite with a bird appearance.
* Create a new costume for it, which will look like an explosion, name that costume 'explosion'.
* Go through the script below and explain it bit by bit to the students.

![bird_script.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/bird_script.jpg)

You may break it down the following way:
* First, let's figure out how to orient the bird, by rotating left and right based on key presses.
* Then, add a handling for the space key, and setup the launch broadcast.
* Add the "when I receive launch" block
* Add the movement loop.
 * we want to move forward a little bit, with the **move 10 steps** block
 * we want to rotate 1 degree everytime to simulate a drop due to gravity. After rotating, the bird will continue on a downward trajectory.
* Finally, add the "Explode" mechanism
 * Play sound
 * Switch costume to the explosion sprite (this is another costume for the bird, which you'll have to draw beforehand)
 * And add the animation loop, making the sprite look progressively bigger.
* When they try the game and realize the bird doesn't go back to its starting position correctly, explain that we need to reset the state using the **set x to** and **set y to** commands.

#### The monsters
* Import a monster sprite.
* Create a dead costume for them.
* Go through the logic below and explain it to the students.

![monster_logic.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/monster_logic.jpg)

You may break it down the following way:
* First, let's make the monster move up and down, but only while we are not touching the bird.
* Then, change costumes when we are dead.
* Finally, add the **broadcast** block, to turn on the LED associated with that monster.

Once you're done with one monster, you'll have to duplicate it 2 times, and change the pins for the LEDs for those two new monsters.

### Hardware setup
* Take 2 additional red LEDs and 2 additional 330 ohm resistors
* Connect short wire from breakout pin 22 (lower row 8 on breadboard) to 
lower row 24, row e.
* Insert long lead of LED into 24,d and short lead into 25,d.
* Insert resistor between 25,a and the "-" side of the 3.3V power rail
* Repeat this with a second set of wire, LED and resistor, with the wire 
gonig from 16,c to 26,e, the LED between 26,d and 27,d, and the resistor 
between 27,a and the "-" side of the 3.3V power rail.
* You should have 3 LEDs side by side. The pin numbers you need to use in 
ScratchGPIO are the following, in order: pin11, pin15, pin31. (the pin 
numbering follows no logic at all. The assignments are in the Vilros Raspberry PI manual, page 158. The Pin# column indicates what ScratchGPIO expects - i.e. pin11 while as the second one indicates the labelling on the breakout board - i.e. GPIO17).
* take a push button, and place on pins 28,e-30,e as well as 28,h-30,h. 
When pushing the button, contact will be made between bins 28,e and 30,e 
together, and similarly between 28,e and 30,e together. 
* Take a longer wire and connect it to breakout board pin 4, 4,c. Connect 
the other end to 28,i 
* Connect a 330 Ohm resistor between 30,c and the 3.3V ground ("-" side of 
the 3.3V power rail)
* To read the push button state, we'll have to read sensor value pin7. 1 
means the button is not pressed, and 0 means it's pressed. When displaying 
the sensor value on the screen, you can see its value change as you press 
the button.

![three_led_pushbutton](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/three_leds_pushbutton.jpg)

![three_led_pushbutton](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/three_leds_pushbutton_top.jpg)

If everything is working properly, you can orient your bird with left/right arrow, launch it with the space bar, then trigger the explosion with the push button, and depending on how many monsters you hit, you will see 0,1,2,3 LEDs light up.

### Extra Credit
If the kids are done early, they may be customizing their game already, adding additional graphics and things like that, so you can let them. If they need suggestions, consider the following:
* Place monsters on the screen randomly at startup using random numbers.
* Implement some logic in the monsters so that they try to avoid the bird.
* Add animation when a monster dies, maybe jump up, do a backflip and then switch to dead costume.

## Bird Vs Monster (Afternoon)
In this project, we are building an angry bird game where the bird is launched and must try to hit the monster. The monster is played by another player and can be moved up and down using two push buttons.

### Hardware setup
* Compared to the previous setup, we are removing all LEDs, and adding another push button.
* Connect a pushbutton on breadboard pins 23,e-25,e and 23,h-25,h
* Connect a 330 ohm resistor between 3.3V - and 25,e
* Connect a wire between 11,c and 23,i
* The newly connected push button can be accessed using sensor value 21 in scratch.

![two_pushbuttons.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/two_pushbuttons.jpg)

### Software

The solution is in grit_pilot/scratch_gpio_projects/bird_vs_monster.sb

![bird_vs_monster_scratch.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/bird_vs_monster_scratch.jpg)

* The bird logic is similar to before, except it doesn't explode and doesn't listen to any sensor input.
* The monster, instead of moving up and down sequentially, moves up and down based on button press states.

![monster_move_up_down_script.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/monster_move_up_down_script.jpg)

### Extra Credit
* Make sure the monster cannot move beyond the edges of the screen.
* Include an announcement after the end of the game to indicate whether the bird won or the monster won.
* Make the bird chase the monster automatically using some logic after launch.

## Reference materials
The ScratchGPIO website says: ***As it comes, six pins are set to be used as outputs (Pins 11,12,13,15,16 and 18) and all the rest as simple inputs (22,7,3,5,24,26,19,21,23,8 and 10)***.

These numbers refer to the **Pin #** table in the Vilros manual page 158. To get the pin number on the breakout board, look at the **Name** column.