# -*- coding: utf-8 _*_
#Convert-data-format


######################################################
####                                              ####
#### Antonio Galvan  agalvan@astro.unam.mx        ####
#### Interface to give format and style to data   ####
####                                              ####
######################################################

try:
     import wx
except ImportError:
    errorMessage = "Please, check all the dependences for this program\n\t*wxPython"
    raise ImportError,errorMessage


class dataFormat(wx.Frame):

    def __init__(self, parent, id, title):
        
        wx.Frame.__init__(self,parent, id,  title,size=(700, 500))
        self.parent = parent
        self.inicialize()


    def inicialize(self):
        '''
        init method
        '''
        
        #Definition of the sizers
        Top = wx.BoxSizer(wx.VERTICAL)
        title = wx.BoxSizer(wx.HORIZONTAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vboxL = wx.BoxSizer(wx.VERTICAL)
        vboxR = wx.BoxSizer(wx.VERTICAL)
        
        #Definition of the panel
        Tpanel = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        Lpanel = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        Rpanel = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
        
        title.Add(Tpanel, 1, wx.EXPAND | wx.ALL, 3)
        vboxL.Add(Lpanel, 1, wx.EXPAND | wx.ALL, 3)
        vboxR.Add(Rpanel, 1, wx.EXPAND | wx.ALL, 3)
        
        #Stuff of the top panel
        
        wx.StaticText(Tpanel,-1,"A77aque", pos = (10,10))
        
        #Stuff of the left panel
        
        self.textFrame = wx.TextCtrl(Lpanel, -1, size = (350,434), style = wx.TE_MULTILINE)
        
        #Stuff of the right panel
        
        #######################################################################################
        ##                                                                                   ##
        ##                             Configuration of the axis                             ##
        ##                                                                                   ##
        #######################################################################################
        
        wx.StaticText(Rpanel, -1, "Chose any transformation to the x axis", pos = (10,10))
        
        wx.StaticText(Rpanel, -1, "Chose any transformation to the y axis", pos = (10,70))
        
        #######################################################################################
        ##                                                                                   ##
        ##       Options to the X-axis                                                       ##
        ##                                                                                   ##
        #######################################################################################
        
        optionsX = ['None', 'Hz -> eV', 'eV -> TeV']
        self.ChoiceX = wx.Choice(Rpanel, 10 ,choices = optionsX, pos = (10, 30))
        self.ChoiceX.SetSelection(0)
        self.ChoiceX.Bind(wx.EVT_CHOICE, self.OnChoiceX)
        
        ###########
        ##
        ##       Box check if the data was on log
        ##
        ###########
        
        self.logX = wx.CheckBox(Rpanel, id = 100,label = "Check if the x are in log", pos = (130,35))
        self.Bind(wx.EVT_CHECKBOX, self.checkBotton)
        
        
        #######################################################################################
        ##                                                                                   ##
        ##       Options to the Y-axis                                                       ##
        ##                                                                                   ##
        #######################################################################################
        
        optionsY = ['None', 'erg -> TeV', 'Jy -> erg']
        self.ChoiceY = wx.Choice(Rpanel, 11 ,choices = optionsY, pos = (10, 90))
        self.ChoiceY.SetSelection(0)
        self.ChoiceY.Bind(wx.EVT_CHOICE, self.OnChoiceY)
        
        ###########
        ##
        ##       Box check if the data was on log
        ##
        ###########
        
        self.logX = wx.CheckBox(Rpanel, id = 101,label = "Check if the y are in log", pos = (130,95))
        self.Bind(wx.EVT_CHECKBOX, self.checkBotton)
        
        #######################################################################################
        #                                    Type of the data
        #######################################################################################
        
        #Op1 if is only x:y data
        self.Op1 = wx.CheckBox(Rpanel, id=102, label = "points", pos = (10, 130))
        self.Op2 = wx.CheckBox(Rpanel, id=103, label = "x errorbars", pos = (120, 130))
        self.Op3 = wx.CheckBox(Rpanel, id=104, label = "y errorbars", pos = (120, 150))
        self.Op4 = wx.CheckBox(Rpanel, id=105, label = "xy errorbars", pos = (10, 150))
        self.Bind(wx.EVT_CHECKBOX, self.checkBotton)
        
        
        
        #######################################################################################
        ##                                                                                   ##
        ##                                  Botton menus                                     ##
        ##                                                                                   ##
        #######################################################################################
        
        #########################
        ##
        ##   Control bottons
        ##
        #########################
        
        self.buttonLoadText = wx.Button(Rpanel, 1,"Read data", (5,360))
        self.Bind(wx.EVT_BUTTON, self.readData, id = 1)
        
        self.buttonLoadText = wx.Button(Rpanel, 2,"Exit", (195,390))
        self.Bind(wx.EVT_BUTTON, self.exit, id = 2)
        
        self.buttonClear = wx.Button(Rpanel, 3,"Clear box", (100,360))
        self.Bind(wx.EVT_BUTTON, self.clearBox, id = 3)
        
        self.buttonSave = wx.Button(Rpanel, 4, "Save data", (195, 360))
        self.Bind(wx.EVT_BUTTON, self.save)
        
        #######################################################################################
        #                                                                                     #
        #               We put the elements of the interface to the canvas.                   #
        #                                                                                     #
        #######################################################################################
        
        hbox.Add(vboxL, 2.3, wx.EXPAND)
        hbox.Add(vboxR, 2.2, wx.EXPAND)
        Top.Add(title, .5, wx.EXPAND)
        Top.Add(hbox, 5, wx.EXPAND)

        #Display of the window
        self.SetSizer(Top)
        self.Show(True)



    def readData(self, event):
        '''
        Module to read the data from the box
        '''
        data =  self.textFrame.GetValue().encode('ascii','ignore')
        if data != "":
            print data.split("\n")
        else:
            event.Skip()
    


    def clearBox(self, event):
        '''
        Clear the boxtext
        '''
        self.textFrame.SetValue("")

    def OnChoiceX(self, event):
        '''
        Election to do on x-axis
        '''
        print self.ChoiceX.GetSelection()
    
    
    def OnChoiceY(self, event):
        '''
            Election to do on y-axis
            '''
        print self.ChoiceY.GetSelection()
    
    def checkBotton(self, event):
        '''
        Command to check the value box
        '''
        # The box checked from the data input are mutually excluyent
        if event.GetEventObject().GetId() == 102:
            self.Op2.SetValue(False)
            self.Op3.SetValue(False)
            self.Op4.SetValue(False)
        elif event.GetEventObject().GetId() == 103:
            self.Op1.SetValue(False)
            self.Op3.SetValue(False)
            self.Op4.SetValue(False)
        elif event.GetEventObject().GetId() == 104:
            self.Op1.SetValue(False)
            self.Op2.SetValue(False)
            self.Op4.SetValue(False)
        elif event.GetEventObject().GetId() == 105:
            self.Op1.SetValue(False)
            self.Op2.SetValue(False)
            self.Op3.SetValue(False)
        else:
            print event.GetEventObject().GetValue()
    
    
    def save(self, event):
        '''
        Save data
        '''
    
        event.Skip()
    

    def exit(self, event):
        '''
        Method to close the program
        '''
        
        dial = wx.MessageDialog(None, "Do you want close the program?","Confirm", wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION)
        response = dial.ShowModal()
        
        if response == wx.ID_YES:
            self.Destroy()
            quit()


#Main de la aplicacion
if __name__ == '__main__':
    app = wx.App()
    frame = dataFormat(None, -1, "pdf digitalizer format")
    app.MainLoop()
