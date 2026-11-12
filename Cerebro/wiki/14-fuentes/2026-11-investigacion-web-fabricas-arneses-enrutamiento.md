---
tipo: fuente
area: conocimiento
estado: borrador
confianza: media
resumen: "Investigación web (2026-11-11) sobre fábricas de software con agentes (Stripe, StrongDM, OpenAI), harness engineering (Thoughtworks), Pi, enrutamiento de modelos (FinOps Foundation, Anthropic) y seguridad de agentes."
fuentes: []
creado: 2026-11-11
actualizado: 2026-11-11
revisar_antes: 2027-02-11
etiquetas: [fase-1, agentes]
---

# Investigación web: fábricas de IA, arneses, Pi y enrutamiento de modelos

## Ficha
| Campo | Valor |
|---|---|
| Autor / institución | Investigación del agente (fuentes primarias de empresas, artículos técnicos, dos artículos académicos y prensa) |
| Medio | Web |
| Fecha de captura | 2026-11-11 |
| Archivo en raw/ | [[2026-11-11-investigacion-web-fabricas-arneses-enrutamiento]] (`raw/articulos/`) |
| Tipo | investigación web agrupada |
| Idioma | inglés y español |
| Fiabilidad (1–5) | Ver la tabla por fuente |

## Fuentes y fiabilidad
| Fuente | Fecha | Fiab. | Motivo |
|---|---|---|---|
| Stripe, «Minions» | 2026-02-09 | 4 | Primaria, con cifras propias y límites reconocidos |
| StrongDM, «Software Factory» | 2026-02-06 | 3 | Primaria, pero es un manifiesto |
| OpenAI, «Harness engineering» (vía InfoQ) | 2026-02 | 3 | No se pudo leer el original |
| B. Böckeler, «Harness engineering» (martinfowler.com) | 2026-04-02 | 4 | Análisis independiente de Thoughtworks |
| N. Jain, «Are Harnesses Worth the Cost?» | 2026-10-13 | 4 | Experimento con datos y límites declarados |
| FinOps Foundation, costos de tokens | 2026-10-28 | 4 | Organización sectorial; cifras indicativas |
| Anthropic, «Building effective agents» | 2024-12-19 | 4 | Primaria; proveedor de IA (máximo 4) |
| Sitio de Pi y blog de Mario Zechner | 2026-11-11; 2025-11-30 | 4 | Primarias sobre la herramienta |
| Fazt, tutorial de Pi | 2026-09-12 | 3 | Secundaria, en español |
| Panickssery y otros, NeurIPS 2024 | 2024 | 5 | Revisado por pares |
| METR, DORA, OWASP, RouteLLM, FrugalGPT | 2023–2026 | 4 | Fuentes sólidas, pero vistas a través de resúmenes |
| «Clinejection» (S. Willison, Snyk) | 2026-03 | 4 | Incidente documentado por varias fuentes |
| The Register, TechCrunch | 2026 | 3 | Prensa |
| Repositorios de terceros basados en el video | 2026-11 | 2 | Interpretaciones de aficionados |

## Resumen en 5 líneas
1. Las fábricas de software con agentes existen y publican resultados: **Stripe** integra más de mil cambios por semana escritos por agentes y revisados por personas; **StrongDM** va al extremo de no leer el código; **OpenAI** construyó una beta interna de cerca de un millón de líneas en cinco meses.
2. Lo que las sostiene no son los agentes sino el entorno: pruebas, reglas automáticas, máquinas aisladas y topes de vueltas. A ese entorno se le llama **arnés** ([[arnes-de-agentes]]).
3. Un arnés también cuesta: con un modelo potente puede multiplicar por siete el costo sin mejorar el resultado, y con uno barato puede ser lo que lo hace funcionar (Jain).
4. Elegir modelo y nivel de razonamiento por tarea se llama **enrutamiento de modelos** y es parte de **FinOps para IA** ([[enrutamiento-de-modelos]]).
5. **Pi** es un agente de programación minimalista para construir un arnés propio; es una herramienta para programadores ([[pi-coding-agent]]).

## Datos y cifras
| Dato | Valor | Universo y año | Fuente |
|---|---|---|---|
| Cambios integrados por semana escritos por agentes | más de 1.000 | Stripe, febrero de 2026; revisados por personas | Stripe |
| Pruebas automáticas de Stripe | más de 3 millones | Stripe, 2026 | Stripe |
| Rondas de integración continua por tarea | máximo 2 | Stripe, 2026 | Stripe |
| Líneas de código sin escribir a mano | cerca de 1 millón en 5 meses | beta interna de OpenAI, 2025–2026 | OpenAI vía InfoQ |
| Gasto de referencia en tokens | 1.000 USD por ingeniero y día | aspiración de StrongDM, 2026 | StrongDM |
| Costo de un arnés con modelo potente | ~10,5× tokens, ~3× tiempo, ~7× costo; 10/10 con y sin arnés | 10 ejecuciones, un servicio en Java, GPT-6 Sol, 2026 | Jain |
| Efecto de un arnés con modelo barato | de 3/10 a 10/10 aceptadas; 33 % más barato que Sol sin arnés | 10 ejecuciones, GPT-6 Luna, 2026 | Jain |
| Ahorro por elegir modelo y enrutar | 60–90 % (indicativo) | guía de la FinOps Foundation, 2026 | FinOps Foundation |
| Ahorro por caché de instrucciones | 50–90 % de los tokens en caché (indicativo) | ídem | FinOps Foundation |
| Ahorro por lotes | cerca del 50 % (indicativo) | ídem | FinOps Foundation |
| Token de salida frente a token de entrada | 3 a 5 veces más caro | ídem | FinOps Foundation |
| Modelo puntero frente al más pequeño | 50 a 100 veces más caro por token | ídem | FinOps Foundation |
| Desarrolladores expertos con IA | 19 % más lentos | ensayo de METR, 2025; actualización de 2026 no concluyente | METR (vía resúmenes) |
| Máquinas afectadas por «Clinejection» | unas 4.000 | incidente de febrero de 2026 | Willison, Snyk |

## Qué cambia en la wiki
- [[evaluacion-video-software-factory]]: es la evidencia con la que se contrasta el video.
- [[fabrica-de-ia]], [[arnes-de-agentes]], [[enrutamiento-de-modelos]]: conceptos nuevos.
- [[pi-coding-agent]]: entidad nueva.
- [[rag-y-agentes]], [[gobernanza-y-regulacion]], [[medicion-de-roi]], [[automatizacion-de-procesos]]: temas nuevos por bloque.
- [[tendencias]] y [[glosario]]: filas y términos nuevos.

## Contradicciones
> [!warning] Contradicción · ¿Pi trae conectores MCP?
> El sitio oficial de Pi dice el 2026-11-11 que MCP viene integrado. El tutorial de Fazt (2026-09-12) y el artículo original de Mario Zechner (2025-11-30) dicen que no. Lo más probable es un cambio reciente del producto; manda el sitio oficial.

> [!warning] Contradicción · nombres de los modelos de OpenAI
> Las fuentes llaman al modelo «Sol» de formas distintas (GPT-6 Sol, GPT-6.1 Sol, GPT-5.6 Sol). No se resolvió; en la wiki se le llama solo «Sol».

## Preguntas que abre
- [ ] Cifras exactas del experimento de OpenAI (número de cambios y tamaño del equipo) en su artículo original.
- [ ] Texto vigente de las condiciones de Anthropic sobre el uso de suscripciones en herramientas de terceros.
- [ ] Texto vigente de la política de YouTube sobre contenido no auténtico y etiquetado de contenido sintético.
- [ ] Cifras de METR, DORA, OWASP, RouteLLM y FrugalGPT en sus documentos originales.

## Conexiones
- [[2026-10-youtube-eric-risco-software-factory]]: el video que originó la investigación.
- [[evaluacion-video-software-factory]]: el análisis que usa estas fuentes.
- [[arnes-de-agentes]]: el concepto que más fuentes respaldan.
- [[enrutamiento-de-modelos]]: la disciplina de costos.
- [[lagunas]]: lo que quedó por verificar.
