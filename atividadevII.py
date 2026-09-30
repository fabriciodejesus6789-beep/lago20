import customtkinter as ctk
from tkinter import messagebox
import time


# =========================================================
# CLASSES DE MODELO
# =========================================================

class Usuario:

    def __init__(self, nome, nivel, notificacoes):
        self.nome = nome
        self.nivel = nivel
        self.notificacoes = notificacoes

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Nível: {self.nivel} | "
            f"Notificações: {self.notificacoes}"
        )


class Produto:

    def __init__(self, nome, categoria, quantidade, tipo, unidade):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.tipo = tipo
        self.unidade = unidade

    def __str__(self):
        return (
            f"Produto: {self.nome}\n"
            f"Categoria: {self.categoria}\n"
            f"Quantidade: {self.quantidade} {self.unidade}\n"
            f"Tipo: {self.tipo}\n"
            f"-------------------------\n"
        )


class Livro:

    def __init__(self, titulo, autor, ano, status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

    def __str__(self):
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Ano: {self.ano}\n"
            f"Status: {self.status}\n"
        )


# =========================================================
# APLICAÇÃO PRINCIPAL
# =========================================================

class Aplicativo(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Sistema de Gestão")
        self.geometry("1000x700")

        # Listas dos objetos
        self.lista_usuarios = []
        self.lista_produtos = []
        self.lista_livros = []

        # Configuração da janela
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # =================================================
        # BARRA LATERAL
        # =================================================

        self.barra_lateral = ctk.CTkFrame(
            master=self,
            width=200
        )

        self.barra_lateral.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.janela_abas = ctk.CTkTabview(
            master=self
        )

        self.janela_abas.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # =================================================
        # ABAS
        # =================================================

        self.janela_abas.add("Perfil")
        self.janela_abas.add("Preferencias")
        self.janela_abas.add("Notificacoes")
        self.janela_abas.add("Estoque")
        self.janela_abas.add("Livros")
        self.janela_abas.add("Configuracao")

        # Construção das telas
        self.construir_barra_lateral()
        self.construir_aba_perfil()
        self.construir_aba_preferencias()
        self.construir_aba_notificacoes()
        self.construir_aba_estoque()
        self.construir_aba_livros()
        self.construir_aba_configuracao()

    # =====================================================
    # BARRA LATERAL
    # =====================================================

    def construir_barra_lateral(self):

        self.label_titulo = ctk.CTkLabel(
            master=self.barra_lateral,
            text="Meu Sistema",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        self.label_titulo.pack(
            padx=20,
            pady=20
        )

        self.botao_preferencias = ctk.CTkButton(
            master=self.barra_lateral,
            text="Preferências",
            command=self.ir_para_preferencias
        )

        self.botao_preferencias.pack(
            padx=20,
            pady=20
        )

        self.switch_tema = ctk.CTkSwitch(
            master=self.barra_lateral,
            text="Modo Escuro",
            command=self.alternar_tema
        )

        self.switch_tema.select()

        ctk.set_appearance_mode("Dark")

        self.switch_tema.pack(
            padx=20,
            pady=10,
            side="bottom"
        )

    def ir_para_preferencias(self):

        self.janela_abas.set("Preferencias")

    def alternar_tema(self):

        if self.switch_tema.get() == 0:
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    # =====================================================
    # PERFIL
    # =====================================================

    def construir_aba_perfil(self):

        aba = self.janela_abas.tab("Perfil")

        self.campo_nome = ctk.CTkEntry(
            master=aba,
            placeholder_text="Digite seu nome completo",
            width=300
        )

        self.campo_nome.pack(
            padx=20,
            pady=10
        )

        self.label_nivel = ctk.CTkLabel(
            master=aba,
            text="Nível do Usuário:"
        )

        self.label_nivel.pack(
            padx=20,
            pady=5
        )

        self.nivel_usuario = ctk.IntVar(value=0)

        self.radio_basico = ctk.CTkRadioButton(
            master=aba,
            text="Básico",
            variable=self.nivel_usuario,
            value=0
        )

        self.radio_basico.pack(
            padx=20,
            pady=5
        )

        self.radio_admin = ctk.CTkRadioButton(
            master=aba,
            text="Admin",
            variable=self.nivel_usuario,
            value=1
        )

        self.radio_admin.pack(
            padx=20,
            pady=5
        )

        self.checkbox_notificacoes = ctk.CTkCheckBox(
            master=aba,
            text="Receber Notificações por e-mail"
        )

        self.checkbox_notificacoes.pack(
            padx=20,
            pady=5
        )

        self.botao_salvar = ctk.CTkButton(
            master=aba,
            text="Salvar Perfil",
            command=self.salvar_perfil
        )

        self.botao_salvar.pack(
            padx=20,
            pady=15
        )

    def salvar_perfil(self):

        nome = self.campo_nome.get()

        if self.nivel_usuario.get() == 0:
            nivel = "Básico"
        else:
            nivel = "Admin"

        if self.checkbox_notificacoes.get() == 0:
            notificacoes = "Não"
        else:
            notificacoes = "Sim"

        if not nome.split():

            messagebox.showerror(
                title="Erro!",
                message="Nome inválido!"
            )

        else:

            novo_usuario = Usuario(
                nome,
                nivel,
                notificacoes
            )

            self.lista_usuarios.append(
                novo_usuario
            )

            mensagem = (
                f"Nome: {nome}\n"
                f"Nível de acesso: {nivel}\n"
                f"Notificações: {notificacoes}"
            )

            messagebox.showinfo(
                title="Perfil Salvo!",
                message=mensagem
            )

    # =====================================================
    # QUESTÃO 1 - PREFERÊNCIAS
    # =====================================================

    def construir_aba_preferencias(self):

        aba = self.janela_abas.tab("Preferencias")

        self.label_idiomas = ctk.CTkLabel(
            master=aba,
            text="Selecione o idioma:"
        )

        self.label_idiomas.pack(
            padx=20,
            pady=10
        )

        self.menu_idiomas = ctk.CTkOptionMenu(
            master=aba,
            values=[
                "Português",
                "Inglês",
                "Espanhol"
            ]
        )

        self.menu_idiomas.pack(
            padx=20,
            pady=5
        )

        self.label_volume = ctk.CTkLabel(
            master=aba,
            text="Volume de dados"
        )

        self.label_volume.pack(
            padx=20,
            pady=5
        )

        # Slider da questão 1
        self.slider_volume = ctk.CTkSlider(
            master=aba,
            from_=0,
            to=100,
            command=self.volume_atualizado
        )

        self.slider_volume.set(100)

        self.slider_volume.pack(
            padx=20,
            pady=5
        )

        self.label_valor_volume = ctk.CTkLabel(
            master=aba,
            text="100%"
        )

        self.label_valor_volume.pack(
            padx=20,
            pady=5
        )

        self.label_progresso = ctk.CTkLabel(
            master=aba,
            text="Carregamento"
        )

        self.label_progresso.pack(
            padx=20,
            pady=5
        )

        self.barra_progresso = ctk.CTkProgressBar(
            master=aba,
            width=500
        )

        self.barra_progresso.set(0)

        self.barra_progresso.pack(
            padx=20,
            pady=5
        )

        self.botao_carregar = ctk.CTkButton(
            master=aba,
            text="Iniciar Carregamento",
            command=self.carregar_dados
        )

        self.botao_carregar.pack(
            padx=20,
            pady=10
        )

        self.label_lista = ctk.CTkLabel(
            master=aba,
            text="Usuários Cadastrados:"
        )

        self.label_lista.pack(
            padx=20,
            pady=5
        )

        self.area_texto_lista_usuarios = ctk.CTkTextbox(
            master=aba,
            width=600,
            height=200
        )

        self.area_texto_lista_usuarios.pack(
            padx=20,
            pady=5
        )

        self.area_texto_lista_usuarios.configure(
            state="disabled"
        )

    def volume_atualizado(self, novo_valor_volume):

        self.label_valor_volume.configure(
            text=f"{int(novo_valor_volume)}%"
        )

    def carregar_dados(self):

        porcentagem = self.slider_volume.get()

        quantidade = int(
            len(self.lista_usuarios)
            * porcentagem
            / 100
        )

        self.barra_progresso.set(0)

        self.area_texto_lista_usuarios.configure(
            state="normal"
        )

        self.area_texto_lista_usuarios.delete(
            "1.0",
            "end"
        )

        self.area_texto_lista_usuarios.configure(
            state="disabled"
        )

        if quantidade == 0:

            self.area_texto_lista_usuarios.configure(
                state="normal"
            )

            self.area_texto_lista_usuarios.insert(
                "end",
                "Nenhum usuário para carregar."
            )

            self.area_texto_lista_usuarios.configure(
                state="disabled"
            )

            return

        # Carrega um usuário por vez
        for i in range(quantidade):

            usuario = self.lista_usuarios[i]

            self.area_texto_lista_usuarios.configure(
                state="normal"
            )

            self.area_texto_lista_usuarios.insert(
                "end",
                str(usuario) + "\n"
            )

            self.area_texto_lista_usuarios.configure(
                state="disabled"
            )

            progresso = (i + 1) / quantidade

            self.barra_progresso.set(
                progresso
            )

            self.update()

            time.sleep(0.3)

    # =====================================================
    # QUESTÃO 2 - NOTIFICAÇÕES
    # =====================================================

    def construir_aba_notificacoes(self):

        aba = self.janela_abas.tab(
            "Notificacoes"
        )

        self.label_notificacao = ctk.CTkLabel(
            master=aba,
            text="Simulador de Envio de Notificações",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        self.label_notificacao.pack(
            padx=20,
            pady=20
        )

        self.label_velocidade = ctk.CTkLabel(
            master=aba,
            text="Velocidade de Envio"
        )

        self.label_velocidade.pack(
            padx=20,
            pady=5
        )

        self.slider_velocidade = ctk.CTkSlider(
            master=aba,
            from_=0.1,
            to=2
        )

        self.slider_velocidade.set(0.5)

        self.slider_velocidade.pack(
            padx=20,
            pady=10
        )

        self.barra_notificacoes = ctk.CTkProgressBar(
            master=aba,
            width=500
        )

        self.barra_notificacoes.set(0)

        self.barra_notificacoes.pack(
            padx=20,
            pady=10
        )

        self.area_notificacoes = ctk.CTkTextbox(
            master=aba,
            width=600,
            height=250
        )

        self.area_notificacoes.pack(
            padx=20,
            pady=10
        )

        self.botao_enviar = ctk.CTkButton(
            master=aba,
            text="Enviar",
            command=self.enviar_notificacoes
        )

        self.botao_enviar.pack(
            padx=20,
            pady=10
        )

    def enviar_notificacoes(self):

        usuarios = []

        for usuario in self.lista_usuarios:

            if usuario.notificacoes == "Sim":
                usuarios.append(usuario)

        self.area_notificacoes.delete(
            "1.0",
            "end"
        )

        self.barra_notificacoes.set(0)

        if not usuarios:

            self.area_notificacoes.insert(
                "end",
                "Nenhum usuário deseja receber notificações."
            )

            return

        total = len(usuarios)

        for i, usuario in enumerate(usuarios):

            self.area_notificacoes.insert(
                "end",
                f"Enviando para: {usuario.nome}\n"
            )

            progresso = (i + 1) / total

            self.barra_notificacoes.set(
                progresso
            )

            self.update()

            time.sleep(
                self.slider_velocidade.get()
            )

        self.area_notificacoes.insert(
            "end",
            "\nEnvio concluído!"
        )

    # =====================================================
    # QUESTÃO 3 - ESTOQUE
    # =====================================================

    def construir_aba_estoque(self):

        aba = self.janela_abas.tab(
            "Estoque"
        )

        titulo = ctk.CTkLabel(
            master=aba,
            text="Gestor de Estoque",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        titulo.pack(
            padx=20,
            pady=15
        )

        self.campo_produto = ctk.CTkEntry(
            master=aba,
            width=300,
            placeholder_text="Nome do produto"
        )

        self.campo_produto.pack(
            padx=20,
            pady=5
        )

        self.campo_categoria = ctk.CTkEntry(
            master=aba,
            width=300,
            placeholder_text="Categoria"
        )

        self.campo_categoria.pack(
            padx=20,
            pady=5
        )

        self.campo_quantidade = ctk.CTkEntry(
            master=aba,
            width=300,
            placeholder_text="Quantidade"
        )

        self.campo_quantidade.pack(
            padx=20,
            pady=5
        )

        self.tipo_produto = ctk.StringVar(
            value="Perecível"
        )

        self.radio_perecivel = ctk.CTkRadioButton(
            master=aba,
            text="Perecível",
            variable=self.tipo_produto,
            value="Perecível"
        )

        self.radio_perecivel.pack(
            pady=5
        )

        self.radio_nao_perecivel = ctk.CTkRadioButton(
            master=aba,
            text="Não Perecível",
            variable=self.tipo_produto,
            value="Não Perecível"
        )

        self.radio_nao_perecivel.pack(
            pady=5
        )

        self.menu_unidade = ctk.CTkOptionMenu(
            master=aba,
            values=[
                "Kg",
                "Unidade",
                "Litro"
            ]
        )

        self.menu_unidade.pack(
            padx=20,
            pady=10
        )

        self.botao_salvar_produto = ctk.CTkButton(
            master=aba,
            text="Salvar Produto",
            command=self.salvar_produto
        )

        self.botao_salvar_produto.pack(
            padx=20,
            pady=10
        )

        self.area_produtos = ctk.CTkTextbox(
            master=aba,
            width=600,
            height=180
        )

        self.area_produtos.pack(
            padx=20,
            pady=10
        )

    def salvar_produto(self):

        nome = self.campo_produto.get()
        categoria = self.campo_categoria.get()
        quantidade = self.campo_quantidade.get()

        # Validação da quantidade
        try:

            quantidade = float(quantidade)

        except ValueError:

            messagebox.showerror(
                "Erro",
                "A quantidade deve ser um número válido."
            )

            return

        if not nome or not categoria:

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos."
            )

            return

        # Criação do objeto
        produto = Produto(
            nome,
            categoria,
            quantidade,
            self.tipo_produto.get(),
            self.menu_unidade.get()
        )

        # Guarda na lista
        self.lista_produtos.append(
            produto
        )

        # Mostra o produto
        self.area_produtos.insert(
            "end",
            str(produto)
        )

        messagebox.showinfo(
            "Sucesso",
            "Produto instanciado e salvo!"
        )

        self.campo_produto.delete(
            0,
            "end"
        )

        self.campo_categoria.delete(
            0,
            "end"
        )

        self.campo_quantidade.delete(
            0,
            "end"
        )

    # =====================================================
    # QUESTÃO 4 - LIVROS
    # =====================================================

    def construir_aba_livros(self):

        aba = self.janela_abas.tab(
            "Livros"
        )

        titulo = ctk.CTkLabel(
            master=aba,
            text="Gerenciador de Livros",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        titulo.pack(
            padx=20,
            pady=10
        )

        # Cadastro

        self.campo_titulo_livro = ctk.CTkEntry(
            master=aba,
            width=300,
            placeholder_text="Título"
        )

        self.campo_titulo_livro.pack(
            pady=5
        )

        self.campo_autor_livro = ctk.CTkEntry(
            master=aba,
            width=300,
            placeholder_text="Autor"
        )

        self.campo_autor_livro.pack(
            pady=5
        )

        self.campo_ano_livro = ctk.CTkEntry(
            master=aba,
            width=300,
            placeholder_text="Ano"
        )

        self.campo_ano_livro.pack(
            pady=5
        )

        self.status_livro = ctk.StringVar(
            value="Disponível"
        )

        self.radio_disponivel = ctk.CTkRadioButton(
            master=aba,
            text="Disponível",
            variable=self.status_livro,
            value="Disponível"
        )

        self.radio_disponivel.pack(
            pady=3
        )

        self.radio_emprestado = ctk.CTkRadioButton(
            master=aba,
            text="Emprestado",
            variable=self.status_livro,
            value="Emprestado"
        )

        self.radio_emprestado.pack(
            pady=3
        )

        self.botao_cadastrar_livro = ctk.CTkButton(
            master=aba,
            text="Cadastrar Livro",
            command=self.cadastrar_livro
        )

        self.botao_cadastrar_livro.pack(
            pady=10
        )

        # Modo de visualização

        self.modo_visualizacao = ctk.StringVar(
            value="Lista Simples"
        )

        self.menu_visualizacao = ctk.CTkOptionMenu(
            master=aba,
            values=[
                "Lista Simples",
                "Detalhado"
            ],
            variable=self.modo_visualizacao
        )

        self.menu_visualizacao.pack(
            pady=5
        )

        # Barra de progresso

        self.barra_livros = ctk.CTkProgressBar(
            master=aba,
            width=500
        )

        self.barra_livros.set(0)

        self.barra_livros.pack(
            pady=5
        )

        # Área da biblioteca

        self.area_livros = ctk.CTkTextbox(
            master=aba,
            width=650,
            height=180
        )

        self.area_livros.pack(
            padx=20,
            pady=5
        )

        self.botao_carregar_livros = ctk.CTkButton(
            master=aba,
            text="Carregar Biblioteca",
            command=self.carregar_livros
        )

        self.botao_carregar_livros.pack(
            pady=5
        )

    def cadastrar_livro(self):

        titulo = self.campo_titulo_livro.get()
        autor = self.campo_autor_livro.get()
        ano = self.campo_ano_livro.get()

        try:

            ano = int(ano)

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite um ano válido."
            )

            return

        if not titulo or not autor:

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos."
            )

            return

        livro = Livro(
            titulo,
            autor,
            ano,
            self.status_livro.get()
        )

        self.lista_livros.append(
            livro
        )

        messagebox.showinfo(
            "Sucesso",
            "Livro cadastrado com sucesso!"
        )

        self.campo_titulo_livro.delete(
            0,
            "end"
        )

        self.campo_autor_livro.delete(
            0,
            "end"
        )

        self.campo_ano_livro.delete(
            0,
            "end"
        )

    def carregar_livros(self):

        self.area_livros.delete(
            "1.0",
            "end"
        )

        self.barra_livros.set(0)

        if not self.lista_livros:

            self.area_livros.insert(
                "end",
                "Nenhum livro cadastrado."
            )

            return

        total = len(self.lista_livros)

        for i, livro in enumerate(
            self.lista_livros
        ):

            if self.modo_visualizacao.get() == "Lista Simples":

                texto = (
                    f"{livro.titulo} - "
                    f"{livro.autor}\n"
                )

            else:

                texto = (
                    f"Título: {livro.titulo}\n"
                    f"Autor: {livro.autor}\n"
                    f"Ano: {livro.ano}\n"
                    f"Status: {livro.status}\n"
                    f"----------------------\n"
                )

            self.area_livros.insert(
                "end",
                texto
            )

            progresso = (i + 1) / total

            self.barra_livros.set(
                progresso
            )

            self.update()

            # Modo turbo
            if self.switch_turbo.get() == 0:

                time.sleep(0.3)

    # =====================================================
    # CONFIGURAÇÃO - MODO TURBO
    # =====================================================

    def construir_aba_configuracao(self):

        aba = self.janela_abas.tab(
            "Configuracao"
        )

        titulo = ctk.CTkLabel(
            master=aba,
            text="Configuração",
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        titulo.pack(
            padx=20,
            pady=20
        )

        self.switch_turbo = ctk.CTkSwitch(
            master=aba,
            text="Modo Turbo"
        )

        self.switch_turbo.pack(
            padx=20,
            pady=10
        )

        self.botao_otimizar = ctk.CTkButton(
            master=aba,
            text="Otimizar Banco de Dados",
            command=self.otimizar_banco
        )

        self.botao_otimizar.pack(
            padx=20,
            pady=20
        )

    def otimizar_banco(self):

        for i in range(100):

            progresso = (i + 1) / 100

            # Atualiza a barra dos livros
            self.barra_livros.set(
                progresso
            )

            self.update()

            # Se Turbo estiver desligado,
            # mostra a animação normalmente
            if self.switch_turbo.get() == 0:

                time.sleep(0.01)

        messagebox.showinfo(
            "Sucesso",
            "Banco de dados otimizado!"
        )


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

meu_sistema = Aplicativo()

meu_sistema.mainloop()