# Incoming Software Engineer Evaluation

In this repo are a series of coding questions and three quick programming exercises to evaluate where to best place you. Pull this repo and change the upstream branch from the MoonFall one to a personal public repository. A guide on how to do that can be found [here](https://devconnected.com/how-to-change-git-remote-origin/). Please fill out the info section on this page, the complete the quick answer questions below. 

There are also 3 programming challenges written in python 3. If you do not know python you can answer in detailed pseudocode or c++. Detailed descriptions for the tasks are in their folders README files. 

 - [C1: Game of Life](C1/README.md)
 - [C2: Matrix Operations](C2/README.md)
 - [C3: Calculator](C3/README.md)

When you are finished, push the code to your own repo and send the link to maxwildersmith@gmail.com.

---
## Info

Name: Mark Cabrera

Email: markacabrer@cpp.edu

Project you are applying for: Project Phoenix


---
## Quick Answer Questions
For the following questions answer as best you can, if you do not know, either make your best guess or skip the question. These questions are designed to cover all the potential roles for a project so it is not expected to know the answer to all of them. For the short answer ones answer is one or two sentences.

Sample:

Which of these is the number 5?
 - 1
 - 0
> - 5
 - 4

What is one difference between a float and an int?

> An int is a whole integer number while a float can be a decimal value.

### Questions:
---

**General**

What does an activity diagram show?
> A visual aid that shows the flow of a program or how  components of a project should work together. It can have conditions with different paths and different shapes represent specific states.

Which of these languages offers the lowest level of control and fastest execution?
 - Python
 - C#
 - Java
 > - C


What is the purpose of version control systems (VCS) such as Git or Mercurial?

> Version control systems act as a safety net while multiple people work on a project should changes or updates lead to any sort of failure. It allows one to recover past (working) versions of a project.
---
**Embedded Systems**

Which level of cache would be accessible by only a single core on a multi-core chip?
 > - L1
 - L2
 - L3
 - All levels


Explain one difference between any of these 2 protocols: I2C, SPI, UART:

> I2C is a protocol that uses a two wire connection of SDA and SCL while SPI uses a 4 wire conection

What is a feature Java has that C++ does not?
 - Object oriented classes
 - Lambda expressions
 - Data streams
 > - Implicit garbage collection


Name one major concern when developing for embedded systems and edge computing such as a deployed Jetson or Raspberry Pi:

> Managing the limitations of physical resources on these devices. There is typically limited processing and storage capabilities and simply increasing these limits would increase the weight of the device.

Which of the following is a job for the DHCP server?
 - Route packets out to the internet
 - Make particular ports available for access on the inter/intranet
 >  - Assign IP addresses on the network
 - Look up what domain name maps to an address on the internet

---
**Linux**

What does the permission code 777 represent (as used in `chmod 777`)?
owner group others

> The three positions of chmod are read, write and execute. '7' allows the user full permision, so '777' would give permission to read, write, and execute a file.

Which of these commands sets and environment variable in Linux? 
 > - export VAR=val
 - export $VAR=val 
 - echo VAR=val
 - echo $VAR=val


What is one major role of systemd?

> Systemd starts and manages the other Linux programs.

---
**AI**

Which of these network architectures would be best suited for processing text?
 - Convolution Neural Network
 > - Recurrent Neural Network
 - Multilayer Perceptron
 - U-Net


What is one solution to the vanishing gradient problem in backprop?

> Using ReLu as the activation function

What is the traditional flow of interactions for a reinforcement learning agent?
 - Read the current state, take an action, environment updates state
 > - Make a prediction, evaluate the loss from a target, update model with backprop
 - Generate result, compare result to similar objects of the class, improve discriminator and predictor


Briefly describe either branch and bound or dynamic programming:

> Branch and bound is an optimization paradigm that uses a tree to determine cost/value of each job, branching down from a root. It can be traversed depth first or breadth first.

What is the main challenge with implementing A*:
 - Picking the correct heuristic
 - Initialization parameters
 - Solution will not converge
 > - Too long of an execution compared to other common pathfinders
