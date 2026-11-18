class Usuario:
    def __init__(self, nome:str, id_usuario:str):
        self.nome = nome 
        self.id_usuario = id_usuario
    
    def __eq__(self, outro):
        if isinstance(outro, Usuario):
            return self.id_usuario == outro.id_usuario