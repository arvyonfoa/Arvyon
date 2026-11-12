---
tipo: concepto
area: transversal
estado: borrador
confianza: media
resumen: "El arnés es todo lo que rodea al modelo en un agente (instrucciones, memoria, herramientas, permisos y comprobaciones); diseñarlo bien es el harness engineering."
fuentes: ["[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]", "[[2026-10-youtube-eric-risco-software-factory]]"]
creado: 2026-11-11
actualizado: 2026-11-12
revisar_antes: 2027-11-11
etiquetas: [fase-1, agentes]
---

# Arnés de agentes (harness) e ingeniería del arnés

## Definición
El **arnés** (*harness*) es todo lo que hay en un agente de IA salvo el modelo: las instrucciones que recibe, la memoria, las herramientas que puede usar, los permisos y las comprobaciones que revisan su trabajo. La fórmula que circula es **agente = modelo + arnés** ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]). Si el modelo es el motor, el arnés es el resto del coche: volante, frenos, tablero y cinturón.

La **ingeniería del arnés** (*harness engineering*) es el oficio de diseñar ese entorno para que el agente acierte a la primera y para que sus errores se corrijan antes de llegar a una persona. El término se popularizó en febrero de 2026 con un artículo de OpenAI y lo ordenó Birgitta Böckeler (Thoughtworks) en abril de 2026.

### Guías y sensores
| | Cuándo actúa | Qué hace | Ejemplos |
|---|---|---|---|
| **Guía** | Antes de que el agente actúe | Orienta: sube la probabilidad de acertar | Archivo de instrucciones, especificación de la tarea, memoria, plantillas |
| **Sensor** | Después de que el agente actúa | Detecta: permite corregir antes de entregar | Pruebas, reglas automáticas, revisión con otra IA, aprobación humana |

### Computacional o inferencial
| | Quién lo ejecuta | Rasgos |
|---|---|---|
| **Computacional** | Un programa | Rápido, barato y da siempre lo mismo |
| **Inferencial** | Una IA | Entiende el significado, pero es más lento, más caro y variable |

Cuando un error se repite, la persona mejora una guía o añade un sensor. El objetivo no es quitar a la persona sino llevar su atención a donde más importa.

> [!note] Hecho
> Böckeler reconoce lo que aún no está resuelto: comprobar el **comportamiento** (que el resultado hace lo que el negocio necesita) es «el elefante en la habitación», y no existe todavía una forma de medir si un arnés es bueno ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

## Por qué importa
- Explica por qué dos empresas con el mismo modelo obtienen resultados distintos. La diferencia está en el arnés, y eso es lo que diseña un consultor.
- Un buen arnés permite usar un modelo más barato ([[enrutamiento-de-modelos]]).
- Es la respuesta ordenada al miedo «¿y si la IA se equivoca?»: con qué guías se reduce el error y con qué sensores se detecta ([[objeciones]]).

> [!note] Hecho · el arnés también cuesta
> Naresh Jain midió en octubre de 2026 una misma tarea con y sin arnés. Con un modelo potente (Sol), el arnés gastó unas 10,5 veces más *tokens*, tardó casi 3 veces más y costó unas 7 veces más (2,68 frente a 0,41 USD), con el mismo resultado: 10 de 10 aceptadas. Con un modelo barato (Luna), subió las aceptadas de 3 a 10 de 10 y aun así costó 0,27 USD, un 33 % menos que Sol sin arnés. Universo: 10 ejecuciones de un único servicio en Java, 2026 ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

## Cómo lo aplicamos en Arvyon
**Este cerebro ya es un arnés** para un agente de conocimiento:

| Pieza del cerebro | Qué es en este vocabulario |
|---|---|
| `AGENTS.md` y `PROMPT-MAESTRO.md` | Guías (instrucciones y reglas); valen para cualquier agente ([[opencode]], Claude Code) |
| `index.md`, `log.md` y la wiki | Memoria, el *brain* del video |
| `herramientas/revisar_wiki.py` | Sensor computacional: siempre revisa lo mismo |
| Los recuadros «Por verificar» y «Contradicción» | Sensor inferencial: el agente juzga su propia evidencia |
| El fundador uniendo cada *pull request* | Puerta humana |
| El flujo de ingesta en 12 pasos | Línea de una [[fabrica-de-ia]] |

- **Con clientes (Fase 2):** todo asistente o automatización se entrega con sus guías (instrucciones, base de conocimiento) y sus sensores (comprobaciones, registro, traspaso a un humano) ([[proceso-de-entrega]]).
- **En el estudio:** el concepto entra en la semana 2, junto a [[prompting-para-empresas]]: escribir buenas instrucciones es construir guías.
- **Lo que no hacemos por ahora:** construir arneses para agentes de programación. Es trabajo de programadores ([[pi-coding-agent]]).

## Ejemplos
- **En el video de Eric Risco:** el *brain* y la especificación son guías; los cuatro revisores y el aprobador son sensores inferenciales. Le faltan sensores computacionales ([[evaluacion-video-software-factory]]).
- **En Stripe:** más de tres millones de pruebas y un tope de dos rondas de comprobación son sensores computacionales.
- **En un asistente de WhatsApp de una pyme ficticia:** guías = tono, preguntas frecuentes y lista de precios; sensores = una regla que impide enviar precios que no estén en la lista y el traspaso a una persona.

## Conexiones
- [[fabrica-de-ia]]: la fábrica es el proceso; el arnés es lo que hace fiable a cada agente dentro de ella.
- [[enrutamiento-de-modelos]]: arnés y elección de modelo se compensan.
- [[pi-coding-agent]]: una herramienta para construir un arnés propio.
- [[prompting-para-empresas]]: las instrucciones son la primera guía.
- [[rag-y-agentes]]: el bloque del currículo donde se estudia.
- [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]: las fuentes.
