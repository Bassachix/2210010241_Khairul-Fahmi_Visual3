# Created by Khairul Fahmi_2210010241_5P

import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")

window = sg.Window(
                title="Profile",
                layout=[
                    [sg.Text("NPM     : 2210010241")],
                    [sg.Text("Nama     : KHAIRUL FAHMI")],
                    [sg.Text("Kelas     : 5P Reguler Banjarmasin")]
                ],
                size=(400,200),
                font=("Times", 18)
)

window()
window.close()