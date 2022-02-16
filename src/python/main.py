import abc


class IExplorer(abc.ABC):
    @abc.abstractmethod
    def OpenFile(self, n, t):
        pass

class Explorer(IExplorer):
    def OpenFile(self, n, t):
        if (t=="PDF"):
            PDF(n).AbrirArchivo()
            return
        TXT(n).AbrirArchivo()

class ProxyExplorer(IExplorer):
    def __init__(self, exp):
        super().__init__()
        self.explorador = exp
        
    def OpenFile(self, n, t):
        self.explorador.OpenFile(n, t)

class Archivo:
    def __init__(self):
        self.nombre="A"
        self.tipo="b"
    
    def AbrirArchivo(self):
        print("Se abrio el archivo: "+self.nombre+self.tipo)

class TXT(Archivo):
    def __init__(self, n):
        self.nombre=n
        self.tipo=".txt"

class PDF(Archivo):
    def __init__(self, n):
        self.nombre=n
        self.tipo=".pdf"

def main():
    proxy = ProxyExplorer(Explorer())

    proxy.OpenFile("tarea", ".pdf")
    proxy.OpenFile("notas", ".txt")

if __name__ == '__main__':
    main()