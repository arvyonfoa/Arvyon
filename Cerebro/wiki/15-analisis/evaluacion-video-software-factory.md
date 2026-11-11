---
tipo: analisis
area: conocimiento
estado: borrador
confianza: media
resumen: "Evaluación del video de Eric Risco sobre fábricas de software: buen mapa con relato optimista; aciertos, exageraciones, cinco incoherencias, doce piezas que faltan y ocho temas nuevos para el estudio."
fuentes: ["[[2026-10-youtube-eric-risco-software-factory]]", "[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]"]
creado: 2026-11-11
actualizado: 2026-11-11
revisar_antes: 2027-02-11
etiquetas: [fase-1, agentes]
---

# ¿Me sirven las fábricas de IA, el harness engineering con Pi y el enrutamiento de modelos?

## Pregunta
El fundador vio el video «Programar con agentes ya no basta: monta tu Software Factory» y preguntó: ¿aportan a mi aprendizaje la fábrica de software, la fábrica de contenido, el *harness engineering* basado en Pi y la disciplina que elige modelo y razonamiento para ahorrar? ¿Qué plantea el video, qué tiene mal y qué le faltó? ¿Qué más debería saber?

## Respuesta corta
Los cuatro temas valen la pena como **conceptos** y son en el fondo el mismo: cómo organizar el trabajo de una IA para que sea repetible, comprobable y barato. Ninguno pide construir nada ni programar antes del 15 de diciembre.

| Tema | ¿Aporta? | ¿Cuándo? |
|---|---|---|
| [[fabrica-de-ia]] (software) | Sí, el concepto: es el patrón que se diseñará para una pyme. No, el proyecto: una fábrica de código exige programar | Idea ya; práctica en las semanas 3 y 4 |
| Fábrica de contenido | Sí, para el canal de YouTube; solo cubre la posproducción | Fase 2 |
| [[arnes-de-agentes]] y [[pi-coding-agent]] | El concepto sí (este cerebro ya es un arnés). Pi es para programadores | Concepto en la semana 2; Pi, opcional después |
| [[enrutamiento-de-modelos]] | Sí: es la respuesta ordenada a «¿cuánto cuesta?» | Semanas 2 y 5 |

**Veredicto sobre el video:** buen mapa con un relato optimista. La estructura es correcta y coincide con lo que publican Stripe, OpenAI y Thoughtworks. No cuenta lo que hace que una fábrica funcione: costo, defensa de la entrada, comprobaciones automáticas, tope de vueltas y datos que demuestren que funciona.

## Desarrollo

### 1. Lo que el video plantea bien
- **Los tres tipos de pasos** (código, agente, humano). Coincide con Stripe, que intercala bucles de agente con código determinista ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).
- **La especificación como contrato:** el constructor ejecuta un documento que ya dice qué se acepta.
- **La memoria:** OpenAI llegó a lo mismo, con un archivo corto de instrucciones como mapa y la documentación como fuente única de verdad.
- **Revisar con un modelo distinto:** un estudio de NeurIPS 2024 mostró que los modelos reconocen sus propios textos y los puntúan mejor.
- **Un agente no basta para la puerta de riesgo:** lo dice el propio autor (min 11:39).
- **Cada puesto paga el modelo que necesita:** es [[enrutamiento-de-modelos]] sin nombrarlo.

### 2. Afirmaciones contrastadas
| Lo que dice el video | Veredicto | Evidencia |
|---|---|---|
| «En Estados Unidos, toda la ingeniería de software ya ha pasado al siguiente nivel» (min 00:00) | Exagerado | Los casos publicados son de equipos de vanguardia. DORA 2025: la IA sube la velocidad de entrega y también la inestabilidad. METR 2025: desarrolladores expertos tardaron un 19 % más con IA; la actualización de 2026 no fue concluyente |
| Ingenieros de OpenAI crearon más de un millón de líneas sin escribir ninguna a mano (min 15:32) | Cierto, con matices | Artículo de OpenAI de febrero de 2026: cinco meses, una beta interna. No fue «el otro día» |
| Stripe hizo más de 1.000 PR en una semana con agentes (min 16:05) | Cierto, con un matiz clave | Los escriben agentes, pero **los revisan personas**; se apoyan en más de 3 millones de pruebas, máquinas aisladas y un máximo de 2 rondas |
| Sol es de OpenAI y Astra está muy enfocado al uso del computador (min 08:50 y 09:24) | Cierto en lo esencial | OpenAI presenta a Astra como su modelo más capaz en uso del computador. Que esté «entrenado con refuerzo para revisar la interfaz» no se pudo confirmar |
| Otro modelo evita el sesgo del constructor (min 08:50) | Plausible | El estudio midió el sesgo en resúmenes de texto, no en código |
| «Cualquier error […] se soluciona solo» (min 12:44) | Anécdota | No da cifras, y el software «lo voy a lanzar muy pronto» |
| «Puedes sacar el trabajo de todo un equipo» (min 16:05) | Sin respaldo | No hay datos propios |
| «Si es algo que haces más de una vez a la semana, tiene todo el sentido» (min 15:32) | Regla incompleta | Falta comparar el costo de montar y mantener con el ahorro. Anthropic recomienda empezar por la solución más simple |
| Llevar aplicaciones a producción «sin saber programar» (min 00:33) | Riesgoso | La puerta humana solo protege si la persona puede juzgar lo que aprueba |
| Opus «edita» los videos (min 13:51) | Impreciso | El modelo razona y da órdenes a programas de edición |

> [!question] Por verificar
> Según resúmenes del artículo de OpenAI, el equipo creció de tres a siete ingenieros durante el experimento y abrió unos 1.500 cambios. No se pudo leer el original ([[lagunas]]).

### 3. Errores e incoherencias internas
1. **El constructor lanza a sus propios revisores** (min 08:17). Quien es revisado no debería controlar su revisión; debería lanzarlos un paso de código.
2. **El aprobador es el mismo modelo que construyó** (min 10:14). El sesgo que quiso evitar con Sol y Astra vuelve a entrar en el último paso.
3. **La revisión de código «no me preocupa mucho»** (min 09:57). La entrega a Sonnet, de la misma casa que Opus y de menor capacidad; contradice su argumento de las familias distintas.
4. **El aviso legal como tarea pequeña** (min 13:17). Su agente mide el riesgo por lo que el cambio toca en el sistema. Un texto legal es pequeño en código y grande en consecuencias: el tamaño de un cambio no es su riesgo.
5. **Lapsus menores:** dice dos veces que la experiencia de uso la revisa Sol; dice «pasa directamente a la PR y se sube directamente a main»; llama «audio en bruto» a la grabación de video; y usa «AI Factory» en un sentido distinto del de Nvidia.

### 4. Lo que le faltó
Las doce piezas están en [[fabrica-de-ia]]. Las de más peso:
- **Comprobaciones que no dependan de una IA.** Los cuatro revisores son sensores inferenciales; faltan los computacionales ([[arnes-de-agentes]]).
- **Tope de vueltas y de gasto.** El bucle «hasta que el aprobador decida» no tiene límite.
- **Defensa de la entrada.** En febrero de 2026, el título de un *issue* de GitHub manipuló al robot de clasificación del proyecto Cline y acabó en una versión no autorizada instalada en unas 4.000 máquinas.
- **El costo.** No se menciona en 17 minutos.

> [!abstract] Estimación · llamadas a modelos por tarea
> Una pasada limpia son 8 llamadas: especificación (1) + construcción (1) + revisores (4) + aprobador (1) + agente de riesgo (1). Cada rechazo añade al menos 6 (construcción, 4 revisores, aprobador). Con dos rechazos: 8 + 2 × 6 = **20 llamadas**. No se puede pasar a dinero sin precios ni tamaños reales.

**Cuatro fábricas reales, comparadas** ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]):

| | OpenAI (feb 2026) | Stripe (feb 2026) | StrongDM (feb 2026) | Video (oct 2026) |
|---|---|---|---|---|
| ¿Quién escribe? | Agentes | Agentes | Agentes | Agentes |
| ¿Quién revisa? | Agentes y personas | Personas, siempre | Nadie lee el código | Cuatro agentes; persona solo en cambios grandes |
| ¿En qué se apoya? | Documentación como fuente de verdad y reglas automáticas | Más de 3 millones de pruebas, máquinas aisladas, tope de 2 rondas | Escenarios fuera del código y copias de los servicios externos | Memoria, prueba primero y revisores con otros modelos |
| Escala publicada | Cerca de 1 millón de líneas en 5 meses | Más de 1.000 cambios por semana | Equipo de 3 personas | Ninguna cifra |

### 5. La fábrica de contenido
El video le dedica dos minutos (min 13:51 a 15:49): grabación en bruto → recorte de silencios y errores → animaciones → transiciones y unión → miniaturas → revisión humana → subida manual.
- **Cómo funciona de verdad:** el modelo hace de director. Lee la transcripción con tiempos y da órdenes a programas (transcripción, corte con FFmpeg, animaciones con Remotion).
- **Lo que no cuenta:** el gusto se entrena (la guía de estilo es la memoria de esa fábrica); solo cubre la posproducción; un corte automático puede cambiar el sentido; no habla de costo ni de derechos.
- **YouTube** no prohíbe el contenido hecho con IA; su política de «contenido no auténtico» retira la monetización a lo repetitivo o producido en masa (por verificar en la página oficial).
- **Para Arvyon:** una persona real que explica, con edición asistida, está en el lado seguro. Empezar en la Fase 2 por lo barato: silencios, subtítulos, descripción y capítulos ([[contenido-y-marca-personal]]).

### 6. Ocho temas que no estaban en la lista
| # | Tema | Qué es | Dónde encaja |
|---|---|---|---|
| 1 | Evaluaciones | Pruebas para una IA: una entrada, una salida y una regla para calificar. Sin ellas no se puede elegir modelo ni demostrar resultados | [[medicion-de-roi]] · semana 5 |
| 2 | Seguridad de agentes | Inyección de instrucciones y «tríada letal»: datos privados, contenido no confiable y un canal de salida | [[gobernanza-y-regulacion]] · semanas 2 y 5 |
| 3 | Flujo o agente | En un flujo el camino lo fija el código; en un agente, el modelo. La mayoría de los casos de una pyme son flujos | [[automatizacion-de-procesos]] · semana 3 |
| 4 | Ingeniería de contexto | Decidir qué información llega al modelo en cada momento | [[prompting-para-empresas]] · semana 2 |
| 5 | Supervisión humana bien diseñada | Qué aprueba una persona, por qué canal y con qué información; n8n ya lo permite | [[ia-en-whatsapp-y-atencion]] · semana 4 |
| 6 | Escribir especificaciones | El encargo bien escrito: qué se quiere, cómo se acepta y cómo se comprueba | [[habilidades-de-consultoria]] · semana 5 |
| 7 | Registro y trazabilidad | Que cada paso deje rastro: qué entró, qué salió, qué modelo, cuánto costó | [[datos-y-reportes]] · semana 4 |
| 8 | Conectores y habilidades (MCP y *Skills*) | Cómo un agente se conecta a herramientas y aprende procedimientos | [[rag-y-agentes]] · Fase 2 |

### 7. Lo que no se recomienda ahora
- Montar una fábrica de software ni instalar RSC Harness o Pi.
- Esperar a RSC Factory: no estaba publicado el 2026-11-11.
- Cambiar el calendario de la Fase 1: las ideas entran en bloques que ya están en el [[curriculo]].

### 8. Tres ejercicios con empresas ficticias
1. **Dibuja una fábrica.** Elige un proceso de una empresa inventada y llena una tabla de pasos como la de [[fabrica-de-ia]].
2. **Encuentra el riesgo escondido.** Señala un cambio pequeño de alto riesgo y escribe la regla que lo manda a una persona.
3. **Reparte los modelos.** Asigna a cada paso de agente un nivel (pequeño, medio o grande) y explica por qué.

## Método o cálculo
1. Se descargaron los subtítulos automáticos del video y se leyeron completos.
2. Cada afirmación verificable se contrastó con fuentes primarias cuando fue posible.
3. Se investigaron Pi, el *harness engineering* y el enrutamiento de modelos en sus fuentes de origen.
4. El informe completo, con diagramas y glosario, se entregó al fundador en PDF antes de la ingesta: `raw/informes/2026-11-11-informe-fabricas-de-ia-arneses-enrutamiento.pdf`.

Límites: no se vio la imagen del video; no se pudo abrir la página original de OpenAI; varias cifras llegan por fuentes secundarias; no se probó ninguna herramienta.

## Fuentes
- [[2026-10-youtube-eric-risco-software-factory]]
- [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]

## Vigencia
Válido hasta: 2027-02-11 — se invalida si: se publica RSC Factory con datos de uso, cambian las políticas citadas (YouTube, Anthropic) o aparecen mediciones mejores del costo de los arneses.

## Conexiones
- [[fabrica-de-ia]]: el concepto y las doce piezas.
- [[arnes-de-agentes]]: guías y sensores.
- [[enrutamiento-de-modelos]]: la disciplina de costos.
- [[pi-coding-agent]]: la herramienta por la que preguntó el fundador.
- [[eric-risco]]: el autor del video.
- [[curriculo]]: dónde entra cada idea en la Fase 1.
- [[programacion-y-bases-de-datos]]: el análisis anterior sobre qué no estudiar todavía.
