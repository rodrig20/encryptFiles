from cryptography.fernet import Fernet
from tkinter import filedialog
import os



def codificar(data):
    global c
    txt = c.encrypt(data.encode()).decode()
    return txt

def decodificar(data):
    global c
    txt = c.decrypt(data.encode()).decode()
    return txt

folder = filedialog.askdirectory(title='Escolha uma pasta')
if os.path.exists(folder+'/fernetKey.txt'):
    existe = 1
    with open(folder+'/fernetKey.txt','r')as k:
        key = k.read()
        c = Fernet(key.encode())
else:
    existe = 0
    with open(folder+'/fernetKey.txt','wb+')as k:
        key = Fernet.generate_key()
        c = Fernet(key)
        k.write(key)

for (dirpath, dirnames, filenames) in os.walk(folder):
    for file in os.listdir(dirpath):
        path = dirpath+'/'+file
        os.chdir(dirpath)
        try:
            if not (folder == dirpath and 'fernetKey.txt' == file ):
                with open(file, 'r') as f:
                    original_txt = f.read()
                #adoicionar criptografia
                if not existe:
                    text_encrypted = codificar(original_txt)
                else: 
                    text_encrypted = decodificar(original_txt)
                with open(file, 'w') as f:
                    f.write(text_encrypted)
        except PermissionError:
            pass

if existe:
    os.remove(folder+'/fernetKey.txt')