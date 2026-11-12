---
tipo: concepto
area: transversal
estado: borrador
confianza: media
resumen: "Proceso repetible y auditable con IA dentro, hecho de pasos de código, pasos de agente y aprobación humana; sirve como criterio de diagnóstico para cualquier proceso de una empresa."
fuentes: ["[[2026-10-youtube-eric-risco-software-factory]]", "[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]"]
creado: 2026-11-11
actualizado: 2026-11-11
revisar_antes: 2027-11-11
etiquetas: [fase-1, agentes]
---

# Fábrica de IA

## Definición
Una fábrica de IA es **un proceso repetible y auditable con inteligencia artificial dentro**: el trabajo entra por un lado, sale por otro y en medio hay pasos que no necesitan a una persona, aunque una persona diseñó el sistema ([[2026-10-youtube-eric-risco-software-factory]], min 01:38). Cuando el proceso es programar, se llama **fábrica de software** (*software factory*); cuando es producir videos o publicaciones, **fábrica de contenido** (*content factory*).

Tiene tres tipos de pasos:

| Tipo de paso | Cómo se comporta | Ejemplo en una pyme |
|---|---|---|
| **Código** | Siempre hace lo mismo | Buscar un precio en la hoja de inventario; calcular el IVA |
| **Agente** | Decide según lo que entra | Entender un mensaje de WhatsApp; redactar la cotización |
| **Humano** | Aprueba o corrige | Autorizar un descuento fuera de tabla |

A cada paso hay que darle cuatro cosas: qué hace, cómo lo hace, cuál es su resultado y cómo se revisa ese resultado (min 02:46). Además, la fábrica necesita una **memoria** (el *brain*) con las decisiones y reglas que los agentes consultan antes de actuar (min 04:00).

> [!warning] Contradicción · el término tiene dos significados
> Nvidia llama «AI factory» a los centros de datos que producen *tokens*. Al buscar el término aparecen los dos sentidos mezclados ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]). En esta wiki, «fábrica de IA» es siempre el proceso.

## Por qué importa
- Es la forma en que las empresas de vanguardia organizan el trabajo con agentes. Stripe intercala bucles de agente con código determinista para que los pasos obligatorios se ejecuten siempre ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).
- Da un **criterio de diagnóstico**: un proceso sirve para la IA si se repite y si cada paso deja rastro.
- Explica por qué la mayoría de los casos de una pyme son **flujos** (el camino lo fija el código) y no agentes sueltos ([[automatizacion-de-procesos]]).

## Las doce piezas que hacen que una fábrica funcione
El video enseña la línea de montaje. Esto es lo que le falta, según las empresas que publican resultados ([[evaluacion-video-software-factory]]):

1. Comprobaciones automáticas que no dependan de una IA (pruebas, reglas fijas).
2. Pruebas que el agente que construye no pueda acomodar.
3. Límite de vueltas y de gasto (Stripe corta en dos rondas).
4. El costo por caso ([[enrutamiento-de-modelos]]).
5. Defensa de la entrada frente a instrucciones maliciosas.
6. Permisos mínimos y entorno aislado.
7. Reglas de riesgo escritas en código, no opinadas por un agente.
8. Marcha atrás y vigilancia después de publicar.
9. Medición: porcentaje de casos bien resueltos y costo por resultado correcto ([[medicion-de-roi]]).
10. Alguien que cuide la memoria.
11. Un humano que pueda juzgar lo que aprueba.
12. Saber cuándo no montar una fábrica.

> [!tip] Supuesto
> El tamaño de un cambio no es su riesgo: un texto legal es pequeño y puede tener consecuencias grandes. La puerta humana debe decidirse por lo que está en juego (dinero, datos personales, textos legales) y no por el tamaño. Se valida al diseñar la demo de la semana 4 ([[ia-en-whatsapp-y-atencion]]).

## Cómo lo aplicamos en Arvyon
- **En el diagnóstico:** las doce piezas son la lista de preguntas que separa una propuesta seria de una demostración: ¿cómo sabemos que lo hizo bien?, ¿cuánto cuesta cada caso?, ¿quién aprueba qué?, ¿qué pasa si se equivoca?, ¿cómo lo deshacemos? ([[diagnostico-expres]], para la Fase 2).
- **En el diseño:** cada automatización se dibuja como una tabla de pasos con su tipo y su forma de revisión ([[proceso-de-entrega]]).
- **En el cerebro:** el flujo de ingesta de esta wiki ya es una pequeña fábrica: entra una fuente, salen páginas, un programa revisa y una persona aprueba ([[arnes-de-agentes]]).
- **Lo que no hacemos:** montar una fábrica de código. Exige programar y no es lo que compra una pyme ([[programacion-y-bases-de-datos]]).

## Ejemplos
**Ferretería ficticia: cotizaciones por WhatsApp** (ejemplo inventado para estudiar; coincide con la demo 1 de la semana 3 del [[curriculo]]):

| # | Paso | Tipo | Cómo se revisa |
|---|---|---|---|
| 1 | Llega un mensaje pidiendo una cotización | Entrada | Queda registrado con fecha y remitente |
| 2 | Extraer productos y cantidades | Agente | Código: ¿están todos los campos? |
| 3 | Buscar precios y existencias en la hoja | Código | Siempre da lo mismo |
| 4 | Calcular total, IVA y descuento según la tabla | Código | Siempre da lo mismo |
| 5 | Redactar la cotización con el tono de la empresa | Agente | Código: ¿los números coinciden con el paso 4? |
| 6 | Regla fija: si supera un tope, pide un descuento fuera de tabla o falta un precio, va a una persona | Código | La regla está escrita, no la decide la IA |
| 7 | Aprobar o corregir | Humano | Queda registrado quién aprobó |
| 8 | Enviar y guardar en el registro | Código | Reporte semanal de casos y errores |

Memoria de esta fábrica: lista de precios, política de descuentos, tono de la empresa y preguntas frecuentes.

**Casos reales comparados:** OpenAI, Stripe y StrongDM, en [[evaluacion-video-software-factory]].

## Conexiones
- [[arnes-de-agentes]]: el entorno que hace fiable cada paso de agente.
- [[enrutamiento-de-modelos]]: qué modelo usa cada paso y cuánto cuesta.
- [[automatizacion-de-procesos]]: el bloque donde se practica (n8n).
- [[evaluacion-video-software-factory]]: el análisis del video que introdujo el concepto.
- [[rag-y-agentes]]: los agentes, sus riesgos y cuándo no usarlos.
- [[metodo-4d]]: Diseñar y Desplegar son, en la práctica, dibujar y montar la fábrica.
- [[2026-10-youtube-eric-risco-software-factory]]: la fuente del concepto.
