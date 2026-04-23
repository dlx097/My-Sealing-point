import tkinter as tk

janela = tk.Tk()
janela.title("desafio")
janela.geometry("500x500")

carrinho = []

e1 = tk.Entry(janela)
e1.pack(pady=20)
e2 = tk.Entry(janela)
e2.pack(pady=20)

t = tk.Label(janela, text="teste")
t.pack()

def adicionar():
    ee1 = e1.get()
    try:
        ee2 = float(e2.get())
    except:
        ee2 = None
    produto = {"nome": ee1, "valor": ee2}
    carrinho.append(produto)
    t.configure(text=produto)

def terminar():
    Nota_T = ""
    Total = 0
    global produto
    for p in carrinho:
        nome = p["nome"]
        valor = p["valor"]
        Nota_T += f"{nome}: {valor}\n"
        Total += valor
        Nota.configure(text=f"----------Nota Fiscal----------\n{Nota_T}\n----------Total----------\n{Total}")
        print(f"{nome}  {valor}")
    for i in range(len(carrinho)):
        Nota.configure(text=f"----------Nota Fiscal----------\n{Nota_T}\n----------Total----------\n{Total}")

b = tk.Button(janela, text="adicionar", command=adicionar)
b.pack(pady=20)

Nota = tk.Label(janela, text="")
Nota.pack()

Terminar = tk.Button(janela, text="Terminar compra", command=terminar)
Terminar.pack(pady=20)

janela.mainloop()