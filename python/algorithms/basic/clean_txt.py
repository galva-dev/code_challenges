def quitar_lineas_vacias(archivo_entrada, archivo_salida):
  """
  Función para quitar las líneas en blanco de un archivo de texto.

  Args:
    archivo_entrada: ruta del archivo de entrada.
    archivo_salida: ruta del archivo de salida.
  """
  with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
    # Lee cada línea del archivo de entrada
    for linea in entrada:
      # Revisa si la línea contiene solo espacios en blanco
      if not linea.isspace():
        # Si no es una línea en blanco, escríbela en el archivo de salida
        salida.write(f"0 -0.5 {str(linea)}" )

# Ejemplo de uso
archivo_entrada = '/home/alvaro/Documents/My Code/code_challenges/python/algorithms/basic/resources/dirty.txt'
archivo_salida = '/home/alvaro/Documents/My Code/code_challenges/python/algorithms/basic/resources/clean.txt'

quitar_lineas_vacias(archivo_entrada, archivo_salida)
