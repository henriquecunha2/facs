class Usuario:

    _nome: str
    _email: str
    _codigo_aut: int

    def __init__(self, nome: str, email = "", cod = 0):
        self._nome = nome
        self._email = email
        self._codigo_aut = cod

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @nome.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def codigo_aut(self):
        return self._codigo_aut

    @nome.setter
    def codigo_aut(self, novo_codigo_aut):
        self._codigo_aut = novo_codigo_aut
