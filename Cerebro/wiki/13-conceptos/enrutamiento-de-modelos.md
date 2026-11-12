---
tipo: concepto
area: transversal
estado: borrador
confianza: media
resumen: "Enviar cada tarea al modelo y al nivel de razonamiento más baratos que la resuelven bien; es parte de FinOps para IA, la gestión del gasto en IA."
fuentes: ["[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]", "[[2026-10-youtube-eric-risco-software-factory]]"]
creado: 2026-11-11
actualizado: 2026-11-11
revisar_antes: 2027-05-11
etiquetas: [fase-1, costos]
---

# Enrutamiento de modelos y FinOps para IA

## Definición
El **enrutamiento de modelos** (*model routing* o *LLM routing*) consiste en enviar cada petición al modelo más barato que la resuelve bien, y en dar a cada tarea solo el nivel de razonamiento que necesita. La disciplina más amplia que lo contiene es **FinOps para IA**: la gestión financiera del gasto en IA (ver cuánto se gasta, repartirlo por área y optimizarlo).

| Nombre que se oye | Qué es |
|---|---|
| Enrutamiento de modelos | La técnica: cada petición va al modelo adecuado |
| Cascada de modelos | Probar primero el modelo barato y subir al caro solo si la respuesta no pasa una comprobación |
| FinOps para IA | La gestión financiera del gasto en IA |
| Pasarela de IA (*AI gateway*) | El programa intermedio por donde pasan todas las llamadas; ahí se aplican rutas, topes de gasto y registro |
| LLMOps | La operación de aplicaciones con modelos de lenguaje; el enrutamiento es una parte |
| Nivel de razonamiento | El ajuste que indica al modelo cuánto «pensar» antes de responder |

## Por qué importa
Toda empresa pregunta cuánto cuesta. Esta es la respuesta ordenada.

> [!note] Hecho · las palancas, según la FinOps Foundation (actualizado el 2026-10-28)
> | Palanca | Ahorro indicativo |
> |---|---|
> | Elegir bien el modelo y enrutar | 60–90 % |
> | Caché de instrucciones (lo que se repite en cada llamada) | 50–90 % de lo repetido |
> | Proceso por lotes (lo que no es urgente) | cerca del 50 % |
> | Gestión del contexto (enviar solo lo necesario) | 20–60 % |
> | Limitar la longitud de la respuesta | 10–40 % |
>
> Un modelo puntero puede costar de 50 a 100 veces más por *token* que el más pequeño, y el texto que el modelo escribe suele costar de 3 a 5 veces más que el que lee. La propia guía presenta las cifras como indicativas y pide validarlas con datos propios ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

> [!note] Hecho · la métrica que importa
> La guía recomienda medir el **costo por resultado exitoso**: lo que cuesta todo el proceso, contando solo los casos que superan el umbral de calidad. Los intentos fallidos también se pagan. Un modelo barato que falla la mitad de las veces puede salir más caro que uno bueno.

Lo que hay que saber antes de prometer ahorros:
- **Sin pruebas no hay enrutamiento.** Para saber qué modelo «resuelve bien» una tarea hace falta un conjunto de casos de ejemplo con su respuesta correcta (evaluaciones) ([[medicion-de-roi]]).
- **Las cifras grandes son de laboratorio.** RouteLLM (2024) y FrugalGPT (2023) reportan ahorros muy altos en bancos de prueba; el resultado real depende de cuántas peticiones fáciles tenga cada empresa.
- **Existe la ruta inversa.** Anthropic ofrece una «estrategia del asesor»: un modelo económico hace el trabajo y consulta a uno potente solo cuando se atasca. Si consulta mucho, el ahorro desaparece.
- **Un buen arnés permite un modelo más barato** ([[arnes-de-agentes]]).

> [!tip] Supuesto
> En una pyme, el modelo no suele ser el costo mayor: pesan más las horas de montaje, el mantenimiento y el tiempo de las personas que revisan. Se valida con los números de las demos de las semanas 3 y 4 ([[estructura-de-costos]]).

## Cómo lo aplicamos en Arvyon
**Las cinco preguntas del consultor** (para propuestas y para el informe de resultados):
1. ¿Qué tareas hará la IA y cuántas veces al mes?
2. ¿Cuál es el modelo más barato que pasa la prueba en cada tarea?
3. ¿Qué parte de cada llamada se repite y se puede guardar en caché?
4. ¿Qué puede esperar y procesarse por lotes?
5. ¿Cuánto cuesta cada resultado correcto, comparado con hacerlo a mano?

Dónde se estudia: semana 2 ([[herramientas-para-pymes]], por qué hay modelos pequeños, medios y grandes) y semana 5 ([[medicion-de-roi]], costo por resultado exitoso).

## Ejemplos
> [!tip] Supuesto · reparto de tareas por nivel
> | Nivel | Tareas típicas en una pyme |
> |---|---|
> | Modelo pequeño, razonamiento bajo | Clasificar mensajes, extraer datos de una factura, preguntas frecuentes |
> | Modelo medio | Redactar cotizaciones y correos, resumir reuniones, atender conversaciones |
> | Modelo grande, razonamiento alto | Casos difíciles, dinero, contratos, quejas delicadas |
>
> Es una propuesta del agente, no una norma. Se valida con casos de prueba en cada proyecto.

- **En el video de Eric Risco:** el modelo más capaz construye y uno menor revisa el código. Es enrutamiento aplicado sin nombrarlo ([[2026-10-youtube-eric-risco-software-factory]], min 09:57).
- **Experimento de Jain:** un modelo barato con arnés resolvió 10 de 10 casos y costó un 33 % menos que el modelo potente sin arnés ([[arnes-de-agentes]]).

> [!question] Por verificar
> Precios vigentes por modelo y por nivel de razonamiento de los principales proveedores. No se recogieron: cambian cada pocas semanas y deben consultarse al preparar cada propuesta ([[lagunas]]).

## Conexiones
- [[medicion-de-roi]]: el costo de la IA entra en el cálculo del retorno.
- [[arnes-de-agentes]]: arnés y modelo se compensan.
- [[fabrica-de-ia]]: cada paso de agente de una fábrica tiene su modelo.
- [[herramientas-para-pymes]]: los planes y modelos entre los que se elige.
- [[estructura-de-costos]]: el costo de la IA en los proyectos de Arvyon.
- [[fundamentos-llm]]: qué es un *token* y por qué se cobra por él.
- [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]: las fuentes.
