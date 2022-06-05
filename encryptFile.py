from tkinter import Tk, Entry, Button, Radiobutton, Label, IntVar, StringVar, Checkbutton
import tkinter
import tkinter.font as tkFont
import os
import base64
from tkinter.filedialog import askopenfilename, askdirectory



e = 0


def chooseFile():
    global path
    path = askopenfilename()
    
def chooseDir():
    global path
    path = askdirectory()







def encode():
    global var1
    
    if e == 1:
        chooseDir()
        dire = r'{}'.format(path)
        if var1.get() == 1:
            for (dirpath, dirnames, filenames) in os.walk(dire):
                dirpath = rf'{dirpath}'
                for file in os.listdir(dirpath):
                    os.chdir(dirpath)
                    try:
                        with open (file,'rb') as imagem:
                            ir = imagem.read()
                            imagem64 = base64.encodebytes(base64.encodebytes(ir))

                        os.remove(file)

                        with open (file, '+wb') as imagem:
                                ir = imagem.write(imagem64)
                    except:
                        pass
        elif var1.get() == 0:
            for file in os.listdir(dire):
                os.chdir(dire)
                try:
                    with open (file,'rb') as imagem:
                        ir = imagem.read()
                        imagem64 = base64.encodebytes(base64.encodebytes(ir))

                    os.remove(file)

                    with open (file, '+wb') as imagem:
                            ir = imagem.write(imagem64)
                except:
                    pass

    elif e == 0:
        chooseFile()
        dire = r'{}'.format(path)
        with open (dire,'rb') as imagem:
            ir = imagem.read()
            imagem64 = base64.encodebytes(base64.encodebytes(ir))

        os.remove(dire)

        with open (dire, '+wb') as imagem:
                ir = imagem.write(imagem64)
    janela.destroy()


def decode():
    global var1
    if e == 0:
        chooseFile()
        dire = r'{}'.format(path)
        with open (dire,'rb') as imagem:
            ir = imagem.read()
            imagem64 = base64.decodebytes(base64.decodebytes(ir))
        os.remove(dire)
        with open (dire, '+wb') as imagem:
            ir = imagem.write(imagem64)  
    elif e == 1:
        chooseDir()
        dire = r'{}'.format(path)
        if var1.get() == 1:
            for (dirpath, dirnames, filenames) in os.walk(dire):
                dirpath = rf'{dirpath}'
                for file in os.listdir(dirpath):
                    os.chdir(dirpath)
                    try:
                        with open (file,'rb') as imagem:
                            ir = imagem.read()
                            imagem64 = base64.decodebytes(base64.decodebytes(ir))
                        os.remove(file)
                        with open (file, '+wb') as imagem:
                            ir = imagem.write(imagem64)
                    except:
                        pass
        elif var1.get() == 0:
            for file in os.listdir(dire):
                os.chdir(dire)
                try:
                    with open (file,'rb') as imagem:
                        ir = imagem.read()
                        imagem64 = base64.decodebytes(base64.decodebytes(ir))
                    os.remove(file)
                    with open (file, '+wb') as imagem:
                        ir = imagem.write(imagem64)
                except:
                    pass


                    
    janela.destroy()

def p():
    global e
    e = 1

def f():
    global e
    e = 0
def d():
    global r
    r = 1


janela = Tk()
var = tkinter.IntVar()

r = 0
var1 = IntVar()
janela.configure(bg='Dark Grey')
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=15)

fi = Radiobutton(janela, text ='Ficheiro', variable = var, value = 0,font = fontStyle ,bg ='Dark Grey', command=f)
fi.place(x=390,y=70)

che = Checkbutton(janela, bg ='Dark Grey', variable = var1,text='Todas as Pastas',font = fontStyle1 ,command= d)
che.place(x=220,y=130)
pasta = Radiobutton(janela,text = 'Pasta', variable = var, value = 1,font = fontStyle, bg ='Dark Grey',command=p)
pasta.place(x=560,y=70)


te = Label(janela, text = 'Documento: ',font = fontStyle, bg ='Dark Grey')
te.place(x= 220,y=70)

codificar = Button(janela,width= 20, text='Codificar',font=fontStyle, bg = 'Grey',command=encode)
codificar.place(x=60,y=200)

descodificar = Button(janela,width= 20, text='Descodificar',font=fontStyle, bg = 'Grey',command=decode)
descodificar.place(x=500,y=200)




janela.title('Encriptador de Ficheiros')
janela.geometry('900x300')
janela.mainloop()


