import subprocess

import gi
import os
import re
import Main_Thread
from Note_Direct import Note_Direct

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

object = None
class SignalHandler:
    @staticmethod
    def onDestroy(self, *args):
        Gtk.main_quit()
memes = 0

class Main:
    def __init__(self):
        #try:
            # self.set_size_request(200, 150)

            self.builder = Gtk.Builder()
            self.builder.add_from_file("New.glade")
            self.Main_Window = self.builder.get_object("Main_Window")
            self.builder.connect_signals(self)
            self.NoteBook = self.builder.get_object("NoteBook")
            self.Virtual_On_Button = self.builder.get_object("Virtual_On_Button")
            self.Virtual_Off_Button = self.builder.get_object("Virtual_Off_Button")
            self.Virtual_Save_Button = self.builder.get_object("Virtual_Save_Button")
            self.Virtual_Reset_Button = self.builder.get_object("Virtual_Reset_Button")
            self.Virtual_Create_Button = self.builder.get_object("Virtual_Create_Button")
            self.Virtual_Combo = self.builder.get_object("Virtual_Combo")

            self.Virtual_TreeView = self.builder.get_object("Virtual_TreeView")
            self.Virtual_TreeView_List = Gtk.ListStore(str, bool, str)

            Note_D = Note_Direct(self.builder)
            object = self
            self.Combo_Changed = None
            self.Block = 0
            self.C1 = "Test"
            self.Virtual_TreeView_Generator()
            self.Spring_Obj = Main_Thread.Main_Thread_Class(Main_Array=self.Main_Array, ctx=self)
            self.Spring_Obj.Start_Thread()
            self.Main_Window.show_all()
          #  self.Spring_Obj.after_event();
        #except Exception:
            #print("Exception Main - ", Exception)

    def getchange(self):
        self.C1 = "sds"
        print(self.C1)

    def getcontext(self):
        return self

    # Заполнение TreeView данными
    def Virtual_TreeView_Generator(self, *args):
        try:
            self.Virtual_TreeView_Second()

            vm_column = Gtk.TreeViewColumn(title="Виртуальная машина", cell_renderer=Gtk.CellRendererText(), text=0)
            st_column = Gtk.TreeViewColumn(title="Статус", cell_renderer=Gtk.CellRendererToggle(), active=1)
            ip_column = Gtk.TreeViewColumn(title="IP-адрес", cell_renderer=Gtk.CellRendererText(), text=2)

            self.Virtual_TreeView.append_column(vm_column)
            self.Virtual_TreeView.append_column(st_column)
            self.Virtual_TreeView.append_column(ip_column)

            self.Virtual_TreeView.set_model(self.Virtual_TreeView_List)
        except Exception:
            print("Exception Virtual_TreeView_Generator - ", Exception)

    def after_event(event):
        print("!вв!")
    # Продолжение заполнения
    def Virtual_TreeView_Second(self):
        #try:
            Out_All_Name = subprocess.getoutput(
                'v=$(VBoxManage list vms);awk -F\'\"|\\"\' \'{print $2}\' <<< $v').split("\n")
            Out_All_Hash = subprocess.getoutput(
                'v=$(VBoxManage list vms);awk -F\'\"|\\"\' \'{print $3}\' <<< $v').split("\n")
            Out_ON_Hash = subprocess.getoutput(
                'v=$(VBoxManage list runningvms);awk -F\'\"|\\"\' \'{print $3}\' <<< $v').split("\n")
            self.Main_Array = [[0] * 3 for i in range(len(Out_All_Name))]
            # self.arg = [0 for x in range(len(Out_All_Name))]
            for i in range(len(Out_All_Name)):
                Out_Bool = False
                for v in range(len(Out_ON_Hash)):
                    if Out_All_Hash[i] == Out_ON_Hash[v]:
                        Out_Bool = True
                Out_IP = re.split('"|<', subprocess.getoutput(
                    f'VBoxManage showvminfo "{Out_All_Name[i]}" | grep TCP/Address '))
                if Out_IP[0] == "" or Out_IP[1] == 'not set>':
                    self.Virtual_TreeView_List.append([Out_All_Name[i], Out_Bool, "0.0.0.0"])
                    self.Main_Array[i][0] = Out_All_Name[i]
                    self.Main_Array[i][1] = Out_Bool
                    self.Main_Array[i][2] = "0.0.0.0"
                else:
                    self.Virtual_TreeView_List.append([Out_All_Name[i], Out_Bool, Out_IP[i]])
                    self.Main_Array[i][0] = Out_All_Name[i]
                    self.Main_Array[i][1] = Out_Bool
                    self.Main_Array[i][2] = Out_IP[1]
        #except Exception:
            #print("Exception Virtual_TreeView_Second - ", Exception)

    # def CRINGE(self, select):
    #     self.C = select
    #     print("", self.C)

    # Выбор элемента TreeView
    def Virtual_TreeView_Changed(self, Selection):
        #try:

            if self.Block == 0:
                self.Virtual_On_Button.set_sensitive(True)
                Model, Treeiter = Selection.get_selected()
                if Treeiter is not None:
                    print("Выбрана ВМ:", Model[Treeiter][0])
                    self.Spring_Obj.Constructor(Model[Treeiter], Model, Selection)
                    self.Change_Name = Model[Treeiter][0]
                    self.Column_ID = self.Virtual_TreeView.get_selection().get_selected_rows()[1][0][0]
                    if Model[Treeiter][1] == True:
                        Main.Virtual_Change_Button(self, 0)
                    if Model[Treeiter][1] == False:
                        Main.Virtual_Change_Button(self, 1)
                    self.Spring_Obj.Checker()
                    self.Spring_Obj.Mutex = 1
                    if self.Spring_Obj.Checker_Changer == 1:
                        if Model[Treeiter][2] == self.Spring_Obj.arg1_3:
                            if self.Change_Name == self.Spring_Obj.arg1_1:
                                self.Block = 1
                                self.Spring_Obj.Checker_Changer = 0
                                Model.remove(Treeiter)
                                self.Virtual_TreeView_List.insert(self.Column_ID, (
                                    str(self.Spring_Obj.arg1_1), bool(self.Spring_Obj.arg1_2),
                                    str(self.Spring_Obj.arg1_3)))
                                self.Block = 0
                            else:
                                print("Ну типа заработало")
                    self.Spring_Obj.Mutex = 0
        # except Exception:
        #     print("Exception Virtual_TreeView_Changed - ", Exception)

    # Нажатие на кнопку Включить
    def Virtual_On_Button_Clicked(self, button):
        try:
            os.system("VBoxManage startvm %a -type headless " % self.Change_Name)
            Main.Virtual_Change_Button(self, 0)
        except Exception:
            print("Exception Virtual_On_Button_Clicked - ", Exception)

    # Нажатие на кнопку Выключить
    def Virtual_Off_Button_Clicked(self, button):
        try:
            os.system("VBoxManage controlvm %a acpipowerbutton" % self.Change_Name)
            Main.Virtual_Change_Button(self, 1)
            print("Выключение", self.Change_Name)
        except Exception:
            print("Exception Virtual_Off_Button_Clicked - ", Exception)

    # Нажатие на кнопку Сохранить Состояние
    def Virtual_Save_Button_Clicked(self, button):
        try:
            os.system("VBoxManage controlvm %a savestate" % self.Change_Name)
            print(os)
        except Exception:
            print("Exception Virtual_Save_Button_Clicked - ", Exception)

    # Нажатие на кнопку Перезагрузить
    def Virtual_Reset_Button_Clicked(self, button):
        try:
            os.system("VBoxManage controlvm %a reset" % self.Change_Name)
            print(os)
        except Exception:
            print("Exception Virtual_Reset_Button_Clicked - ", Exception)
    #
    def Virtual_Combo_Changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            #row_id, name = model[tree_iter][:2]
            row_id = model[tree_iter][0]
            self.Combo_Changed = row_id
            #print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())
    def Virtual_Create_Button_Clicked(self, button):
        if self.Combo_Changed == "Прямое подключение":
            self.NoteBook_Click_1()
        if self.Combo_Changed == "PDR-подключение":
            self.NoteBook_Click_2()
        if self.Combo_Changed == "RemoteApp-подключение":
            self.NoteBook_Click_3()

    def NoteBook_Click_1(self):
        print("1")
        #self.NoteBook.set_surrent_page(1)
    def NoteBook_Click_2(self):
        print("2")
    def NoteBook_Click_3(self):
        print("3")
    # Изменение доступности к кнопкам в зависимости от состояния машины
    def Virtual_Change_Button(self, on):
        try:
            if on == 0:
                self.Virtual_Off_Button.set_sensitive(True)
                self.Virtual_Save_Button.set_sensitive(True)
                self.Virtual_Reset_Button.set_sensitive(True)
                self.Virtual_Create_Button.set_sensitive(True)
                self.Virtual_Combo.set_sensitive(True)
                self.Virtual_On_Button.set_sensitive(False)
            else:
                self.Virtual_Off_Button.set_sensitive(False)
                self.Virtual_Save_Button.set_sensitive(False)
                self.Virtual_Reset_Button.set_sensitive(False)
                self.Virtual_Create_Button.set_sensitive(False)
                self.Virtual_Combo.set_sensitive(False)
                self.Virtual_On_Button.set_sensitive(True)
        except Exception:
            print("Exception Virtual_Change_Button - ", Exception)

    # Закрытие приложения и потока
    def Main_Close(self, e):
        try:
            self.Spring_Obj.Stop_Thread()
        except Exception:
            print("Exception Main_Close - ", Exception)


if __name__ == '__main__':
    main = Main()
    Gtk.main()

