# cbp-Recursive-Name-Changer
Since I started learning C and using the IDE Code blocks, I have come to hate how the project files work. I'm using this repository as we way to create a script of some kind that will constantly change the name of the of the project within the file soI don't need to mainly change it whenever I rename a code blocks project.

Origins: The origins of the project came about when I was trying to debug some school work on my home laptop. The debug would not work which lead to me writing an entire program using the regular run function to fix any bugs. I asked one of my instructors about the debug issue and he informed me that changing the file names for the project file wouldn't actually change what the project was referenced as internally. I decided that I need to fix tis so I dusted of my PowerShell scripting skills and decided to start working. I will be updating this documentation as I work on this code. So if this document devolves into incoherent ramblings of a mad man, where will at least be some historical documentation for the future.

## Game plan: 
My first step was to create a c project in code blocks. This project is probably going to go through hell as my testing dummy but as long as the singularity doesn't occur in my life time, I think I'll be ok.

The next step is to figure out how I should write this code. My initial thought was to simply write a PowerShell script. But an I/O file might be a better choice. Since the cbp files are written in xml, I could use a python library or something to write this function. I'm not sure yet, but I'll defiantly think about it over lunch.

I've decided my best strats is to plan a flowchart out. I'll but it on git once I've completely worked out how to use lucid chart. I'll work on it tonight I think.

So I didn't work on the other night like I though, but, did do some research on libraries for python so I've decided that the best chance for me to get this script working is to use Python, along with OS and XML modules. I'll continue writing the flowchart.

Finished the flowchart. Started to work on the python file but I'm starting to get a head ache. I'll do some more work later

## Program for Python:
 Alright. So I've gotten the python program to change the file path and determine whether the file path works or not so I've gotten that to work. It's not a lot of work but its better then nothing. I would have done more but this what I get for playing dark souls 3. That being said, a thought struck me as I was writing the code. How the hell do I get this to run? I mean, I don't think I can run this through PowerShell as I don't believe it has a python interpreter. My new thought is that I might need to open the interpreter through PowerShell. I'm going to look through VS Code to see how it make sure the terminal opens the interpreter. Perhaps I'll have to write a PowerShell Script to automate this even more. Hell, maybe the end goal for this is creating a Daemon to run inn the background by writing this code. But I doubt I'll be able to do that any time soon. Side note, I need to learn how to spell doubt.

After reading through this article: https://pynative.com/python-delete-files-and-directories/, I've looked through some methods to get rid of the \bin and \obj folders, and it looks like the best method to recursively delete everything would be shtil.rmtree('path') method. This just means I'm have to import shutil. Need to do more search on it. I also forgot to add this link: https://www.guru99.com/manipulating-xml-with-python.html. This will be particularly important when I needs to start reading the xml.

I can delete folders!!!!!!! This will probably bite me in the ass in the future. But small victories. Small victories...

So I can't use wildcard like I want so I'm going to implement the glob library. It's not fun to work with, but I got glob to work. I have finished the easier bit right now. The next major step will be to parse and edit the xml, which wil be new to me. I like what I have so far though.

So here's am interesting pickle. How am I going to change the file? My initial idea was to only read the lines I want with a while loop but I doubt that would actually work. I mean there are plenty of methods I could use, but I'm not  sure what the best would be. I have to think about. Probably shouldn't be doing this during Sharla's class, but there are worse thing's I could do in her class.

I found my holy grail! The "re" module. If I'm right, then I'll be able to replace any bit of text I want. This should be easy as long as I'm able to read the line properly.

I've Done it !!!!! I finished the python Script, I can now change the files I want to change! Now it's time to write the script to launch this.

## The Power of Powershell:
So halfway through making the python script, I realized that I was forgetting to do something really important. My python isn't going to work without the interpreter. So how do I solve this? PowerShell! I'm going to write a PowerShell Script to open the interpretor, and then somehow launch the program I wrote. So how do I do that? No clue! Time to do some research. Probably after class.