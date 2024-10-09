# Created by Khairul Fahmi_2210010241_5P

import PySimpleGUI as sg

window = sg.Window(
                title="Profile", 
                layout=[
                        [sg.Text("NPM          : 2210010241")],
                        [sg.Text("Nama         : KHAIRUL FAHMI")],
                        [sg.Text("Kelas         : 5P Reguler Pagi Banjarmasin")],
                        [sg.Text("Mata Kuliah : Pemrograman Visual 3")]
                ],
                size=(400, 200)
)

window()
window.close()