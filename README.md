# Engineering_4_Notebook
My E4 stuff. Documentation, code, etc, it's all here.

## Python
Check out the Python folder for details on my Python assignments.

## Bash and GPIO

### Intro to GPIO pins and Bash
Can I just say, Bash is *disgusting* after using Python so long. Like, *abhorrent*. Anyway, I suppose we'll have to use it at some point, so I learned the very basics of how it works and wired up a basic LED-on-a-breadboard. Except this time, there were *two* LEDs! Exciting stuff. They were both connected to one pin on the pi so that I could control both at once. I then created a horrible (but functional) Bash script that blinked the LEDs 10 times. The main thing I learned was Bash syntax. Going in, I had no knowledge of the syntax at all. I still don't have an extremely deep understanding of the language, but it's an improvement.

### GPIO pins, cont.
Thank God. I missed Python. For this assignment, I simply created a program that would blink the LEDs in Python rather than Bash. To do this, I needed to use the GPIO module in Python, but this didn't do much besides adding in a bit of new syntax to learn. These GPIO commands are taking me back to the old Arduino assignments...

### Intro to SSH
In order to connect my pi to SSH, I first needed to get its IP address. This was fairly simple. I just typed the command `hostname -I` into Terminal, getting the pi's IP adddress as a result. Next, I enabled SSH on my pi by going into its interfacing options (`sudo raspi-config` > Interfacing Options > SSH > Enable > Yes). I then used the chrome extension [Secure Shell App](https://chrome.google.com/webstore/detail/secure-shell-app/pnhechapfaindjhompbnflcldabbghjo?hl=en) to connect to my pi remotely by giving Secure Shell the pi's address. I could then turn the LEDs from before on and off (using the same code), but this time with the pi no longer connected to my computer. With this new knowledge, I can do real pi stuff like, for example, controlling a boat from 50 feet away. Also, I realized that using a phone hotspot for my pi is probably a bad idea, as the IP address on the pi can change. I gotta fix that sometime.

### Intro to I2C
For this assignment, I needed to use some of the fancy tools that came with my pi. Specifically, the `Adafruit_Python_LSM303` and `Adafruit_Python_SSD1306`; an accelerometer and an OLED display. First, I downloaded the proper libraries onto my pi, then ran a test where the accelerometer would `print` its readings out onto my SSH terminal. Then, I ran an example program from the `Adafruit_Python_SSD1306` library (the OLED screen) which drew simple shapes and text. Now, I (as well as my partner, [Meg](https://github.com/mgist56)) could move on to the real assignment: `print` the accelerometer results onto the OLED display! 

We started off by copy-pasting the code for the screen onto a new file, called `I2C_intro.py`. Then, we started the tedious progress of trying to decipher how the code worked and how to implement the relatively simple accelerometer code so that it would be printed onto the screen instead of to my SSH terminal. The meat of the code was a `while` loop which would first collect data from the accelerometer. It would then `write` said data on the screen. 

We quickly ran into an issue. The text, after being printed, didn't go anywhere, so it kept looping and overlapping text on text. Easy fix, right? Just throw in a `disp.clear()`? Wrong. Turns out, `disp.clear()` turns off all the lights on the screen, but the actual data of what the screen ought to look like remains unchanged. So things were still overlapping, but the screen was also flashing black with every loop. Turns out what we needed to do was create a black rectangle over the whole screen (well, that was at least the solution we came up with), making the text go on, then emptiness covers it up, then the next set of results come in, etc, etc. The other major issue we ran into was the screen simply refusing to turn on. Gave us a serious headache, but it turned out that we just had a slight syntax mistake.

Meg and I learned tons of new syntax for this assignment. The screen and accelerometer we used had lots of new commands to learn. Truth be told, we didn't really understand how some parts of it worked, but the job was complete, so the real learning would have to come during our next assignment: Headless.