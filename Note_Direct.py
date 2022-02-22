import subprocess

import gi
import os
import re
import Main_Thread

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SignalHandler:
    @staticmethod
    def onDestroy(self, *args):
        Gtk.main_quit()


class Note_Direct:
    def __init__(self, builder):
        self.builder = builder
        self.Direct_TreeView = self.builder.get_object("Direct_TreeView")
        self.Direct_TreeView_List = Gtk.ListStore(bool, str)
        self.Direct_Button_1 = self.builder.get_object("Direct_Button_1")
        self.Direct_Button_2 = self.builder.get_object("Direct_Button_2")
        self.Direct_Button_3 = self.builder.get_object("Direct_Button_3")
        self.Direct_Button_4 = self.builder.get_object("Direct_Button_4")
        self.Direct_Button_5 = self.builder.get_object("Direct_Button_5")
        self.Direct_TreeView_Generator()

    def Direct_TreeView_Generator(self, *args):
        self.Direct_TreeView_Second()

        one_column = Gtk.TreeViewColumn(title="Активно", cell_renderer=Gtk.CellRendererToggle(), active=0)
        two_column = Gtk.TreeViewColumn(title="Устройство", cell_renderer=Gtk.CellRendererText(), text=1)

        self.Direct_TreeView.append_column(one_column)
        self.Direct_TreeView.append_column(two_column)

        self.Direct_TreeView.set_model(self.Direct_TreeView_List)


    # Продолжение заполнения
    def Direct_TreeView_Second(self):
        USB_List = subprocess.getoutput('VBoxManage list usbhost').split("\n")
        # Out_All_Name = subprocess.getoutput('v=$(VBoxManage list vms);awk -F\'\"|\\"\' \'{print $2}\' <<< $v').split("\n")
        # Out_All_Hash = subprocess.getoutput('v=$(VBoxManage list vms);awk -F\'\"|\\"\' \'{print $3}\' <<< $v').split("\n")
        # Out_ON_Hash = subprocess.getoutput('v=$(VBoxManage list runningvms);awk -F\'\"|\\"\' \'{print $3}\' <<< $v').split("\n")
        # self.Main_Array = [[0] * 3 for i in range(len(Out_All_Name))]
        # # self.arg = [0 for x in range(len(Out_All_Name))]
        # for i in range(len(Out_All_Name)):
        #     Out_Bool = False
        #     for v in range(len(Out_ON_Hash)):
        #         if Out_All_Hash[i] == Out_ON_Hash[v]:
        #             Out_Bool = True
        #     Out_IP = re.split('"|<', subprocess.getoutput(f'VBoxManage showvminfo "{Out_All_Name[i]}" | grep TCP/Address '))
        #     if Out_IP[0] == "" or Out_IP[1] == 'not set>':
        #         self.Virtual_TreeView_List.append([Out_All_Name[i], Out_Bool, "0.0.0.0"])
        #         self.Main_Array[i][0] = Out_All_Name[i]
        #         self.Main_Array[i][1] = Out_Bool
        #         self.Main_Array[i][2] = "0.0.0.0"
        #     else:
        #         self.Virtual_TreeView_List.append([Out_All_Name[i], Out_Bool, Out_IP[i]])
        #         self.Main_Array[i][0] = Out_All_Name[i]
        #         self.Main_Array[i][1] = Out_Bool
        #         self.Main_Array[i][2] = Out_IP[1]




# if __name__ == '__main__':
#     main = Note_Direct()
#     Gtk.main()
