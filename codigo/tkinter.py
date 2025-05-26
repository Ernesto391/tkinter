## ::::::::::::::::::::::::::::::::: ENCABEZADO :::::::::::::::::::::::::::::::::
# PRACTICA DE TKINTER
# Realizado por: PIÑA SALINAS LUIS ERNESTO
# Version: 1.0

# Descripcion: En una ventana de tkinter habra un menu en donde contendra 
# ejemplos de contenedores, estructuras de datos y grafos

## :::::::::::::::::::: IMPORTACION DE MODULOS Y BIBLIOTECAS ::::::::::::::::::::

import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

## :::::::::::::::::::::: DEFINICION DE FUNCIONES O CLASES ::::::::::::::::::::::

class Lista:
    def __init__(self):
        self.lista = []
    
    def anadir(self):
        texto = self.elemento.get()
        self.lista.append(texto)
        self.texto_lista.config(text=f'La lista es: {self.lista}')
        self.elemento.delete(0, tk.END)
    
    def eliminar(self):
        def aceptar():
            dato = int(posicion.get())
            if dato+1 > len(self.lista):
                messagebox.showerror("Error", f'{dato} esta fuera de rango')
            else:
                self.lista.pop(dato)
                self.texto_lista.config(text=f'La lista es: {self.lista}')
            ventana_eliminar.destroy()
            self.ventana1.lift()
            self.ventana1.focus_force() 

        if len(self.lista)>0:
            ventana_eliminar = tk.Toplevel(self.ventana1)
            ventana_eliminar.title = 'Eliminando'
            ventana_eliminar.geometry('425x300+800+400')
            tk.Label(ventana_eliminar, text='Escriba la posicion del elemento que desea eliminar de la lista', font=('Arial',12)).grid(row=0, column=0)
            posicion = tk.Entry(ventana_eliminar)
            posicion.grid(row=1, column=0)
            #Boton de confirmacion
            boton = tk.Button(ventana_eliminar, text = 'Aceptar', command=aceptar)
            boton.grid(row=2, column=0)
        else:
            messagebox.showerror('Error','No hay elementosa en la lista')
        self.ventana1.lift()
        self.ventana1.focus_force() 

    def ventana(self):
        self.ventana1 = tk.Toplevel()
        self.ventana1.title('Lista')
        self.ventana1.geometry('500x500+500+300')
        #Mostrar lista
        self.texto_lista = tk.Label(self.ventana1, text=f'La lista es: {self.lista}', font=('Arial',12))
        self.texto_lista.grid(row=0, column=0)
        tk.Label(self.ventana1, text='Escriba el elemento que desea añadir a la lista', font=('Arial',12)).grid(row=1, column=0)
        self.elemento = tk.Entry(self.ventana1)
        self.elemento.grid(row=1, column=1)
        #Boton para añadir
        botonA = tk.Button(self.ventana1, text = 'Añadir', command=self.anadir)
        botonA.grid(row=2, column=0)
        #Boton para eliminar
        botonB = tk.Button(self.ventana1, text = 'Eliminar', command=self.eliminar)
        botonB.grid(row=2, column=1)

class Conjunto:
    def __init__(self):
        self.conjunto = set()

    def anadir(self):
        texto = self.elemento.get()
        if texto in self.conjunto:
            messagebox.showerror("Error", f'{texto} ya existe en el conjunto')
        else:
            self.conjunto.add(texto)
            self.texto_conjunto.config(text=f'El conjunto es: {self.conjunto}')
        self.elemento.delete(0, tk.END)
        self.ventana1.lift()

    def eliminar(self):
        def aceptar():
            texto = valor.get()
            if texto not in self.conjunto:
                messagebox.showerror("Error", f'{texto} no esta en el conjunto')
            else:
                self.conjunto.remove(texto)
                if len(self.conjunto) > 0:
                    self.texto_conjunto.config(text=f'El conjunto es: {self.conjunto}')
                else:
                    self.texto_conjunto.config(text='El conjunto es: {}')
            self.ventana1.lift()
            self.ventana1.focus_force() 
            ventana_eliminar.destroy()

        if len(self.conjunto)>0:
            ventana_eliminar = tk.Toplevel(self.ventana1)
            ventana_eliminar.title = 'Eliminando'
            ventana_eliminar.geometry('425x300+800+400')
            tk.Label(ventana_eliminar, text='Escriba el valor del elemento que desea eliminar de la lista', font=('Arial',12)).grid(row=0, column=0)
            valor = tk.Entry(ventana_eliminar)
            valor.grid(row=1, column=0)
            #Boton de confirmacion
            boton = tk.Button(ventana_eliminar, text = 'Aceptar', command=aceptar)
            boton.grid(row=2, column=0)
        else:
            messagebox.showerror('Error', 'No hay elementos en el conjunto')
        self.ventana1.lift()
        self.ventana1.focus_force() 
            

    def ventana(self):
        self.ventana1 = tk.Toplevel()
        self.ventana1.title('Conjunto')
        self.ventana1.geometry('500x500+500+300')
        #Mostrar conjunto
        if len(self.conjunto)>0:
            self.texto_conjunto = tk.Label(self.ventana1, text=f'El conjunto es: {self.conjunto}', font=('Arial',12))
            self.texto_conjunto.grid(row=0, column=0)
        else:
            self.texto_conjunto = tk.Label(self.ventana1, text='El conjunto es: {}', font=('Arial',12))
            self.texto_conjunto.grid(row=0, column=0)
        tk.Label(self.ventana1, text='Escriba el elemento que desea añadir al conjunto', font=('Arial',12)).grid(row=1, column=0)
        self.elemento = tk.Entry(self.ventana1)
        self.elemento.grid(row=1, column=1)
        #Boton para añadir
        botonA = tk.Button(self.ventana1, text = 'Añadir', command=self.anadir)
        botonA.grid(row=2, column=0)
        #Boton para eliminar
        botonB = tk.Button(self.ventana1, text = 'Eliminar', command=self.eliminar)
        botonB.grid(row=2, column=1)

class Diccionario:
    def __init__(self):
        self.diccionario = {}

    def eliminar(self):
        def aceptar():
            texto = clave.get()
            if texto not in self.diccionario:
                messagebox.showerror("Error", f'{texto} no existe')
            else:
                self.diccionario.pop(texto)
                self.texto_diccionario.config(text=f'El diccionario es: {self.diccionario}')
            self.ventana1.lift()
            self.ventana1.focus_force() 
            ventana_eliminar.destroy()
        
        if len(self.diccionario)>0:
            ventana_eliminar = tk.Toplevel(self.ventana1)
            ventana_eliminar.title = 'Eliminando'
            ventana_eliminar.geometry('450x300+800+450')
            tk.Label(ventana_eliminar, text='Escriba la clave que desea eliminar del diccionario', font=('Arial',12)).grid(row=0, column=0)
            clave = tk.Entry(ventana_eliminar)
            clave.grid(row=1, column=0)
            #Boton de confirmacion
            boton = tk.Button(ventana_eliminar, text = 'Aceptar', command=aceptar)
            boton.grid(row=2, column=0)
        else:
            messagebox.showerror('Error','No hay elementos en el diccionario')
        self.ventana1.lift()
        self.ventana1.focus_force() 

    def anadir(self):
        clave = self.clave.get()
        valor = self.valor.get()    
        self.diccionario[clave] = valor
        self.texto_diccionario.config(text=f'El diccionario es: {self.diccionario}')
        self.clave.delete(0, tk.END)
        self.valor.delete(0, tk.END)

    def actualizar(self):
        def aceptar():
            claveAc = clave.get()
            valorAc = valor.get()
            if claveAc not in self.diccionario:
                messagebox.showerror("Error", f'{claveAc} no existe')
            else:
                self.diccionario[claveAc] = valorAc
                self.texto_diccionario.config(text=f'El diccionario es: {self.diccionario}')
            self.ventana1.lift()
            self.ventana1.focus_force() 
            ventana_actualizar.destroy()
        
        if len(self.diccionario)>0:
            ventana_actualizar = tk.Toplevel(self.ventana1)
            ventana_actualizar.title = 'Actualizando'
            ventana_actualizar.geometry('450x300+800+450')
            tk.Label(ventana_actualizar, text='Escriba la clave que desea actualizar', font=('Arial',12)).grid(row=0, column=0)
            clave = tk.Entry(ventana_actualizar)
            clave.grid(row=0, column=1)
            tk.Label(ventana_actualizar, text='Escriba el valor que desea actualizar', font=('Arial',12)).grid(row=1, column=0)
            valor = tk.Entry(ventana_actualizar)
            valor.grid(row=1, column=1)
            #Boton de confirmacion
            boton = tk.Button(ventana_actualizar, text = 'Aceptar', command=aceptar)
            boton.grid(row=2, column=0)
        else:
            messagebox.showerror('Error', 'No hay elementos en el diccionario')
        self.ventana1.lift()
        self.ventana1.focus_force() 

    def ventana(self):
        self.ventana1 = tk.Toplevel()
        self.ventana1.title('Diccionario')
        self.ventana1.geometry('700x500+500+300')
        #Mostrar diccionario
        self.texto_diccionario = tk.Label(self.ventana1, text=f'El diccionario es: {self.diccionario}', font=('Arial',12))
        self.texto_diccionario.grid(row=0, column=0)
        tk.Label(self.ventana1, text='Escriba la clave que desea añadir al diccionario', font=('Arial',12)).grid(row=1, column=0)
        self.clave = tk.Entry(self.ventana1)
        self.clave.grid(row=1, column=1)
        tk.Label(self.ventana1, text='Escriba el valor que desea añadir al diccionario', font=('Arial',12)).grid(row=2, column=0)
        self.valor = tk.Entry(self.ventana1)
        self.valor.grid(row=2, column=1)
        #Boton para añadir
        botonA = tk.Button(self.ventana1, text = 'Añadir', command=self.anadir)
        botonA.grid(row=3, column=0)
        #Boton para eliminar
        botonB = tk.Button(self.ventana1, text = 'Eliminar', command=self.eliminar)
        botonB.grid(row=3, column=1)
        #Boton para actualizar
        botonC = tk.Button(self.ventana1, text = 'Actualizar', command=self.actualizar)
        botonC.grid(row=3, column=2)

class Pila:
    def __init__(self):
        self.pila = []
        self.contador = 0

    def anadir(self):
        self.pila.append(self.contador)
        self.texto_pila.config(text=f'{self.pila}')
        self.contador += 1

    def eliminar(self):
        if len(self.pila)>0:
            self.pila.pop()
            self.texto_pila.config(text=f'{self.pila}')
            self.contador -= 1
        else:
            messagebox.showerror("Error", f'No hay elementos en la pila')
        self.ventana1.lift()

    def ventana(self):
        self.ventana1 = tk.Toplevel()
        self.ventana1.title('Pila')
        self.ventana1.geometry('500x500+500+300')
        #Mostrar Pila
        tk.Label(self.ventana1, text=f'Representacion de la pila', font=('Arial',16)).grid(row=0, column=0)
        self.texto_pila = tk.Label(self.ventana1, text=f'{self.pila}', font=('Arial',16))
        self.texto_pila.grid(row=1, column=0)
        #Boton para añadir
        botonA = tk.Button(self.ventana1, text = 'Añadir', command=self.anadir)
        botonA.grid(row=2, column=0)
        #Boton para eliminar
        botonB = tk.Button(self.ventana1, text = 'Eliminar', command=self.eliminar)
        botonB.grid(row=2, column=1) 

class Cola:
    def __init__(self):
        self.cola = []
        self.contador = 0

    def anadir(self):
        self.cola.append(self.contador)
        self.texto_cola.config(text=f'{self.cola}')
        self.contador += 1

    def eliminar(self):
        if len(self.cola)>0:
            self.cola.pop(0)
            self.texto_cola.config(text=f'{self.cola}')
        else:
            messagebox.showerror("Error", f'No hay elementos en la cola')
        self.ventana1.lift()

    def ventana(self):
        self.ventana1 = tk.Toplevel()
        self.ventana1.title('Cola')
        self.ventana1.geometry('500x500+500+300')
        #Mostrar Cola
        tk.Label(self.ventana1, text=f'Representacion de la cola', font=('Arial',16)).grid(row=0, column=0)
        self.texto_cola = tk.Label(self.ventana1, text=f'{self.cola}', font=('Arial',16))
        self.texto_cola.grid(row=1, column=0)
        #Boton para añadir
        botonA = tk.Button(self.ventana1, text = 'Añadir', command=self.anadir)
        botonA.grid(row=2, column=0)
        #Boton para eliminar
        botonB = tk.Button(self.ventana1, text = 'Eliminar', command=self.eliminar)
        botonB.grid(row=2, column=1) 

class GrafoDirigido:
    def __init__(self):
        self.adyacencias = {}
        self.atributos = {}
        pelicula = {
            "Dune": {"genero": "Sci-fi","director": "Denis Villeneuve","estilo": "Epico"},
            "Sicario": {"genero": "Accion","director": "Denis Villeneuve","estilo": "Realista"},
            "2001: Odisea espacial": {"genero": "Sci-fi","director": "Stanley Kubrick","estilo": "Estetico"},
            "Interstellar": {"genero": "Sci-fi","director": "Christopher Nolan","estilo": "Epico"},
            "El gran hotel Budapest": {"genero": "Comedia","director": "Wes Anderson","estilo": "Estetico"}
        }

    def crearNodo(self, nodos, pelicula):
        for nombre, atributo in pelicula.items():
            nodo = f"{nombre}\n {atributo['genero']}\n{atributo['director']}"
            nodos.append(nodo)
            grafo.add_node(nodo)
            self.atributos[nodo] = atributo

    def crearAristas(self, nodos):
        for i in range(len(nodos)):
            for j in range(i + 1, len(nodos)):
                nodo1, nodo2 = nodos[i], nodos[j]
                atributo1, atributo2 = self.atributos[nodo1], self.atributos[nodo2]

                # Conexión por género
                if atributo1['genero'] == atributo2['genero']:
                    grafo.add_edge(nodo1, nodo2)

                # Conexión por director
                elif atributo1['director'] == atributo2['director']:
                    grafo.add_edge(nodo1, nodo2)

                # Conexion por estilo visual
                elif atributo1['estilo'] == atributo2['estilo']:
                    grafo.add_edge(nodo1, nodo2)

    def bfs(self, inicio):
            visitados = set()
            cola = deque([inicio])
            recorrido = []

            while cola:
                nodo = cola.popleft()
                if nodo not in visitados:
                    visitados.add(nodo)
                    recorrido.append(nodo)
                    vecinos = list(grafo.successors(nodo))
                    cola.extend([vecino for vecino in vecinos if vecino not in visitados])

            return recorrido

class Principal:
    def __init__(self):
        self.lista = Lista()
        self.conjunto = Conjunto()
        self.diccionario = Diccionario()
        self.pila = Pila()
        self.cola = Cola()
        self.grafoDirigido = GrafoDirigido()
        self.crearMenu()
    
    def crearMenu(self):
        ventana = tk.Tk()
        ventana.title('Portafolio de evidencia')
        ventana.geometry('500x500+500+240')
        #Creacion del menu
        menu_principal = tk.Menu()
        #Creacion salir
        menu_principal.add_command(label='Salir', command=ventana.destroy)
        #Creacion contenedores
        menu_contenedores = tk.Menu(menu_principal, tearoff=0)
        menu_contenedores.add_command(label='Lista', command=self.lista.ventana)
        menu_contenedores.add_command(label='Conjunto', command=self.conjunto.ventana)
        menu_contenedores.add_command(label='Diccionario', command=self.diccionario.ventana)
        menu_principal.add_cascade(label='Contenedores', menu=menu_contenedores)
        #Creacion de estructura de datos
        menu_estructuraDatos = tk.Menu(menu_principal, tearoff=0)
        menu_estructuraDatos.add_command(label='Pila', command=self.pila.ventana)
        menu_estructuraDatos.add_command(label='Cola', comman=self.cola.ventana)
        menu_principal.add_cascade(label='Estructura de datos', menu=menu_estructuraDatos)
        #Creacion grafos
        menu_grafos = tk.Menu(menu_principal, tearoff=0)
        menu_grafos.add_command(label='Grafos dirigido')
        menu_grafos.add_command(label='Grafo NO dirigido')
        menu_principal.add_cascade(label='Grafos', menu=menu_grafos)
        ventana.config(menu=menu_principal)
        ventana.mainloop()

## :::::::::::::::::::::::: VARIABLES U OBJETOS GLOBALES ::::::::::::::::::::::::

grafo = nx.DiGraph()
nodos = []

## :::::::::::::::::::::::::::::: BLOQUE PRINCIPAL ::::::::::::::::::::::::::::::

if __name__ == '__main__':
    menu = Principal()

    plt.gcf().canvas.manager.set_window_title('Grafo dirigido')

    nx.draw(grafo, with_labels=True)
    plt.show()

    
