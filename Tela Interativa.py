#COMEÇO DE UMA TELA INTERATIVA

import tkinter as tk

# Crie uma janela
janela = tk.Tk()

# Crie um rótulo
rotulo = tk.Label(janela, text="Olá, mundo!")

# Adicione o rótulo à janela
rotulo.pack()

# Inicie o loop principal da janela
janela.mainloop()