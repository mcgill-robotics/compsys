# CompSys

This package sets up the user's computer to accomodate McGill Robotics' development environment. This is optional, but **highly recommended** especially if you are interacting with the robot or the ROS bags in any way.

## Installation

### 0. Pre-requisites
Follow the [basic setup](http://mcgillrobotics.com/wiki/index.php/Basic_Setup) instructions on the wiki.
If you are not sure how to do it, ask any software section leader to help you.

### 1. Setup

Create a directory to contain all of your McGill Robotics files and `cd` into it from your terminal.  
This folder will become your `$ROBOTIC_PATH` and will contain both this `compsys` repository **and** your team repository.

Run the following commmand:

```bash
git clone https://github.com/mcgill-robotics/compsys.git
cd compsys && ./install
```

and follow the on-screen instructions.  
**This may ask for your user's password several times.**

## FAQs

### 1. Am I a robot?
**Do not set this option for personal use.**  
If you are asking yourself this question, the answer is probably no. This option is there if you want to install this on one of the team robots or on one of the team's public computers.  
This will `export IAMROBOT` in your `.bashrc` (or `.zshrc`) to `true` or `false` depending on your answer.


### 2. Which team am I on?
*Really?*  
This will `export ROBOT` in your `.bashrc` (or `.zshrc`) to `auv` or `rover` depending on your answer.

### 3. ROS
ROS is the most important part of McGill Robotics software system, if you have not install it yet, the script will ask to install it.
The full ROS is quite big, so we recommand you only install it when you have a stable network connection and about one to two hours of waiting time.
If you can't install it right now, select no, you can install it later by runnning the following command:

```bash
cd $ROBOTIC_PATH/compsys/setup/config && ./install_ros
```


### 4. Would I like to switch from `bash` to `zsh`?
**Here be dragons.**  
This gives you the option to switch your default shell from Ubuntu's default `bash` to the more feature-full `zsh` along with `prezto` framework. If you are still unsure after reading this, simply say no; you can always change your mind later by installing it manually as such:

```bash
cd $ROBOTIC_PATH/compsys/setup/zsh && ./install
```

#### Why would I want to?
*Many reasons.*  

The main ones are:
* better auto-completion
* spelling correction
* git integration
* eye candy

For more information, simply look up the differences between `zsh` and `bash` online.  
Another reason is *all of our robots will be running `zsh`.*

Two things to note though:
  1. You are **not** required to switch to `zsh`. Run whatever you feel comfortable with as long as it's compatible with `ROS`.  
  2. Any scripts written in `bash` are largely compatible with `zsh`, but not necessarily vice-versa. So be warned.

#### What will my shell look like?
By setting this option, you will be using the custom `mcgill` prompt which looks like this:
![GitHub Logo](/setup/zsh/mcgill_theme.png)
*Colors and font may vary depending on your terminal settings.*  
We recommend the `menlo` font in combination with the `monokai` colorscheme.


### 4. I don't like *something*. Can I change it?
**No.**  
Remember that any change you make can and will change everybody else's environment. If you wish to make a change, you should be able to overwrite the option we set in your own `.bashrc` (or `.zshrc`).  
If you think, your change can be beneficial to everyone or if you have any suggestions or feature requests, open an issue and we'll discuss the change.
