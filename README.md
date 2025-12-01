# RAICES DE ECUACIONES  
**INFORMATICA – UMSA**

**Autor:** Carlos Manuel Miranda Aguirre  
**CI:** 13759486  
**RU:** 1825954  
**Carrera:** Informatica  
**Universidad:** Universidad Mayor de San Andres (UMSA)  

---

## 1. Descripcion general del proyecto

Este proyecto implementa y compara metodos numericos para la **determinacion de raices de ecuaciones no lineales**.  

Se trabajan cuatro ecuaciones del libro (seccion 9.6 – Problems) y se desarrollan tres herramientas paralelas:

1. **Hojas de calculo (Excel):** desarrollo paso a paso de cada metodo, mostrando todas las iteraciones.
2. **Programas en Python:** implementacion de los metodos con graficos de la funcion y de las raices.
3. **Pagina web interactiva (GitHub Pages):** permite ingresar una funcion \( f(x) \) cualquiera y aplicar Biseccion, Newton o Secante de forma visual.

El objetivo es entender el algoritmo, comprobar los resultados y comparar eficiencia (numero de iteraciones y comportamiento grafico).

---

## 2. Problemas resueltos

Se implementan los metodos para las siguientes ecuaciones:

1. \( x^3 - e^{0.8x} = 20 \)  
   – Dos soluciones en el intervalo \( 0 \le x \le 8 \).

2. \( 3 \sin(0.5x) - 0.5x + 2 = 0 \).

3. \( x^3 - x^2 e^{-0.5x} - 3x = -1 \)  
   – Tres raices reales (una negativa, una cercana a 0 y una positiva).

4. \( \cos^2(x) - 0.5x e^{0.3x} + 5 = 0 \)  
   – Raices positivas.

En cada caso se usan los tres metodos (Biseccion, Newton y Secante) y se comparan sus resultados.

---

## 3. Metodos numericos implementados

- **Biseccion:**  
  Metodo robusto basado en dividir un intervalo \([a,b]\) donde \( f(a) \cdot f(b) < 0 \). Garantiza convergencia, pero requiere muchas iteraciones.

- **Newton-Raphson:**  
  Metodo de orden cuadratico que utiliza la derivada de la funcion (o derivada numerica) para construir una sucesion de la forma  
  \( x_{k+1} = x_k - f(x_k)/f'(x_k) \). Es muy rapido si el punto inicial es adecuado.

- **Secante:**  
  Variante de Newton que evita calcular la derivada analitica, aproximando \( f'(x) \) con una recta secante entre dos puntos. Suele ser mas rapido que biseccion y no requiere derivada exacta.

---

## 4. Estructura del repositorio

- `Raices de Ecuaciones.xlsx`  
  Hojas de calculo con la implementacion paso a paso de los metodos:
  - Tablas de iteracion para Biseccion, Newton y Secante.
  - Calculo explcito de los errores en cada paso.
  - Resultados finales comparables con Python y la pagina web.

- Carpeta **`Codigo Python`**  
  Contiene cuatro archivos principales (uno por ejercicio):

  - `ejercicio1_raices.py`  
    Metodos Biseccion, Newton y Secante para \( x^3 - e^{0.8x} - 20 = 0 \).

  - `ejercicio2_raiz.py`  
    Metodos para \( 3 \sin(0.5x) - 0.5x + 2 = 0 \).

  - `ejercicio3_tres_raices.py`  
    Metodos para \( x^3 - x^2 e^{-0.5x} - 3x + 1 = 0 \) (tres raices).

  - `ejercicio4_raiz.py`  
    Metodos para \( \cos^2(x) - 0.5x e^{0.3x} + 5 = 0 \).

  Cada archivo:
  - Define la funcion \( f(x) \) (y \( f'(x) \) cuando es necesario).
  - Implementa las funciones `bisection`, `newton` y `secant`.
  - Imprime las raices aproximadas y el numero de iteraciones.
  - Genera un grafico de la funcion con las raices marcadas.

- Carpeta **`Capturas`**  
  Capturas de pantalla de:
  - Las hojas de calculo con las iteraciones.
  - La ejecucion de los scripts de Python.
  - La pagina web interactiva.

- `index.html` (antes `main.html`)  
  Pagina web interactiva desplegada en **GitHub Pages**.

- `README.md`  
  Este documento de explicacion para la docente.

---

## 5. Pagina web interactiva (GitHub Pages)

La pagina web permite experimentar con **cualquier funcion**:

- El usuario ingresa la expresion de \( f(x) \) en formato JavaScript, por ejemplo:
  - `x**3 - Math.exp(0.8*x) - 20`
  - `3*Math.sin(0.5*x) - 0.5*x + 2`
- Selecciona el metodo:
  - Biseccion (con intervalo [a, b]).
  - Newton (con valor inicial x0).
  - Secante (con valores iniciales x0 y x1).
- Define la tolerancia y el numero maximo de iteraciones.

La pagina muestra:

- La raiz aproximada y el numero de iteraciones del metodo elegido.
- Una **tabla de iteraciones** con los valores que se usarian en una hoja de calculo:
  - Biseccion: \( a_k, b_k, c_k, f(a_k), f(b_k), f(c_k), error \).
  - Newton: \( x_k, f(x_k), f'(x_k), error \).
  - Secante: \( x_{k-1}, x_k, f(x_{k-1}), f(x_k), x_{k+1}, error \).
- Un **grafico de la funcion** en el intervalo de trabajo, marcando la raiz obtenida.

La pagina esta publicada en:

`https://manuelaguirre3002-beep.github.io/RAICES-DE-ECUACIONES/`

y esta pensada como apoyo visual para el curso: permite ver rapidamente como se comporta cada metodo al cambiar intervalos o puntos iniciales.

---

## 6. Como ejecutar el proyecto

### 6.1. Hojas de calculo (Excel)

1. Abrir el archivo `Raices de Ecuaciones.xlsx`.
2. En cada hoja se encuentran las tablas de:
   - Biseccion, Newton y Secante.
3. Se puede seguir la formula de cada celda para ver paso a paso como se actualizan los valores y los errores.

### 6.2. Programas en Python

Requisitos:

- Python 3.x
- Biblioteca `matplotlib`

Instalacion rapida:

```bash
pip install matplotlib
