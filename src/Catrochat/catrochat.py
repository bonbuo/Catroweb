import sys
import pathlib
import os
script_path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(os.path.abspath(script_path))
#from catrochat_simple import CatrochatSimple as Cc_simple

if __name__ == "__main__":
    #print(pathlib.Path(__file__).parent.resolve())
    #print('another one')
    #print(0)
    #catrochat_version = Cc_simple()
    #user_query = sys.argv[1]
    #print(user_query)
    #print(catrochat_version.answer_user(user_query))

   response = "<br> Exit Stage Brick: Exits the program and continues the workflow in the programing view." + "<br>"
   response = response + "You can find additional info <a href = 'https://wiki.catrobat.org/bin/view/Documentation/BrickDocumentation/ExitStageBrick/'> here </a> <br>"
   response = response + "__________________________________________________________________________________________________<br>"
   response = response + "Here are additional relevant search results for your question:<br>"
   response = response + "<ul>"
   counter = 0
   while counter < 4:
       if counter > 0:
           response = response + "<li>"
           response = response + "Set Tempo Brick: This brick sets the tempo of the notes played. A higher tempo correlates to a the notes beeing played faster."+ "<br>"
           response = response + "<a href= 'https://wiki.catrobat.org/bin/view/Documentation/BrickDocumentation/SetTempoBrick/'> Details </a>"
           response = response + "</li>"
       counter = counter + 1
   response = response + "</ul>"
   response = response + "__________________________________________________________________________________________________<br>"


   print(response)


