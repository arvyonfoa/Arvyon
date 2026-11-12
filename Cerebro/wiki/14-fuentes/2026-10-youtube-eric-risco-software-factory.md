---
tipo: fuente
area: conocimiento
estado: borrador
confianza: media
resumen: "Video de Eric Risco (17 min): qué es una fábrica de IA, cómo monta la suya con especificación, constructor, cuatro revisores, aprobador y puerta humana, y su fábrica de contenido."
fuentes: []
creado: 2026-11-11
actualizado: 2026-11-11
revisar_antes: 2027-02-11
etiquetas: [fase-1, video, agentes]
---

# Video: «Programar con agentes ya no basta: monta tu Software Factory» (Eric Risco)

## Ficha
| Campo | Valor |
|---|---|
| Autor / institución | [[eric-risco]], canal «Eric Risco \| Inteligencia Artificial» |
| Medio | YouTube |
| Fecha de publicación | 2026-10-23 |
| URL | https://www.youtube.com/watch?v=p6nnqerea7w |
| Archivo en raw/ | [[2026-10-23-eric-risco-software-factory]] (`raw/transcripciones/`) |
| Tipo | video |
| Idioma | español (España) |
| Duración | 17 min 21 s, 10 capítulos |
| Fiabilidad (1–5) | 3 — motivo: practicante con experiencia real, pero con interés comercial (promociona su proyecto), sin cifras propias y con un solo caso |
| Universo / muestra | Un caso: su propia aplicación, que «va a lanzar muy pronto» |

> [!note] Hecho
> La transcripción es la de los subtítulos automáticos de YouTube y tiene errores («Cloud Code» es Claude Code, «Sonet» es Sonnet). El agente no vio la imagen del video: el diagrama se reconstruyó con lo que el autor dice y con un repositorio de un tercero ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

## Resumen en 5 líneas
1. Chatear con un agente de programación convierte a la persona en el cuello de botella; la salida es una **fábrica**: el trabajo entra por un lado y sale por otro sin que estés en medio.
2. Una fábrica de IA es «cualquier proceso que sea repetible y auditable con inteligencia artificial dentro», hecho de tres tipos de pasos: código, agente y aprobación humana ([[fabrica-de-ia]]).
3. Necesita una memoria persistente, el *brain*, que el agente consulta antes de actuar.
4. Su fábrica de software: entrada → especificación → constructor → cuatro revisores con modelos distintos → aprobador → agente que decide si hace falta un humano → producción.
5. El mismo patrón edita sus videos (fábrica de contenido) y, según él, sirve para cualquier proceso que se repita.

## Ideas clave
1. El cuello de botella es la persona que chatea, aunque abra cuatro ventanas (min 00:00).
2. Errores de producción, pruebas y desarrollos pequeños ya se pueden delegar (min 01:06).
3. Definición de fábrica de IA y analogía de la fábrica de coches: cada máquina recibe algo, entrega algo y su resultado se puede revisar, porque un error se arrastra a las siguientes (min 01:38).
4. A cada paso hay que darle cuatro cosas: qué hace, cómo lo hace, cuál es el resultado y cómo se revisa (min 02:46).
5. Dos condiciones: proceso repetible y auditable, es decir, cada paso deja rastro (min 03:18 a 03:52).
6. El *brain*: sin memoria continua, el agente olvida decisiones (ejemplo de PostgreSQL y MySQL) (min 04:00 a 05:30).
7. Entrada única para errores de Sentry, *issues* de GitHub y tareas propias; el redactor de la especificación (Opus) consulta el *brain* antes de escribir (min 06:38 a 07:12).
8. El constructor (Opus) crea una rama y programa con la prueba primero (TDD) (min 07:12 a 08:17).
9. Cuatro revisores con contexto limpio: seguridad (Sol), experiencia de uso (Sol), interfaz (Astra) y código (Sonnet). Usa otros modelos porque Opus «se sesgaría» (min 08:17 a 10:14).
10. El aprobador (Opus) reúne los veredictos y devuelve el trabajo al constructor hasta que los cuatro pasan (min 10:14).
11. Un agente decide si el cambio es lo bastante grande para pedir un humano; reconoce que hace falta código que bloquee, no solo un agente (min 11:06 a 12:32).
12. Las tareas corren en paralelo, cada una con su identificador y su rama (min 12:32).
13. Marketing y ventas podrían pedir cambios por Slack, incluido «algo en el aviso legal» (min 13:17).
14. Fábrica de contenido: recorta silencios y errores, añade animaciones y transiciones, une y crea miniaturas; él sube el video a mano (min 13:51 a 15:32).
15. Regla: «si es algo que haces más de una vez a la semana, tiene todo el sentido» (min 15:32).

## Datos y cifras
| Dato | Valor | Universo y año | Página o minuto |
|---|---|---|---|
| Alcance del video | 424.685 vistas y 8.167 «me gusta» | 19 días después de publicarse, 2026-11-11 | metadatos |
| OpenAI: solución sin código escrito a mano | «más de un millón de líneas» | un equipo de OpenAI; lo cita sin fecha | min 15:32 |
| Stripe: cambios hechos por agentes | «más de 1.000 PR en una semana» | Stripe; lo cita sin fecha | min 16:05 |
| Modelos por puesto | Opus (especificación, constructor, aprobador), Sol (seguridad y UX), Astra (UI), Sonnet (código) | su fábrica, 2026-10 | min 06:38 a 10:14 |

Las dos cifras de terceros están contrastadas en [[evaluacion-video-software-factory]].

## Qué cambia en la wiki
- [[fabrica-de-ia]], [[arnes-de-agentes]] y [[enrutamiento-de-modelos]]: conceptos nuevos.
- [[evaluacion-video-software-factory]]: análisis crítico del video.
- [[eric-risco]]: entidad nueva (canal de referencia).
- [[youtube]]: primeras lecciones de formato.
- [[automatizacion-de-procesos]], [[rag-y-agentes]], [[contenido-y-marca-personal]] y [[curriculo]]: dónde encaja lo aprendido.
- [[tendencias]]: fila nueva sobre fábricas de IA.

## Contradicciones con la wiki
No contradice ninguna página. Las incoherencias internas del video (el constructor lanza a sus revisores, el aprobador es el mismo modelo que construyó, el aviso legal como tarea pequeña) están en [[evaluacion-video-software-factory]].

## Citas textuales útiles
> «El cuello de botella eres tú.» (min 00:00)

> «Una AI Factory al final es cualquier proceso que sea repetible y auditable con inteligencia artificial dentro.» (min 01:38)

> «Para hacer esto no basta solo con un agente de inteligencia artificial. Aquí hay que meter hooks o hay que meter código para bloquear.» (min 11:39)

> «Si son procesos revisables y auditables puedes crear un AI factory.» (min 15:32)

## Lecciones de formato
- **Gancho:** empieza con un dolor y no con una presentación: «Programar con agentes […] ya no basta» y «el cuello de botella eres tú», en los primeros 30 segundos.
- **Estructura:** problema → analogía sencilla (fábrica de coches) → piezas del concepto → caso propio paso a paso con un diagrama que se va completando → giro para ampliar el público («sirve a quien no programa») → segundo caso (contenido) → prueba social (OpenAI y Stripe) → anuncio.
- **Duración:** 17 min 21 s, con 10 capítulos marcados en la descripción.
- **Llamada a la acción:** ligada al siguiente video y a un producto futuro: pide comentarios para publicar RSC Factory.
- **Descripción:** resumen de dos párrafos, capítulos con minutos, enlaces al video anterior y al repositorio, y etiquetas.
- **Comentarios de la audiencia:** no se capturaron (laguna abierta en [[lagunas]]).

## Preguntas que abre
- [ ] ¿Qué piden los comentarios del video? Son señales de demanda ([[senales-de-demanda]]).
- [ ] ¿Se publicó RSC Factory? No estaba público el 2026-11-11.
- [ ] ¿Qué porcentaje de mejora atribuye a la memoria en el minuto 04:24? El subtítulo no lo recoge.
- [ ] ¿Cuánto cuesta una tarea completa en su fábrica?

## Conexiones
- [[evaluacion-video-software-factory]]: qué está bien, qué exagera y qué le faltó.
- [[fabrica-de-ia]]: el concepto central del video.
- [[arnes-de-agentes]]: el *brain* y los revisores son piezas de un arnés.
- [[enrutamiento-de-modelos]]: el reparto de modelos por puesto.
- [[eric-risco]]: el autor y su canal.
- [[youtube]]: las lecciones de formato.
- [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]: las fuentes con que se contrastó.
