## ::::::::::::::::::::::::::::::::: ENCABEZADO :::::::::::::::::::::::::::::::::
''''
PRACTICA DE TKINTER
Realizado por: PIÑA SALINAS LUIS ERNESTO

Descripcion: En una ventana de tkinter habra un menu en donde contendra 
ejemplos de contenedores, estructuras de datos y grafos

Version 1.3
Modificaciones:
+ Se agrego la clase ABB
+ Se agrego el url codigo/imagenes/arbol_binario en el metodo verArbol()

'''
## :::::::::::::::::::: IMPORTACION DE MODULOS Y BIBLIOTECAS ::::::::::::::::::::

import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from graphviz import Digraph
from PIL import Image, ImageTk

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
        self.nodos = []
        self.adyacencias = {}
        self.atributos = {}
        self.pelicula = {
            "Dune": {"genero": "Sci-fi","director": "Denis Villeneuve","estilo": "Epico"},
            "Sicario": {"genero": "Accion","director": "Denis Villeneuve","estilo": "Realista"},
            "2001: Odisea espacial": {"genero": "Sci-fi","director": "Stanley Kubrick","estilo": "Estetico"},
            "Interstellar": {"genero": "Sci-fi","director": "Christopher Nolan","estilo": "Epico"},
            "El gran hotel Budapest": {"genero": "Comedia","director": "Wes Anderson","estilo": "Estetico"}
        }
        self.crearNodo()
        self.crearAristas()

    def crearNodo(self):
        for nombre, atributo in self.pelicula.items():
            nodo = nombre
            self.nodos.append(nodo)
            grafo.add_node(nodo)
            self.atributos[nodo] = atributo

    def crearAristas(self):
        for i in range(len(self.nodos)):
            for j in range(i + 1, len(self.nodos)):
                nodo1, nodo2 = self.nodos[i], self.nodos[j]
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

    def verGrafo(self):
        plt.gcf().canvas.manager.set_window_title('Grafo dirigido')
        nx.draw(grafo, with_labels=True)
        plt.show()

class GradoNoDirigido:
    def __init__(self):
        self.nodos = []
        self.adyacencias = {}
        self.atributos = {}
        self.pelicula = ['A', 'B', 'C', ]
        self.crearAristas()

    def crearAristas(self):
        grafoNoDirigido.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('B','E')])

    def verGrafo(self):
        plt.gcf().canvas.manager.set_window_title('Grafo NO dirigido')
        nx.draw(grafoNoDirigido, with_labels=True)
        plt.show()

class Nodo:
    def __init__(self, boleta, nombre, prom):
        self.boleta = boleta
        self.nombre = nombre
        self.prom = prom
        self.izq = None
        self.der = None

    def __str__(self):
        return f"{self.boleta} - {self.nombre} - {self.prom: .3}"

class ABB:
    def __init__(self):
        self.raiz = None
        self.personas = []
        self.personasIniciales = {
            'Caridad Medina':{
                'boleta':20252280,
                'prom': 9.567
            },
            'Wes Anderson':{
                'boleta':20252023,
                'prom':9.654
            },
            'Josh Dun':{
                'boleta':20254567,
                'prom':7.478
            },
            'Luz Shelby':{
                'boleta':20251234,
                'prom': 8.785
            },
            'Camilo Villaruel':{
                'boleta':20257890,
                'prom': 7.987
            }
        }
        for nombre, atributos in self.personasIniciales.items():
            boleta = atributos['boleta']
            prom = atributos['prom']
            if self.raiz is None:
                self.raiz = Nodo(boleta, nombre, prom)
            else:
                self._insertar_recursivo(self.raiz, boleta, nombre, prom)

    def _insertar_recursivo(self, nodo, boleta, nombre, prom):
        if boleta < nodo.boleta:
            if nodo.izq is None:
                nodo.izq = Nodo(boleta, nombre, prom)
            else:
                self._insertar_recursivo(nodo.izq, boleta, nombre, prom)
        elif boleta > nodo.boleta:
            if nodo.der is None:
                nodo.der = Nodo(boleta, nombre, prom)
            else:
                self._insertar_recursivo(nodo.der, boleta, nombre, prom)

    def visualizar(self):
        punto = Digraph()
        punto.attr('node', shape='rectangle')
        if self.raiz is not None:
            self._visualizar_recursivo(self.raiz, punto)
            return punto

    def _visualizar_recursivo(self, nodo, punto):
        punto.node(f'{nodo.boleta}\n{nodo.nombre}\n{nodo.prom: .3}')
        if nodo.izq is not None:
            punto.edge(f'{nodo.boleta}\n{nodo.nombre}\n{nodo.prom: .3}', f'{nodo.izq.boleta}\n{nodo.izq.nombre}\n{nodo.izq.prom: .3}')
            self._visualizar_recursivo(nodo.izq, punto)
        if nodo.der is not None:
            punto.edge(f'{nodo.boleta}\n{nodo.nombre}\n{nodo.prom: .3}', f'{nodo.der.boleta}\n{nodo.der.nombre}\n{nodo.der.prom: .3}')
            self._visualizar_recursivo(nodo.der, punto)

    def inorden(self):
        self.recorrido = []
        self._inorden_recursivo(self.raiz)
        texto = f'Recorrido Inorden:\n' + '\n'.join(str(elemento) for elemento in self.recorrido)
        self.mostrar.configure(text=texto)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izq)
            actual = nodo.__str__()
            self.recorrido.append(actual)
            self._inorden_recursivo(nodo.der)

    def preorden(self):
        self.recorrido = []
        self._preorden_recursivo(self.raiz)
        texto = f'Recorrido Preorden:\n' + '\n'.join(str(elemento) for elemento in self.recorrido)
        self.mostrar.configure(text=texto)

    def _preorden_recursivo(self, nodo):
        if nodo is not None:
            actual = nodo
            self.recorrido.append(actual)
            self._preorden_recursivo(nodo.izq)
            self._preorden_recursivo(nodo.der)

    def postorden(self):
        self.recorrido = []
        self._postorden_recursivo(self.raiz)
        texto = f'Recorrido Postorden:\n' + '\n'.join(str(elemento) for elemento in self.recorrido)
        self.mostrar.configure(text=texto)

    def _postorden_recursivo(self, nodo):
        if nodo is not None:
            self._postorden_recursivo(nodo.izq)
            self._postorden_recursivo(nodo.der)
            actual = nodo.__str__()
            self.recorrido.append(actual)

    def insertar(self):
        boleta = int(self.boletaEntry.get())
        nombre = self.nombreEntry.get()
        parcial1 = int(self.parcial1Entry.get())
        parcial2 = int(self.parcial2Entry.get())
        parcial3 = int(self.parcial3Entry.get())
        prom = (parcial1 + parcial2 + parcial3)/3
        if self.raiz is None:
            self.raiz = Nodo(boleta, nombre, prom)
        else:
            self._insertar_recursivo(self.raiz, boleta, nombre, prom)
        messagebox.showinfo("Éxito", "Persona insertada en el árbol.")
        self.boletaEntry.delete(0, tk.END)
        self.nombreEntry.delete(0, tk.END)
        self.parcial1Entry.delete(0, tk.END)
        self.parcial2Entry.delete(0, tk.END)
        self.parcial3Entry.delete(0, tk.END)

    def verArbol(self):
        # Cracion de la ventana para ver el arbol
        self.ventanaArbol = tk.Toplevel(self.ventana)
        self.ventanaArbol.title('Viendo el arbol')
        self.ventanaArbol.geometry('500x500+500+240')

        # Creacion del espacio para ver el arbol
        imagenArbol = tk.Label(self.ventanaArbol)
        imagenArbol.pack(pady=10)

        # Creacion de la imagen del arbol
        dot = self.visualizar()
        if dot:
            dot.render("imagen/imagen_arbol", format="png", cleanup=True)
            imagen = Image.open("imagen/imagen_arbol.png")
            imagen = imagen.resize((500, 500))
            self.imagen_tk = ImageTk.PhotoImage(imagen)

            imagenArbol.configure(image=self.imagen_tk)
            imagenArbol.image = self.imagen_tk
        else:
            messagebox.showinfo("Árbol vacío", "No hay elementos en el árbol.")

    def buscar(self):
        # Modificar el texto en pantalla
        def aceptar():
            boleta = int(self.busqueda.get())
            if self._buscar_recursivo(self.raiz, boleta):
                messagebox.showinfo('Exito', f'La boleta {boleta} esta inscrita')
            else:
                messagebox.showinfo('Error', f'La boleta {boleta} NO esta inscrita')
            self.busqueda.destroy()
            self.botonBusqueda.destroy()
            self.boletaBusqueda.destroy()

        # Limpiar texto de pantalla
        self.mostrar.configure(text='')
        tk.Label(self.ventana, text=' ', font=('Arial', 16)).grid(row=8, column=0)
        self.boletaBusqueda = tk.Label(self.ventana, text='Escriba la boleta a buscar', font=('Arial', 16))
        self.boletaBusqueda.grid(row=9, column=0)
        self.busqueda = tk.Entry(self.ventana)
        self.busqueda.grid(row=9, column=1)
        self.botonBusqueda = tk.Button(self.ventana, text='Aceptar', command=lambda: aceptar())
        self.botonBusqueda.grid(row=9, column=3)

    def _buscar_recursivo(self, nodo, boleta):
        if nodo is None:
            return False
        elif boleta == nodo.boleta:
            return True
        elif boleta < nodo.boleta:
            return self._buscar_recursivo(nodo.izq, boleta)
        else:
            return self._buscar_recursivo(nodo.der, boleta)

    def eliminar(self):
        # Modificar el texto en pantalla
        def aceptar():
            # Comprobar si la boleta existe
            boleta = int(self.borrar.get())
            if self._buscar_recursivo(self.raiz, boleta):
                self._eliminar_recursivo(self.raiz, boleta)
                messagebox.showinfo('Exito', f'Se ha eliminado la boleta: {boleta}')
            else:
                messagebox.showerror('Error', f'No existe la boleta: {boleta}')
            self.borrar.destroy()
            self.botonEliminar.destroy()
            self.boletaEliminar.destroy()

        # Limpiar texto de la pantalla
        self.mostrar.configure(text='')
        tk.Label(self.ventana, text=' ', font=('Arial', 16)).grid(row=8, column=0)
        self.boletaEliminar = tk.Label(self.ventana, text='Escriba la boleta a eliminar', font=('Arial', 16))
        self.boletaEliminar.grid(row=9, column=0)
        self.borrar = tk.Entry(self.ventana)
        self.borrar.grid(row=9, column=1)
        self.botonEliminar = tk.Button(self.ventana, text='Aceptar', command=lambda: aceptar())
        self.botonEliminar.grid(row=9, column=3)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        elif valor < nodo.boleta:
            nodo.izq = self._eliminar_recursivo(nodo.izq, valor)
        elif valor > nodo.boleta:
            nodo.der = self._eliminar_recursivo(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            sucesor = self._minimo_nodo(nodo.der)
            nodo.boleta = sucesor.boleta
            nodo.nombre = sucesor.nombre
            nodo.prom = sucesor.prom
            nodo.der = self._eliminar_recursivo(nodo.der, sucesor.boleta)
        return nodo

    def profundidad(self):
        if self.raiz is None:
            messagebox.showerror('ERROR', 'No hay datos')
        else:
            prof = self._profundidad_recursiva(self.raiz)
            messagebox.showinfo('Exito', f'La profundidad es: {prof}')

    def _profundidad_recursiva(self, nodo):
        if nodo is None:
            return 0
        izq = self._profundidad_recursiva(nodo.izq)
        der = self._profundidad_recursiva(nodo.der)
        return 1 + max(izq, der)

    def crearVentana(self):
        # Creacion de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title('Arbol binario')
        self.ventana.geometry('700x500+300+240')

        # Creacion de la interfaz interactiva con el usuario
          ## Especificacion al ususario de que colocar
        tk.Label(self.ventana, text=f'Boleta:', font=('Arial',16)).grid(row=0, column=0)
        tk.Label(self.ventana, text=f'Nombre:', font=('Arial',16)).grid(row=0, column=2)
        tk.Label(self.ventana, text=f'Calificacion del primer parcial', font=('Arial',16)).grid(row=1, column=0)
        tk.Label(self.ventana, text=f'Calificacion del segundo parcial', font=('Arial',16)).grid(row=2, column=0)
        tk.Label(self.ventana, text=f'Calificacion del tercer parcial', font=('Arial',16)).grid(row=3, column=0)
        tk.Label(self.ventana, text=' ', font=('Arial',16)).grid(row=4, column=0) # Esta parte es para crear un espacio en blanco y mejorar el diseño
        tk.Label(self.ventana, text=' ', font=('Arial',16)).grid(row=6, column=0) # Esta parte es para crear un espacio en blanco y mejorar el diseño
        self.mostrar = tk.Label(self.ventana, text=' ', font=('Arial',16))
        self.mostrar.grid(row=10, column=0)
          ## Creacion de las entradas de datos
        self.boletaEntry = tk.Entry(self.ventana)
        self.boletaEntry.grid(row=0, column=1)
        self.nombreEntry = tk.Entry(self.ventana)
        self.nombreEntry.grid(row=0, column=3)
        self.parcial1Entry = tk.Entry(self.ventana)
        self.parcial1Entry.grid(row=1, column=1)
        self.parcial2Entry = tk.Entry(self.ventana)
        self.parcial2Entry.grid(row=2, column=1)
        self.parcial3Entry = tk.Entry(self.ventana)
        self.parcial3Entry.grid(row=3, column=1)

        # Creacion de botones
        botonA = tk.Button(self.ventana, text='Insertar', command=lambda: self.insertar())
        botonA.grid(row=5, column=0)
        botonEliminar = tk.Button(self.ventana, text='Eliminar', command=lambda: self.eliminar())
        botonEliminar.grid(row=5, column=1)
        botonBuscar = tk.Button(self.ventana, text='Buscar', command=lambda: self.buscar())
        botonBuscar.grid(row=5, column=2)
        botonB = tk.Button(self.ventana, text='Ver el arbol', command=self.verArbol)
        botonB.grid(row=5, column=3)
        botonC = tk.Button(self.ventana, text='Recorrido Inorden', command=lambda: self.inorden())
        botonC.grid(row=7, column=0)
        botonD = tk.Button(self.ventana, text='Recorrido Preorden', command=lambda: self.preorden())
        botonD.grid(row=7, column=1)
        botonE = tk.Button(self.ventana, text='Recorrido Postorden', command=lambda: self.postorden())
        botonE.grid(row=7, column=2)
        botonProfundidad = tk.Button(self.ventana, text='Profundidad', command=lambda: self.profundidad())
        botonProfundidad.grid(row=7, column=3)

        self.ventana.mainloop()

class Principal:
    def __init__(self):
        self.lista = Lista()
        self.conjunto = Conjunto()
        self.diccionario = Diccionario()
        self.pila = Pila()
        self.cola = Cola()
        self.grafoDirigido = GrafoDirigido()
        self.grafoNoDirigido = GradoNoDirigido()
        self.ABB = ABB()
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
        menu_estructuraDatos.add_command(label='Cola', command=self.cola.ventana)
        menu_principal.add_cascade(label='Estructura de datos', menu=menu_estructuraDatos)
        #Creacion grafos
        menu_grafos = tk.Menu(menu_principal, tearoff=0)
        menu_grafos.add_command(label='Grafos dirigido', command=self.grafoDirigido.verGrafo)
        menu_grafos.add_command(label='Grafo NO dirigido', command=self.grafoNoDirigido.verGrafo)
        menu_grafos.add_command(label='Arbol binario', command=self.ABB.crearVentana)
        menu_principal.add_cascade(label='Grafos', menu=menu_grafos)
        ventana.config(menu=menu_principal)
        ventana.mainloop()

## :::::::::::::::::::::::: VARIABLES U OBJETOS GLOBALES ::::::::::::::::::::::::

grafo = nx.DiGraph()
grafoNoDirigido = nx.Graph()
nodos = []

## :::::::::::::::::::::::::::::: BLOQUE PRINCIPAL ::::::::::::::::::::::::::::::

if __name__ == '__main__':
    menu = Principal()
## :::::::::::::::::::::::::::::::: COMENTARIOS :::::::::::::::::::::::::::::::::
'''
Es necesario descargar las siguientes bibliotecas:
pip install pillow
pip install graphviz pillow


Ademas se debe tener instalado Graphviz en el sistema y agregado en el PATH
para que funcione el codigo.
link de descarga: https://graphviz.org/download/

'''

    
