# cbp-Recursive-Name-Changer
Since I started learning C and using the IDE Code blocks, I have come to hate how the project files work. I'm using this repository as we way to create a script of some kind that will constantly change the name of the of the project within the file soI don't need to mainly change it whenever I rename a code blocks project.

Origins: The origins of the project came about when I was trying to debug some school work on my home laptop. The debug would not work which lead to me writing an entire program using the regular run function to fix any bugs. I asked one of my instructors about the debug issue and he informed me that changing the file names for the project file wouldn't actually change what the project was referenced as internally. I decided that I need to fix tis so I dusted of my powershell scripting skills and decided to start working. I will be updating this documentation as I work on this code. So if this document devolves into incoherent ramblings of a mad man, where will at least be some historical documentation for the future.

Game plan: My first step was to create a c project in code blocks. This project is probably going to go through hell as my testing dummy but as long as the singularity doesn't occur in my life time, I think I'll be ok.

The next step is to figure out how I should write this code. My initial thought was to simply write a powershell script. But an I/O file might be a better choice. Since the cbp files are written in xml, I could use a python library or something to write this function. I'm not sure yet, but I'll defiantly think about it over lunch.

I've decided my best strats is to plan a flowchart out. I'll but it on git once I've completely worked out how to use lucid chart. I'll work on it tonight I think.

So I didn't work on the other night like I though, but, did do some research on libraries for python so I've decided that the best chance for me to get this script working is to use Python, along with OS and XML modules. I'll continue writing the flowchart