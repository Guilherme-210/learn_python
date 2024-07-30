import tkinter as tk

# 1 - criando a janela
window = tk.Tk()
window.geometry('600x300' )
window.title('Gerenciador de frases')

# 2 - adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o label
label = tk.Label(frame, text='Hello, word.')
label.pack(fill='x', expand=True)

# 4 - Adicionando o input
frase_lab = tk.Label(frame, text='Frase')
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - função para alterar o texto
def click():
  label.config(text=frase_inp.get())

# 6 - Adicionando botão
button = tk.Button(frame, text='Enviar', command=click)
button.pack()

window.mainloop()