https://www.codingame.com/profile/26a602cf8b1f1e239334331005872dd53408704


https://www.codingame.com/training/hard/her-majestys-well-shared-secret

# El Secreto Mejor Guardado de Su Majestad

Algunas información secreta ha sido compartida entre los agentes de doble cero de Su Majestad. Ha llegado el momento de revelarla. Pero, para evitar que el secreto caiga fácilmente en manos del enemigo, se ha utilizado un proceso profundamente pensado para compartirlo.

## Descripción del Problema

Primero, cada uno de los nueve agentes de doble cero (de 001 a 009) lleva una **parte distinta** del secreto. Además, existe un umbral **k** (1 < k < 9) tal que al menos **k partes** del secreto son necesarias para revelarlo. Esto permite recuperar el secreto incluso si algunos agentes están fuera de acción. Finalmente, el conocimiento de menos de **k partes** no permite obtener ninguna información sobre el secreto (pueden existir sesgos estadísticos en algunos casos, pero en general no los hay). El enemigo debe capturar o contratar al menos **k agentes** para aprender algo.

Tu tarea es averiguar cómo revelar el secreto dados al menos **k** partes.

## Proceso de Compartición del Secreto

El secreto S se escribe utilizando el siguiente alfabeto de 53 caracteres:

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_

markdown
Copiar
Editar

Cada carácter está identificado por su índice de 0 a 52: a=0, b=1, ..., _=52.

Dado un umbral **k ≥ 2**, el proceso de compartición del secreto es el siguiente:

1. Para cada índice **i** de **S**, se define un polinomio:

P[i] = A[i,k-1]⋅X^(k-1) + A[i,k-2]⋅X^(k-2) + ... + A[i,1]⋅X + S[i]

css
Copiar
Editar

Donde los coeficientes **A[..]** se eligen aleatoriamente entre 0 y 52 (inclusive) con la restricción adicional de que **A[i,k-1] > 0**.

2. Cada agente 00x recibe la cadena que representa los valores:

[P0%53, P1%53, ...]

css
Copiar
Editar

Esta es su parte del secreto, mientras que el secreto en sí es la cadena representada por:

..]`

Ejemplo
Considera k = 2 y S = "SIS" = [44, 34, 44].

Para cada carácter, se elige un polinomio aleatorio de grado 1 con el coeficiente constante correspondiente:

ini
Copiar
Editar
P0 = 41X + 44
P1 = 8X + 34
P2 = 2X + 44
El Agente 001 recibe:

perl
Copiar
Editar
[P0(1)%53, P1(1)%53, P2(1)%53] = [32, 42, 46] = GQU
El Agente 002 recibe:

perl
Copiar
Editar
[P0(2)%53, P1(2)%53, P2(2)%53] = [20, 50, 48] = uYW
Tareas
La tarea principal consiste en averiguar cómo revelar el secreto a partir de al menos k partes del mismo.

Este es el resumen y la descripción del proceso de compartición del secreto. Utiliza las partes proporcionadas por los agentes para revelar el secreto final.



Este es el archivo **.md** con la traducción al español y la explicación detallada del problema. Puedes copiarlo directamente en tu `README.md`. Si necesitas más detalles o modificaciones, avísame.
