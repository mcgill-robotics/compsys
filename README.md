# CompSys

This package sets up the user's computer to accommodate McGill Robotics'
development environment. This is optional, but **highly recommended**
especially if you are interacting with our robots or the ROS bags in any way.

This will install **ROS Jade Turtle** on **Ubuntu 14.04** along with a set of
other software tools McGill Robotics uses.

## Installation

### 0. Pre-requisites
This package requires *Ubuntu 14.04*. You can follow the
[basic setup](http://mcgillrobotics.com/wiki/index.php/Basic_Setup)
instructions on the wiki. If you are not sure how to do it, ask any software
section leader to help you. *Make sure you have
[set up](https://help.github.com/articles/generating-ssh-keys/) your ssh keys
correctly.*

### 1. Setup
Create a directory to contain all of your McGill Robotics files and `cd` into
it from your terminal.  
This folder will become your `$ROBOTIC_PATH` and will contain both this
`compsys` repository **and** your team repository.

Run the following command:

```bash
git clone git@github.com:mcgill-robotics/compsys.git
cd compsys
./install
```

and follow the on-screen instructions.  
**This may ask for your user's password several times.**

## FAQs

### 1. Am I a robot?
**Do not set this option for personal use.**  
If you are asking yourself this question, the answer is probably no. This
option is there if you want to install this on one of the team robots or on
one of the team's public computers.  
This will `export IAMROBOT` in your `.bashrc` (or `.zshrc`) to `true` or
`false` depending on your answer.

### 2. Which project am I working on?
This will `export ROBOT` in your `.bashrc` (or `.zshrc`) to `auv`, `drone`,
`rover` or `demo` depending on your answer. If you wish to change project
later, you can manually change the `ROBOT` variable in your `.bashrc` (or
`.zshrc`) to your new desired project and `git clone` that project's
repository in your `$ROBOTIC_PATH` directory.

### 3. How do I install ROS?
ROS is the most important part of the McGill Robotics software system, if you
have not installed it yet, this tool will ask if you want to. The complete ROS
package is quite large however, so we recommend you only install it when you
have a stable network connection and about one to two hours to spare. If you
can't install it right away, simply select no. You can install it later by
running the following command:

```bash
cd $ROBOTIC_PATH/compsys
./setup/ros/install
```

### 4. I am upgrading from ROS Indigo Igloo. How should I proceed?
Simply, uninstall ROS Indigo Igloo as such:

```bash
sudo apt-get remove ros-indigo-*
```

and then install ROS Jade Turtle as follows:

```bash
cd $ROBOTIC_PATH/compsys
git pull
./setup/ros/install
```

### 5. Would I like to switch from `bash` to `zsh`?
**Here be dragons.**  
This gives you the option to switch your default shell from Ubuntu's default
`bash` to the more feature-full `zsh` along with `prezto` framework. If you
are still unsure after reading this, simply say no; you can always change your
mind later by installing it manually as such:

```bash
cd $ROBOTIC_PATH/compsys
./setup/zsh/install
./setup/config/install
```

#### Why would I want to?
*Many reasons.*  

The main ones are:
* better auto-completion
* spelling correction
* git integration
* eye candy

For more information, simply look up the differences between `zsh` and `bash`
online.  
Another reason is *all of our robots will be running `zsh`.*

Two things to note though:
  1. You are **not** required to switch to `zsh`. Run whatever you feel
  comfortable with as long as it's compatible with `ROS`.  
  2. Any scripts written in `bash` are largely compatible with `zsh`, but not
  necessarily vice-versa. So be warned.

#### What will my shell look like?
By setting this option, you will be using the custom `mcgill` prompt which
looks like this:
![GitHub Logo](/setup/zsh/mcgill_theme.png)
*Colors and font may vary depending on your terminal settings.*  

#### I don't like it. Please take me back!
Don't sweat, simply run:

```bash
chsh -s /bin/bash
```

and restart.

### 6. I installed `zsh`. Why does `rosrun` autocompletion not work?
Unfortunately, this is a new bug that has been introduced in the latest
versions of ROS. This issue has been fixed, but the fix has not been released
yet. So, you will need to fix it manually, as such:

```bash
git clone -b indigo-devel git://github.com/ros/catkin.git /tmp/catkin
cd /opt/ros/jade/lib/python2.7/dist-packages/catkin
sudo cp /tmp/catkin/python/catkin/find_in_workspaces.py .
```

### 7. I installed `zsh`, and I am missing modules. How do I update it?
`compsys` uses the [prezto](https://github.com/sorin-ionescu/prezto)
`zsh` configuration framework to make things easier. If you run into any
issues (e.g. missing the `autosuggestions` module), you can simply update it.
This will also give you access to other nice goodies :) To update, simply run:

```bash
cd ${HOME}/.zprezto
git pull && git submodule update --init --recursive
```

and launch a new terminal.

### 8. I don't like *something*. Can I change it?
**No.**  
Remember that any change you make can and will change everybody else's
environment. If you wish to make a change, you should be able to overwrite
the option we set in your own `.bashrc` (or `.zshrc`).  
If you think, your change can be beneficial to everyone or if you have any
suggestions or feature requests, open an issue or a pull request and we'll
discuss the change.
