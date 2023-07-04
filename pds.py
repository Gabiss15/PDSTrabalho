
class Endereco:
    def __init__(self, rua, bairro, cidade, numero, estado, complemento):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero = numero
        self.estado = estado
        self.complemento = complemento
    def getEndereco(self):
        return "Seu endereco se encontra na " + self.rua + "," + self.bairro + "," + self.cidade + "," + self.numero + "," + self.estado + "," + self.complemento + "."

class Pedido:
    def __init__(self, nomeCliente, valor, formaPagamento, idCompra, dia):
        self.nomeCliente = nomeCliente
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.idCompra = idCompra
        self.dia = dia
        
        self.endereco = []

    def cadEndereco(self, endereco)
        self.endereco.append(endereco)
        
    def getIDpedido(self):
        return "ID do Pedido" + int(self.idCompra) + "Valor:" + int(self.valor)
        
class Produto:
    def __init__(self, nomeProduto, valorProduto, quantidade, codigo):
        self.nomeProduto = nomeProduto
        self.valorProduto = valorProduto
        self.quantidade = quantidade
        self.codigo = codigo
        
        self.pedidos = []
        
    def confirmarPedido(self, pedidos):
        conf_pedido = pedidos.getIDpedido()
        resposta = input("Deseja confirmar pedido? (Digitar S para Sim e N para Não")
        if(resposta == 'S'):
        self.pedidos.append(pedidos)
        return "Pedido confirmado com sucesso"
        else:
        return "Pedido não confimado"

        