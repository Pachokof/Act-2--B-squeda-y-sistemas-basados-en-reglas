
# Importar librerías necesarias
from collections import defaultdict, deque

# Base de conocimiento: Representación del sistema de transporte masivo
# Estructura: {Estación: [Estaciones conectadas]}
transporte = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'H'],
    'G': ['D', 'E', 'H'],
    'H': ['F', 'G']
}

# Reglas lógicas para moverse entre estaciones
def puede_moverse(estacion_actual, estacion_siguiente):
    """
    Regla lógica: Verifica si es posible moverse de una estación a otra.
    """
    return estacion_siguiente in transporte[estacion_actual]

# Algoritmo de búsqueda para encontrar la mejor ruta (BFS)
def encontrar_ruta(inicio, fin):
    """
    Encuentra la mejor ruta entre dos estaciones usando BFS.
    """
    cola = deque()  # Cola para BFS
    cola.append([inicio])  # Inicializar con la ruta que solo contiene el inicio
    visitados = set()  # Conjunto para evitar ciclos

    while cola:
        ruta = cola.popleft()  # Obtener la primera ruta de la cola
        estacion_actual = ruta[-1]  # Obtener la última estación de la ruta

        # Si llegamos al destino, retornar la ruta
        if estacion_actual == fin:
            return ruta

        # Si no ha sido visitada, explorar sus conexiones
        if estacion_actual not in visitados:
            visitados.add(estacion_actual)

            # Explorar todas las estaciones conectadas
            for estacion_siguiente in transporte[estacion_actual]:
                if puede_moverse(estacion_actual, estacion_siguiente):
                    nueva_ruta = list(ruta)  # Copiar la ruta actual
                    nueva_ruta.append(estacion_siguiente)  # Agregar la siguiente estación
                    cola.append(nueva_ruta)  # Agregar la nueva ruta a la cola

    # Si no se encuentra una ruta, retornar None
    return None

# Función principal
def main():
    # Puntos de inicio y fin
    inicio = 'A'
    fin = 'H'

    # Encontrar la mejor ruta
    ruta_optima = encontrar_ruta(inicio, fin)

    # Mostrar resultados
    if ruta_optima:
        print(f"La mejor ruta desde {inicio} hasta {fin} es: {' -> '.join(ruta_optima)}")
    else:
        print(f"No se encontró una ruta desde {inicio} hasta {fin}.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
    
    