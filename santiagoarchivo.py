#class Empleado :
   # def __init__(self,nombre):
   #     self.nombre= nombre
 #   def Trabajar (self):
  #      print(self.nombre,"El empleado esta trabajando")
#class Programador(Empleado):
 #   def Trabajar(self):
  #    print(self.nombre," esta programando")
#class Disenador(Empleado):
  #  def Trabajar(self):
 #       print(self.nombre," esta diseñando")

#empleado1= Empleado("santiago")
#prog=Programador("luis")
#dis = Disenador  ("laura")


#Empleados = [empleado1,prog,dis]


#for dis in Empleados:
 #   dis.Trabajar()


class Animal :
    def __init__(self,nombre):
        self.nombre=nombre
    def mostrar_accion (self):
        print(self.nombre,"has corrido")
class Perro(Animal):
        def mostrar_accion(self):
            print(self.nombre,"se ha sentado")
class Gato(Animal):
        def mostrar_accion(self):
              print(self.nombre,"se ha mojado")
class Pajaro(Animal):
        def mostrar_accion(self):
            print(self.nombre,"a comido")


perr = Perro("bobby")
gat =Gato("white")
paj = Pajaro ("chipi")

 #animales = [perr,gat,paj]
#for Animal in animales :
 #     Animal.mostrar_accion()


class Calculadora :
     def __init__(self,numero1,numero2) :
          self.numero1 = numero1
          self.numero2 = numero2
     def Duplicar(self):
           suma = self = self.numero1 + self.numero2
           return suma * 2
          

resultado = Calculadora(5,5)
resul = resultado.Duplicar()
print(resul)


class Instrumento :
      def __init__(self,nombre):
            self.nombre= nombre
      def tocar(self):
            print(self.nombre , "estas tocando tu instrumento")
class Guitarra (Instrumento) :
      def tocar(self):
            print(self.nombre,"estas tocando tu guitarra")
class Piano(Instrumento):
      def tocar(self):
            print(self.nombre,"estas tocando piano")
class Bateria (Instrumento):
      def tocar(self):
            print (self.nombre,"estas tocando bateria")
pia = Guitarra("danae")
gui = Piano("daniel")
ba = Bateria("luis")

inst = [pia,gui,ba]
for Instrumento in inst :
      Instrumento.tocar ()



