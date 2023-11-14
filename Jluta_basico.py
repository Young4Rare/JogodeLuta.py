import tkinter as tk
from tkinter import messagebox
import random

class JogoBatalha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Batalha com Tkinter")

        self.vida_jogador = 10
        self.vida_computador = 10

        self.personagens = {
            "Guerreiro": {"ataque": "Cabeçada", "poder_combate": 4, "dano": 3},
            "Lobisomem": {"ataque": "Soco", "poder_combate": 0, "dano": 0},
            "Mago": {"ataque": "Soco", "poder_combate": 0, "dano": 0},
            "Elfo": {"ataque": "Soco", "poder_combate": 0, "dano": 0},
            "Viking": {"ataque": "Soco", "poder_combate": 0, "dano": 0},
            "Arcano": {"ataque": "Soco", "poder_combate": 0, "dano": 0}
        }

        self.personagem_jogador = None

        self.criar_interface()

    def criar_interface(self):
        self.label_vida_jogador = tk.Label(self.master, text="Vida do Jogador: {}".format(self.vida_jogador))
        self.label_vida_jogador.pack()

        self.label_vida_computador = tk.Label(self.master, text="Vida do Computador: {}".format(self.vida_computador))
        self.label_vida_computador.pack()

        # Adiciona botões para escolher personagem
        for personagem in self.personagens.keys():
            botao_personagem = tk.Button(self.master, text=personagem, command=lambda p=personagem: self.escolher_personagem(p))
            botao_personagem.pack()

        self.botao_realizar_ataque = tk.Button(self.master, text="Realizar Ataque", command=self.realizar_ataque, state=tk.DISABLED)
        self.botao_realizar_ataque.pack()

    def escolher_personagem(self, escolha):
        self.personagem_jogador = self.personagens[escolha]
        messagebox.showinfo("Personagem Escolhido", "Você escolheu o personagem: {}".format(escolha))
        self.botao_realizar_ataque.config(state=tk.NORMAL)

    def realizar_ataque(self):
        if self.personagem_jogador["ataque"] == "Cabeçada":
            poder_combate_jogador, dano_jogador = 4, 3
        elif self.personagem_jogador["ataque"] == "Soco":
            poder_combate_jogador, dano_jogador = random.randint(1, 6), random.randint(1, 6)

        self.vida_computador -= dano_jogador
        self.atualizar_interface()

        if self.vida_computador <= 0:
            messagebox.showinfo("Fim de Jogo", "Você venceu! Parabéns!")
            self.master.destroy()

        # Computador realiza o ataque
        poder_combate_computador, dano_computador = random.randint(1, 6), random.randint(1, 6)
        self.vida_jogador -= dano_computador
        self.atualizar_interface()

        if self.vida_jogador <= 0:
            messagebox.showinfo("Fim de Jogo", "Você perdeu! Melhor sorte na próxima vez.")
            self.master.destroy()

    def atualizar_interface(self):
        self.label_vida_jogador.config(text="Vida do Jogador: {}".format(self.vida_jogador))
        self.label_vida_computador.config(text="Vida do Computador: {}".format(self.vida_computador))


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoBatalha(root)
    root.mainloop()
