class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        #Atributos:
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe (cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    wesley = Pessoa(nome='Wesley')
    luciano = Pessoa(wesley, nome ='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)    
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = "Ramalho"
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(wesley.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(wesley.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(wesley.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())