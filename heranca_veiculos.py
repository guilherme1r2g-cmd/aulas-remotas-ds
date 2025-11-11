class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"Veículo: {self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def info(self):
        return f"Carro: {self.marca} {self.modelo} | Portas: {self.numero_portas}"