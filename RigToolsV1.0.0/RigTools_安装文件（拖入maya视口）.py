import os,sys
import maya.cmds as cmds
import maya.mel as mel

def shelfButtonInstall():
    PATH = os.path.dirname(__file__) 
    PATH = os.path.abspath(PATH).replace('\\','/') 
    print(PATH)

    Label = "RT"
    Script = '''#
import sys
if "{0}" not in sys.path:
    sys.path.append("{0}")

import {1} as RT
import importlib
importlib.reload(RT)

RT_PATH = '{0}'
RT_PATH_Lib = "{0}/RigLibrary"

# 显示UI
if __name__ == "__main__":
    try:
        R.close()  # 如果有相同名称的窗口，则关闭
    except:
        pass
    R = RT.RigTools(RT_PATH,RT_PATH_Lib)
    R.show()
'''.format(PATH, 'RigTools') 

    mel.eval('global string $gShelfTopLevel') 
    gShelfTopLevel = mel.eval('$tmp = $gShelfTopLevel') 

    currentShelf = cmds.tabLayout(gShelfTopLevel, query=True, selectTab=True)
    cmds.setParent(currentShelf)

    iconExt = "png"
    icon = PATH+'/RigTools.png'

    cmds.shelfButton( 
        command = Script,
        annotation = Label,
        label = Label,
        imageOverlayLabel = Label,
        image = icon,
        image1 = icon,
        sourceType = "python"
    ) 

def onMayaDroppedPythonFile(param):
    shelfButtonInstall()
