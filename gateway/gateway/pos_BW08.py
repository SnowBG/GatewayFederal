"""
Esse módulo recebe e decodifica posições do rastreador BW08.

Formato geral do pacote de dados:
 _________________________________
|Formato             | Tamanho    |
|Bit início          |  2         |
|Tamanho do pacote   |  1         |
|Número do protocolo |  1         |
|Dados de informação |  'N'       |
|Número serial       |  2         |
|Checagem de erro    |  2         |
|Bit final           |  2         |
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
Funções:

"""


class position_bw08:
    """Essa classe recebe e interpreta as posições do rastreador."""

    def __init__(self, position):
        """Método inicial para quebrar as informações do rastreador."""
        self.start = position[0:2]
        self.lenght = position[2:3]
        self.protocol = position[3:4]
