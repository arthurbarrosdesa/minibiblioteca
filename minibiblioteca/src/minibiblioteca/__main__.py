from .livros import Livro
from .usuarios import Usuario
from .emprestimos import Emprestimo

user = Usuario("Henrique", "123")

book = Livro("Pax", "AsaLarsson", "ACD")

loan = Emprestimo(book, user)

print(f"Estado inicial-> Disp.Livro: {book.disponivel}; Emp.Ativo: {loan.ativo}")

loan.devolver()

print(f"Estado final-> Disp.Livro: {book.disponivel}; Emp.Ativo: {loan.ativo}")
