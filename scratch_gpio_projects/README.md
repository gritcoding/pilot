# Scratch + GPIO lesson

In this lesson, we continue using Scratch, using a special GPIO (General Purpose Input/Output) enabled build. It will be installed on the Raspberry PI.

## Setup instructions
* Have the kids setup the Raspberry PI by connecting the usual connectors (microSD card, HDMI, mouse, keyboard, power).
* You will also connect the header cable to the breakout board, and insert the breakout board into the breadboard.
* Start up the RPI, wait for it to boot.

![Empty Breadboard](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/breadboard_empty.jpg)
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/breadboard_empty.jpg)

![RPI and Breadboard](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/rpi_and_breadboard.jpg)

Through the rest of the lesson, keep the breadboard oriented in a way that the 
lettering on the breakout board is visible to you (i.e. you should see SDA, GND, 
etc).

## Blinking Light
* Take a red LED and a 330 Ohm resistor from the kit, as well as 1 short 
wire.
* Connect one short wire from pin 17 (lower row 6 on the breadboard) to a 
free row on the breadboard, say lower row 22 (yellow cable on picture).
* Take the LED, and connect the longer lead to lower row 22, and the 
shorter lead to lower row 23
* Take the resistor, connect one of its lead to lower row 23, and the other 
one to the "-" side of the 3.3V power rail.
* Now create the scratch project (solution is is 
grit_pilot/scratch_gpio_projects/blinking_led.sb)
 * This is a normal Scratch project, except some variables will be 
intepreted as input/output. In this case, we want to broadcast the events 
pin11high and pin11low alternatively. This will set the voltage to 3.3V for 
high and 0V for low.
 * You should see the blinking red LED when starting the Scratch project if 
everything was connected properly.

![Scratch Code](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/scratch_blinking_light.png)

![blinking_led_setup.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/blinking_led_setup.jpg)
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/blinking_led_setup.jpg)


## Exploding Birds
### Software
The game is similar to angry birds, but with a simpler launch mecanism (angle-based). The bird can explode mid-flight after pressing the push button. Depending on how many monsters were hit, that many LEDs will be lit up. The solution is present in grit_pilot/scratch_gpio_projects/exploding_birds.sb. 

![exploding_birds.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/exploding_birds.jpg)
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/exploding_birds.jpg)

#### The bird
* Import a new sprite with a bird appearance.
* Create a new costume for it, which will look like an explosion, name that costume 'explosion'.
* Go through the script below and explain it bit by bit to the students.

![bird_script.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/bird_script.jpg)
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/bird_script.jpg)

#### The monsters
* Import a monster sprite.
* Create a dead costume for them.
* Go through the logic below and explain it to the students.

![monster_logic.jpg](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/monster_script.jpg)
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/monster_script.jpg)

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
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/three_leds_pushbutton.jpg)

![three_led_pushbutton](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/three_leds_pushbutton_top.jpg)
[zoom-in](https://raw.githubusercontent.com/gritcoding/pilot/master/scratch_gpio_projects/images/three_leds_pushbutton_top.jpg)