*Utrecht Experiment Design 2022*

# Project canvas

### POP

+ **Purpose**: to make the project requirements, boundaries, and goals as concrete as possible  
+ **Outcome(s)**: list your project steps, the best possible outcome, and the minimum desired outcome  
+ **Process**: self-reflection and discussion with your mentors

PROJECT NAME: Vacuum Cannon

TEAM: Mantas, Trey and Matthijs

## Project description  
The premise of our experiment is to create a vacuum cannon that does not require a vacuum pump that can propel ping pong balls or other projectiles at high speeds due to ambient air rushing into fill the vacuum in the tube, pushing the ball to the other end.
There is some evidence that suggests that these projectiles can reach supersonic speeds even though the theory prohibits this. We desire to build a robust dataset by measuring speed and impact force that can perhaps shed more light on whether these models correctly depict the projectile velocity.
Here is an example of a similar cannon that we are modeling ours after. https://www.youtube.com/watch?v=9ydJXOTf1-4
### Open Hardware and its purpose
We are not using any direct open hardware, so will have to build and fabricate all of the materials required for our experiment ourselves. 

### Potential users of the hardware and its added value
We think there is numerous applications to such a vacuum cannon, such as launching probes in space where a vacuum may be easily attainable. This understanding of the airflow into a vacuum could also have numerous implications for aerospace engineering and other applications.
In addition, the vacuum cannon we are creating is very cheap and easy to create, and therefore could be something that may have some use for any system requiring a piston action, that can easily use energy stored by hand (using a handle or crank to pull back the action)

### Underlying physics and working principles
- According to some models the theoretical maximum velocity is independent of the vacuum cannon diameter and projectile mass and is significantly lower than the speed of sound. Some experimental sources have suggested that this may indeed not be the case.
- The problem can be set up as a simple difference in pressure that accelerates the projectile and with constant acceleration this would predict that the speed would depend only on tube length. The actual situation is somewhat more complicated, because the air pressure must accelerate not only the projectile but also the air column behind the projectile.
- Beginning with F = dP/dt , we obtain PA = d/dt {(m + ρxA)v}
- Setting up the theory this way we obtain a formula for the velocity v(x) = vmax [x/(x + λ)sqrt(1 + 2λ/x)] where λ is characteristic length m/pA.
- However this theory already contains many assumptions - That the projectile fits —and seals— the barrel perfectly, and thateffects due to friction, viscosity, and compressibility are negligible. If our experiment does not fit the expected results we will attempt to see which of these estimations - or perhaps a different error - is responsible.


### Required components and planned alteration to the reported recipe
- Two pipes that fit within each other
- A brace and bracket system to secure the cannon
- Projectile - pingpong balls
- O-rings and material to create a seal in the tube
- A ratchet and puly system to pull back the inner tube
- Breakaway seals for the vacuum side of the tube - aluminum foil and tape
- Arduino
- Laser gates or high speed optical cameras
- Piezosensors
Here is an example of some of the materials we can create and use in our experiment https://www.youtube.com/watch?v=BCZGWvieJ7I

### Chosen method of interfacing with a computer
Our sensors will be monitored and recorded by the computer. We could also potentially have the system be pulled back by a motor connected to a computer, but this would be a secondary objective as it is not at all necessary to achieve our goals.

### Planned measurements
Velocity measurements from optical sensors
Force measurements from impact sensors
Volume and mass measurements for our experimental setup

## Mid-course review of your project state (fill this mid-course)
*Note what progress you have made and what adjustments you need to make to finish your project in time.*

Thanks to the generosity of Vin from NPEC we were able to utilise the high speed camera, but he needed his lens back before he left in November and won't return with it until January.

We could not complete the trigger due to unforseen circumstances, so we proceeded to collect 4 data runs before the barrel of the cannon cracked, rendering it unsafe to operate.
We're looking to get another barrel to demonstrate for the end presentation.

In the mean time, we're working on analyzing the data we have and refining our documentation.


## Final review of the project accomplishments (fill at the end of the course)

+ list the achievements of your project  
+ write down your plans for improving your project or making it more widely accessible

We would actually purchase supplies, like precision tubing with thicker walls, to make the cannon.

The biggest difference that would return the most value is a camera like a Phantom so we could add an order of magnitude or three to the frame rate to see the shock effects.
