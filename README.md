# CompSys

This package sets up the user's computer to accommodate McGill Robotics'
development environment. This is optional, but **highly recommended**
especially if you are interacting with our robots or the ROS bags in any way.

This will install **ROS Kinetic Kame** on **Ubuntu 16.04** along with a set of
other software tools McGill Robotics uses.

## Installation

### 0. Pre-requisites
This package requires *Ubuntu 16.04*. The **.iso** can be found on the
[Ubuntu download page](http://www.ubuntu.com/download/desktop). You may choose
to install either directly on your machine with a bootable USB or by using a
Virtual Machine. If you are planning on using a VM, be sure you have a powerful
enough computer to handle it. For both methods, there are plenty of quality
online instruction sets and guides for installing Ubuntu.

*Note that McGill students have access to free VMware licenses and downloads*.

Once you have Ubuntu set up, you will need to install `git` and setup your
SSH keys. Open a terminal and issue the following commands to install git:

```bash
sudo apt-get update
sudo apt-get install git
```

Set up your ssh keys for git by following this
[help article](https://help.github.com/articles/generating-an-ssh-key/).
*Make sure you set up your ssh keys correctly. Be sure to follow
the instructions for Linux.*

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

#### git branch for robot specific setup

The install script will invoke the setup script in the robot repository and
setup robot specific settings.

If you would like to checkout to a specific branch of the robot repository,
you can do so by adding `GIT_BRANCH=branch_name` before `./install` as follows:

```bash
GIT_BRANCH=branch_name ./install
```

**Note: This only works if the robot repository is not cloned yet. If the robot
repository exists when the script runs, the robot specific setup will not run,
and you will need to `cd` to the robot repository, optionally checkout to a
branch, and run `./setup.sh` to setup robot specific settings.**

## Functions
### rosworkon
To switch between projects, you can use the function `rosworkon`:

```bash
rosworkon <project> [profile]
```

#### Parameters:
- `<project>`: name of the project you wish to switch to (ex. auv). This
parameter is required.
- `[profile]`: catkin profile of the project you wish to switch to. This
parameter is not required. Leave it empty if you don't know the profile to
use.

### rosconnect
To connect to a remote ROS master, you can use the function `rosconnect`:

```bash
rosconnect [host_name]
```
#### Parameter:
- `[host_name]`: the name of the host you wish to connect to, the host must be
present in your `/etc/hosts` file. This parameter is not required. Leave it
empty to set the roscore to your local host.

## Tmux
CompSys installs and configures [tmux](https://github.com/tmux/tmux/wiki), a
terminator multiplexer, to switch easily between several programs in one
terminal, to detach them (they keep running in the background), and to
reattach them to a different terminal.

tmux is also used in junction with [tmuxinator](https://github.com/tmuxinator/tmuxinator)
to automatically or quickly launches complex tmux sessions.

### Cheat Sheet
#### tmux basics
- Start new session: `tmux`
- Start new session with name: `tmux new -s <name>`
- List all sessions:`tmux ls`
- Reattach most recent disattached session: `tmux a`
- Reattach a specific session: `tmux a -t <name>`
`<name>` can be found by `tmux ls` and can be both string or integer.
- Kill specific session: `tmux kill-session -t <name>`
- kill all sessions: `tmux kill-session -a`

#### Key-bindings
The key-bining prefix is changed from `ctrl-b` to `ctrl-a`.

To use a key-bind shortcut, first hit the prefix `ctrl-a` then hit a specific
character.
- sessions:
```
s             List and switch sessions
$             Rename current session
```
- windows (tabs)
```
c             Create new window
w             List and switch windows
l             Go back to last window
n             Go to next window
p             Go to previous window
,             Rename window
&             Kill window and all pane in that window
1-9           Go to window number 1-9

ctrl-o        retate window
```

- pane
```
|             Split pane vertically
-             Split pane horizontally
!             Move pane into new window
x             Kill pane
SPACE         Toggle between defualt layouts

# Use the arrow key to navigate between panes
# Mutiple keys can be enter in a quick succession
UP            Move to pane on top of the current pane
DOWN          Move to pane below of the current pane
LEFT          Move to pane on the left of the current pane
RIGHT         Move to pane on the right of the current pane

# Use the ctrl + arrow key to navigate between panes
# Subtitute ctrl by alt to move much more
# Mutiple keys can be enter in a quick succession
ctrl-UP       Resize pane up
ctrl-DOWN     Resize pane down
ctrl-LEFT     Resize pane left
ctrl-RIGHT    Resize pane right

```

- misc
```
d             Detach from current session
t             Show current time, press any key to exit
?             List all shortcuts
[             Enter copy mode
]             Paste the last buffer of copy mode
=             List and paste from copy mode buffer, press ctrl-c to exit
ctrl-c        Put the last copy buffer into the system clipboard
```

#### Copy Mode
You can enter copy mode by either hitting the prefix key (`ctrl-a`) then `[`
or use mouse wheel up. Copy mode is indicated by the yellow line number
indicator on the top right.

You can exit the copy mode by pressing `ESC` or `ctrl-c`.

Once in the copy mode, you can use the arrow keys to navigate and use the
following commands directly.
```
ctrl-u       Move page up
ctrl-d       Move page down
0            Go to start of line
$            Go to end of line
SPACE        Start selection
ENTER        End selection and put selected section into copy mode buffer
ESC          Cancel selection
```

#### Mouse Mode
You can use mouse to accelerate tasks:
- Click on a pane to select it
- Drag a pane boarder to resize it.
- Click on a window from the buttom bar to change to that window
- Mouse whell up and down in the bottom bar to cycle between windows
- Mouse wheel up to enter copy mode and scroll up in copy mode.
- Mouse wheel down to scroll down in copy mode. Exit copy mode when scrolled
down to last line.
- Highlight text to put it into copy mode buffer.

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

### 4. Would I like to switch from `bash` to `zsh`?
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

### 5. I installed `zsh`, and I am missing modules. How do I update it?
`compsys` uses the [prezto](https://github.com/sorin-ionescu/prezto)
`zsh` configuration framework to make things easier. If you run into any
issues (e.g. missing the `autosuggestions` module), you can simply update it.
This will also give you access to other nice goodies :) To update, simply run:

```bash
cd ${HOME}/.zprezto
git pull && git submodule update --init --recursive
```

and launch a new terminal.

### 6. I don't like *something*. Can I change it?
**No.**
Remember that any change you make can and will change everybody else's
environment. If you wish to make a change, you should be able to overwrite
the option we set in your own `.bashrc` (or `.zshrc`).
If you think, your change can be beneficial to everyone or if you have any
suggestions or feature requests, open an issue or a pull request and we'll
discuss the change.
