class Emprestimo:
    def __init__(self, livro:Livro, usuario:Usuario, ativo:bool = True):
        if livro.disponivel:
            self.livro = livro
            self.livro.disponivel = False
        else:
            raise ValueError("Livro indisponível.")
        self.usuario = usuario
        self.ativo = ativo

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True