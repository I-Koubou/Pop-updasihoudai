import PySimpleGUI as sg
from tkinter import messagebox
import webbrowser

sg.theme('python')#テーマはここで変えます

cols = [
    [sg.Frame('タイプ1 (showinfo)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt1')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth1')],
     [sg.Submit(button_text='実行',key='st1'),]])],
      
     [sg.Frame('タイプ2 (showwarning)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt2')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth2')],
     [sg.Submit(button_text='実行',key='st2'),]])],

      [sg.Frame('タイプ3 (showerror)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt3')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth3')],
     [sg.Submit(button_text='実行',key='st3'),]])],

      [sg.Frame('タイプ4 (askquestion)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt4')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth4')],
     [sg.Submit(button_text='実行',key='st4'),]])],

      [sg.Frame('タイプ5 (askquestion)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt5')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth5')],
     [sg.Submit(button_text='実行',key='st5'),]])],

      [sg.Frame('タイプ6 (askyesnocancel)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt6')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth6')],
     [sg.Submit(button_text='実行',key='st6'),]])],

      [sg.Frame('タイプ7 (askretrycancel)', [
    [ sg.Text('タイトル'),sg.InputText(key='txtt7')],
    [ sg.Text('メッセージ'),sg.InputText(key='txth7')],
     [sg.Submit(button_text='実行',key='st7'),]])],

]


layout = [
    [sg.Text("タイトルとメッセージに記入して実行を押すとポップアップが出ます",font=('UD デジタル 教科書体 N-R',10)),sg.MenuBar([['メニュー',['これについて','これのgithub','バージョン情報','---','終了']]], key='menu')],
[sg.Column(cols, scrollable=True , vertical_scroll_only=True)],]

window = sg.Window('ポップアップ出し放題', layout,)
while True:  # Event Loop
    event, values = window.Read()

    if event == "st1":
       messagebox.showinfo(values["txtt1"],values["txth1"])

    if event == "st2":
       messagebox.showwarning(values["txtt2"],values["txth2"])

    if event == "st3":
       messagebox.showerror(values["txtt3"],values["txth3"])

    if event == "st4":
       messagebox.askquestion(values["txtt4"],values["txth4"])

    if event == "st5":
       messagebox.askokcancel(values["txtt5"],values["txth5"])

    if event == "st6":
       messagebox.askyesnocancel(values["txtt6"],values["txth6"])

    if event == "st7":
       messagebox.askretrycancel(values["txtt7"],values["txth7"])

    if event is None or event == 'Exit'or values['menu']=='終了':
        break

    if event == values['menu']=='これについて':
        webbrowser.open("https://istudio2628.wordpress.com/2022/01/24/pop-up/")

    if event == values['menu']=='これのgithub':
        webbrowser.open("https://github.com/I-Koubou/Pop-updasihoudai")

    if event == values['menu']=='バージョン情報':
        sg.popup('バージョン:1.0.1\n')
window.Close()
