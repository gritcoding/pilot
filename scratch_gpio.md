# Scratch + GPIO lesson

In this lesson, we continue using Scratch, using a special GPIO (General Purpose Input/Output) enabled build. It will be installed on the Raspberry PI.

## Setup instructions
* Have the kids setup the Raspberry PI by connecting the usual connectors (microSD card, HDMI, mouse, keyboard, power).
* You will also connect the header cable to the breakout board, and insert the breakout board into the breadboard.
* Start up the RPI, wait for it to boot.
**insert picture**

Through the rest of the lesson, keep the breadboard oriented in a way that the 
lettering on the breakout board is visible to you (i.e. you should see SDA, GND, 
etc).

## Blinking Light
* Take a red LED and a 330 Ohm resistor from the kit, as well as 1 short 
wire.
* Connect one short wire from pin 17 (lower row 6 o the breadboard) to a 
free row on the breadboard, say lower row 22 (yellow cable on picture).
* Take the LED, and connect the longer lead to lower row 22, and the 
shorter lead to lower row 23
* Take the resistor, connect one of its lead to lower row 23, and the other 
one to the "-" side of the 3.3V power rail.
* Now create the scratch project (solution is is 
grit_pilot/scratch_gpio_projects/blinking_led.sb)
** This is a normal Scratch project, except some variables will be 
intepreted as input/output. In this case, we want to broadcast the events 
pin11high and pin11low alternatively. This will set the voltage to 3.3V for 
high and 0V for low.
** You should see the blinking red LED when starting the Scratch project if 
everything was connected properly.

**insert picture**
