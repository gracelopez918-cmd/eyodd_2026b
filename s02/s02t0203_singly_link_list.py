# Importando clase Node 
from s02t0201_Linked_list import Node

# Creando la clase de una lista enlazada
class SinglyLinkedList:
    # Consturctor de la clase de una lista enlazada
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Metodo de insercion de Nodo en la lista
    def append(self, data):
        # Creo el nodo
        new_node = Node(data)

        # Si hay un Tail, el nuevo nodo
        # Pasa a ser el nuevo Tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
         # Si no hay un tail
        else:
            self.tail = new_node
            self.head = new_node
        # Se incrementa size en 1
        self.size +=1

# Insertando en posicion intermedia  
def append_at_location(self, data, index):
    if index < 1 or index >= self.size + 1:
        raise IndexError(f"Index {index} fuera de ranga")

    # Creo el new node
    new_node = Node(data)

    # Insertando al inicio de la lista
    if index == 1:
        new_node.next = self.head
        self.head = new_node
        if self.size == None:
            self.tail = new_node
            # Incremento el size en 1 porque se agrego un nuevo nodo  
            self.size += 1
        # Creando variables de control para las inserciones en posiciones intermedias
        current = self.head
        previous = None
        position = 1

        # Traversal (Recorrido) de la lista hasta llegar a la posicion deseada
        while current is not None and position < index:
            previous = current
            current = current.next
            position += 1
        # Llego a la posicion deseada, ahora inserto el nuevo nodo
        # Estoy al final de la lista, entonces el nuevo nodo pasa a ser el tail
        if current is None:
            previous.next = new_node
            self.tail = new_node
            self.size += 1
            return

        # Si llegamos a una posición intermedia
        # 🚧 TODO: Pendiente de terminar🚧

# 1 Creo funcion principal 
def main():
    # Creando una instancia de una lista enlazada
    my_list = SinglyLinkedList()
    # Agregar elementos a la lista 
    my_list.append(30)
    my_list.append(59)
    my_list.append(80)
    my_list.append(100)

    # Recorrer la lista
    for value in my_list.head.iter():
        print(f"{value},", end="")
    print()

# evaluo el valor de __name__
if __name__ == "__main__":
    main()