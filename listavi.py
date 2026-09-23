"""
QUESTAO 1

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry("500x450")


def calcular():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        if peso <= 0 or altura <= 0:
            messagebox.showwarning("Aviso", "Digite valores maiores que zero.")
            return

        imc = peso / (altura * altura)

        if imc < 18.5:
            situacao = "Abaixo do peso"
        elif imc < 25:
            situacao = "Peso normal"
        elif imc < 30:
            situacao = "Sobrepeso"
        else:
            situacao = "Obesidade"

        resultado.configure(
            text=f"IMC: {imc:.2f}\nSituação: {situacao}"
        )

        if receber_dicas.get():
            messagebox.showinfo(
                "Dicas",
                "Procure manter uma alimentação equilibrada e praticar atividades físicas."
            )

    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos.")


titulo = ctk.CTkLabel(janela, text="Calculadora de IMC",
                      font=("Arial", 24))
titulo.pack(pady=20)

entrada_peso = ctk.CTkEntry(janela, placeholder_text="Peso em kg")
entrada_peso.pack(pady=10)

entrada_altura = ctk.CTkEntry(janela, placeholder_text="Altura em metros")
entrada_altura.pack(pady=10)

genero = ctk.StringVar(value="Masculino")

radio_m = ctk.CTkRadioButton(
    janela, text="Masculino", variable=genero, value="Masculino"
)
radio_m.pack(pady=5)

radio_f = ctk.CTkRadioButton(
    janela, text="Feminino", variable=genero, value="Feminino"
)
radio_f.pack(pady=5)

receber_dicas = ctk.BooleanVar()

check = ctk.CTkCheckBox(
    janela,
    text="Quero receber dicas por e-mail",
    variable=receber_dicas
)
check.pack(pady=10)

botao = ctk.CTkButton(
    janela,
    text="Calcular",
    command=calcular
)
botao.pack(pady=10)

painel = ctk.CTkFrame(janela)
painel.pack(pady=15, padx=20, fill="x")

resultado = ctk.CTkLabel(
    painel,
    text="Resultado aparecerá aqui",
    font=("Arial", 18)
)
resultado.pack(pady=20)

janela.mainloop()

"""
QUESTAO 2

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Lista de Tarefas")
janela.geometry("600x500")

tarefas = []


def adicionar():
    tarefa = entrada_tarefa.get()

    if tarefa == "":
        messagebox.showwarning("Aviso", "Digite uma tarefa.")
        return

    tarefas.append(tarefa)

    check = ctk.CTkCheckBox(
        aba_pendentes,
        text=tarefa
    )
    check.pack(anchor="w", padx=20, pady=5)

    entrada_tarefa.delete(0, "end")


def remover():
    messagebox.showinfo(
        "Remover",
        "Para este exemplo, as tarefas podem ser desmarcadas manualmente."
    )


def mudar_tema():
    if modo_escuro.get():
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


abas = ctk.CTkTabview(janela)
abas.pack(expand=True, fill="both", padx=20, pady=20)

aba_pendentes = abas.add("Tarefas Pendentes")
aba_concluidas = abas.add("Concluídas")
aba_config = abas.add("Configurações")

entrada_tarefa = ctk.CTkEntry(
    aba_pendentes,
    placeholder_text="Digite uma nova tarefa"
)
entrada_tarefa.pack(pady=20, padx=20, fill="x")

botao_adicionar = ctk.CTkButton(
    aba_pendentes,
    text="Adicionar",
    command=adicionar
)
botao_adicionar.pack(pady=10)

botao_remover = ctk.CTkButton(
    aba_pendentes,
    text="Remover",
    command=remover
)
botao_remover.pack(pady=10)

label_config = ctk.CTkLabel(
    aba_config,
    text="Configurações",
    font=("Arial", 20)
)
label_config.pack(pady=20)

modo_escuro = ctk.BooleanVar()

switch = ctk.CTkSwitch(
    aba_config,
    text="Modo escuro",
    variable=modo_escuro,
    command=mudar_tema
)
switch.pack(pady=20)

janela.mainloop()

"""
QUSTAO 3

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Inscrição em Curso")
janela.geometry("500x550")


def inscrever():
    nome = entrada_nome.get()
    email = entrada_email.get()
    cpf = entrada_cpf.get()
    turno = horario.get()

    if nome == "" or email == "" or cpf == "":
        messagebox.showwarning(
            "Aviso",
            "Preencha todos os campos."
        )
        return

    if not termos.get():
        messagebox.showwarning(
            "Aviso",
            "Você precisa aceitar os termos."
        )
        return

    messagebox.showinfo(
        "Inscrição",
        f"Inscrição realizada!\n\n"
        f"Nome: {nome}\n"
        f"E-mail: {email}\n"
        f"CPF: {cpf}\n"
        f"Turno: {turno}"
    )


titulo = ctk.CTkLabel(
    janela,
    text="Formulário de Inscrição",
    font=("Arial", 24)
)
titulo.pack(pady=20)

entrada_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Nome completo"
)
entrada_nome.pack(pady=10)

entrada_email = ctk.CTkEntry(
    janela,
    placeholder_text="E-mail"
)
entrada_email.pack(pady=10)

entrada_cpf = ctk.CTkEntry(
    janela,
    placeholder_text="CPF"
)
entrada_cpf.pack(pady=10)

horario = ctk.StringVar(value="Manhã")

ctk.CTkRadioButton(
    janela,
    text="Manhã",
    variable=horario,
    value="Manhã"
).pack(pady=5)

ctk.CTkRadioButton(
    janela,
    text="Tarde",
    variable=horario,
    value="Tarde"
).pack(pady=5)

ctk.CTkRadioButton(
    janela,
    text="Noite",
    variable=horario,
    value="Noite"
).pack(pady=5)

termos = ctk.BooleanVar()

ctk.CTkCheckBox(
    janela,
    text="Aceito os termos",
    variable=termos
).pack(pady=15)

ctk.CTkButton(
    janela,
    text="Inscrever",
    command=inscrever
).pack(pady=10)

janela.mainloop()


"""

"""
QEUSTAO 4

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Gerenciador Financeiro")
janela.geometry("500x550")

saldo = 0


def adicionar():
    global saldo

    descricao = entrada_descricao.get()

    try:
        valor = float(entrada_valor.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")
        return

    if descricao == "":
        messagebox.showwarning("Aviso", "Digite uma descrição.")
        return

    if tipo.get() == "Entrada":
        saldo += valor
    else:
        saldo -= valor

    texto_saldo.configure(
        text=f"Saldo: R$ {saldo:.2f}"
    )

    recorrente = "Sim" if despesa_recorrente.get() else "Não"

    messagebox.showinfo(
        "Lançamento",
        f"Descrição: {descricao}\n"
        f"Valor: R$ {valor:.2f}\n"
        f"Tipo: {tipo.get()}\n"
        f"Recorrente: {recorrente}"
    )

    entrada_descricao.delete(0, "end")
    entrada_valor.delete(0, "end")


painel = ctk.CTkFrame(janela)
painel.pack(pady=20, padx=20, fill="x")

texto_saldo = ctk.CTkLabel(
    painel,
    text="Saldo: R$ 0.00",
    font=("Arial", 22)
)
texto_saldo.pack(pady=20)

entrada_descricao = ctk.CTkEntry(
    janela,
    placeholder_text="Descrição"
)
entrada_descricao.pack(pady=10)

entrada_valor = ctk.CTkEntry(
    janela,
    placeholder_text="Valor"
)
entrada_valor.pack(pady=10)

tipo = ctk.StringVar(value="Entrada")

ctk.CTkRadioButton(
    janela,
    text="Entrada / Receita",
    variable=tipo,
    value="Entrada"
).pack(pady=5)

ctk.CTkRadioButton(
    janela,
    text="Saída / Despesa",
    variable=tipo,
    value="Saída"
).pack(pady=5)

despesa_recorrente = ctk.BooleanVar()

ctk.CTkCheckBox(
    janela,
    text="Despesa recorrente",
    variable=despesa_recorrente
).pack(pady=15)

ctk.CTkButton(
    janela,
    text="Adicionar lançamento",
    command=adicionar
).pack(pady=10)

janela.mainloop()

"""

"""
QUESTAO 5

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Pedido da Lanchonete")
janela.geometry("600x550")


def finalizar():
    tamanho = tamanho_produto.get()

    adicionais = []

    if queijo.get():
        adicionais.append("Queijo")

    if bacon.get():
        adicionais.append("Bacon")

    if refrigerante.get():
        adicionais.append("Refrigerante")

    endereco = entrada_endereco.get()
    telefone = entrada_telefone.get()

    if endereco == "" or telefone == "":
        messagebox.showwarning(
            "Aviso",
            "Preencha o endereço e telefone."
        )
        return

    if len(adicionais) == 0:
        adicionais_texto = "Nenhum"
    else:
        adicionais_texto = ", ".join(adicionais)

    messagebox.showinfo(
        "Pedido",
        f"Pedido realizado!\n\n"
        f"Tamanho: {tamanho}\n"
        f"Adicionais: {adicionais_texto}\n"
        f"Endereço: {endereco}\n"
        f"Telefone: {telefone}"
    )


abas = ctk.CTkTabview(janela)
abas.pack(expand=True, fill="both", padx=20, pady=20)

aba_pedido = abas.add("Monte seu Pedido")
aba_endereco = abas.add("Endereço de Entrega")

ctk.CTkLabel(
    aba_pedido,
    text="Escolha o tamanho:",
    font=("Arial", 18)
).pack(pady=15)

tamanho_produto = ctk.StringVar(value="M")

ctk.CTkRadioButton(
    aba_pedido,
    text="Pequeno",
    variable=tamanho_produto,
    value="P"
).pack(pady=5)

ctk.CTkRadioButton(
    aba_pedido,
    text="Médio",
    variable=tamanho_produto,
    value="M"
).pack(pady=5)

ctk.CTkRadioButton(
    aba_pedido,
    text="Grande",
    variable=tamanho_produto,
    value="G"
).pack(pady=5)

queijo = ctk.BooleanVar()

ctk.CTkCheckBox(
    aba_pedido,
    text="Queijo adicional",
    variable=queijo
).pack(pady=5)

bacon = ctk.BooleanVar()

ctk.CTkCheckBox(
    aba_pedido,
    text="Bacon",
    variable=bacon
).pack(pady=5)

refrigerante = ctk.BooleanVar()

ctk.CTkCheckBox(
    aba_pedido,
    text="Refrigerante",
    variable=refrigerante
).pack(pady=5)

entrada_endereco = ctk.CTkEntry(
    aba_endereco,
    placeholder_text="Endereço"
)
entrada_endereco.pack(pady=20, padx=20, fill="x")

entrada_telefone = ctk.CTkEntry(
    aba_endereco,
    placeholder_text="Telefone"
)
entrada_telefone.pack(pady=20, padx=20, fill="x")

ctk.CTkButton(
    janela,
    text="Finalizar Pedido",
    command=finalizar
).pack(pady=10)

janela.mainloop()

"""


"""

QUSTÃO 6
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Configurações do Sistema")
janela.geometry("650x450")


def salvar():
    idioma_escolhido = idioma.get()

    notificacao = "Ativadas" if notificacoes.get() else "Desativadas"
    aceleracao = "Ativada" if hardware.get() else "Desativada"
    escuro = "Ativado" if modo_escuro.get() else "Desativado"

    if modo_escuro.get():
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

    messagebox.showinfo(
        "Configurações",
        f"Alterações salvas!\n\n"
        f"Notificações: {notificacao}\n"
        f"Aceleração: {aceleracao}\n"
        f"Modo escuro: {escuro}\n"
        f"Idioma: {idioma_escolhido}"
    )


menu = ctk.CTkFrame(janela, width=200)
menu.pack(side="left", fill="y", padx=10, pady=10)

ctk.CTkLabel(
    menu,
    text="CONFIGURAÇÕES",
    font=("Arial", 18)
).pack(pady=20)

notificacoes = ctk.BooleanVar(value=True)

ctk.CTkSwitch(
    menu,
    text="Notificações",
    variable=notificacoes
).pack(pady=15)

hardware = ctk.BooleanVar()

ctk.CTkSwitch(
    menu,
    text="Aceleração de hardware",
    variable=hardware
).pack(pady=15)

modo_escuro = ctk.BooleanVar()

ctk.CTkSwitch(
    menu,
    text="Modo escuro",
    variable=modo_escuro
).pack(pady=15)

area = ctk.CTkFrame(janela)
area.pack(side="right", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(
    area,
    text="Idioma do sistema",
    font=("Arial", 20)
).pack(pady=20)

idioma = ctk.StringVar(value="Português")

ctk.CTkRadioButton(
    area,
    text="Português",
    variable=idioma,
    value="Português"
).pack(pady=5)

ctk.CTkRadioButton(
    area,
    text="Inglês",
    variable=idioma,
    value="Inglês"
).pack(pady=5)

ctk.CTkRadioButton(
    area,
    text="Espanhol",
    variable=idioma,
    value="Espanhol"
).pack(pady=5)

ctk.CTkButton(
    area,
    text="Salvar alterações",
    command=salvar
).pack(pady=30)

janela.mainloop()

"""

"""
QUESTÃO 7

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Avaliação de Atendimento")
janela.geometry("500x550")


def enviar():
    nome = entrada_nome.get()
    comentario = entrada_comentario.get()
    nota_escolhida = nota.get()

    if nome == "":
        messagebox.showwarning(
            "Aviso",
            "Digite seu nome."
        )
        return

    if comentario == "":
        messagebox.showwarning(
            "Aviso",
            "Digite um comentário."
        )
        return

    publicacao = "Sim" if publicar.get() else "Não"

    messagebox.showinfo(
        "Obrigado!",
        f"Obrigado pela avaliação, {nome}!\n\n"
        f"Nota: {nota_escolhida}\n"
        f"Comentário: {comentario}\n"
        f"Autoriza publicação: {publicacao}"
    )


titulo = ctk.CTkLabel(
    janela,
    text="Avaliação de Atendimento",
    font=("Arial", 24)
)
titulo.pack(pady=20)

entrada_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Seu nome"
)
entrada_nome.pack(pady=10, padx=20, fill="x")

entrada_comentario = ctk.CTkEntry(
    janela,
    placeholder_text="Comentário"
)
entrada_comentario.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(
    janela,
    text="Nota do atendimento:"
).pack(pady=10)

nota = ctk.StringVar(value="5")

for numero in range(1, 6):
    ctk.CTkRadioButton(
        janela,
        text=str(numero),
        variable=nota,
        value=str(numero)
    ).pack(pady=3)

publicar = ctk.BooleanVar()

ctk.CTkCheckBox(
    janela,
    text="Autorizo a publicação do depoimento",
    variable=publicar
).pack(pady=15)

ctk.CTkButton(
    janela,
    text="Enviar avaliação",
    command=enviar
).pack(pady=15)

janela.mainloop()

"""

