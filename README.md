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
