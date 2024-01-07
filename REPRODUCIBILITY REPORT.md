# Reproducibility report

## Experiment/team: 
Vacuum cannon/ Manstas , Matthijs, Trey

## Reviewers: 
Elpida, Gerasimos, Rimo


------

## Report 

### Documentation:

1. Could you understand the purpose of the experiment? Explain.  
Our objective was to calculate the velocity of a ball moving inside a vacuum cannon, taking into account the frames 
captured and the time taken.
2. Were the safety instructions clear?  
The instructions given were exceptionally clear, providing a detailed explanation of each step accompanied by visual 
aids, including both images and videos.
3. Was the starting point and the expected duration of the measurements clear in the documentation?  
The initial instructions were clearly outlined, although the specific duration was not specified.
4. Does the documentation contain all necessary information to successfully reproduce the measurement? If not, what was missing?
n the documentation, we focused on a particular camera feature (number of frames) as described for modification. It was 
later discovered that the wrong value was used, despite the group mentioning it before we began. Additionally, the requirement for the camera picture to capture the entire setup was found to be inaccurate; capturing only a portion of it proved to be sufficient.

5. Did you get stuck at some point? What extra help did you need to proceed?  
Certainly, we received assistance from the production group to overcome these challenges. They provided specifications 
on how the camera operates, including details on the number of frames and instructions on how to configure the camera to
capture the desired image.

6. Are you encouraged to reproduce previous measurements? How easily could you navigate through the project documentation?  
We utilized the provided software and obtained results that differed from the initial signal obtained by the other group.
7. What can be improved in the documentation?  
Some specific details were provided to prevent getting stuck at the mentioned stages..

**1.5**

On the scale of 1-5 (1: top quality, 5: disappointing) how do you assess the documentation? Please justify your grade based on the questions above.

#### Documentation grade: 1,5

### Measurements:

1. Can you operate the setup with the provided instructions?  
Yes.
2. How close were the results you obtain to the previously reported results?  
They are quite different .
3. Is the analysis procedure easy to understand? Summarize it briefly in your own words.  
The primary software utilized was Tracker. The goal of video tracking is to link target objects across successive video 
frames. Initially, we choose the specific portion of the video we wish to concentrate on. We set the start frame using
the slider and designate the end frame as the point where the ball exits the video frame. To define the area of focus, 
we use a calibration stick, indicating where the frames should be captured. Subsequently, we specify the mass of the 
object to be detected, determining it by selecting its center. This initiates a process where the object is identified 
in different frames, providing us with data on time and velocity. Finally, we export our data into a txt file, which,
along with a Python script, enables us to generate the planned curves.
4. Is the setup robust and safe to operate?  
Yes, safety instructions  were also provided.
5. Did you encounter any issues? Could you troubleshoot those issues without contacting the owners? 
Indeed, we managed to resolve some of the issues on our own, although it took a bit more time..
6. What part of the measurement procedure did you appreciate most?  
Making the setup and getting the results.

**2**

On the scale of 1-5 (1: top quality, 5: disappointing) how do you assess the measurements reproducibility? Please justify your grade based on the questions above.

#### Reproducibility grade: 2

### Interactions:

1. If you had to perform work on this part of the project, would you have selected the same goal or aimed at something else? Please, explain.  
The objective is clearly defined and, in fact, quite intriguing. Another idea would be  to investigate the velocity 
using different shape of objects.
2. Which instructions did you need from the owners on top of the written files?  
While setting up the camera, altering the number of frames proved challenging as it required multiple attempts before being 
accepted from its software. Removing a filter lens, although not specified in the documentation, caused issues with picture detection. 
Additionally, determining the duration for keeping the lamps on and their proximity to the setup raised questions.
3. Does the experiment accomplish its stated purpose?  
Yes.
4. What do you recommend to the project owners to improve their complete package?  
Pay attention to details to prevent minor challenges that may arise

______

### Response to reviewers

_This part must be filled by the project owners based on the peer feedback_

1. Which major adjustments did you make based on this feedback? 

We provided better results, added more extensive safety instructions, finalised lens and FPS used.

2. Do you agree with the graded assessment of the reviewer?  

Yes

$`\textcolor{Green}{\text{1.5}}`$

On the scale of 1-5 (1: really helpful, 5: disappointing) how do you assess the peer evaluation? Please explain.
