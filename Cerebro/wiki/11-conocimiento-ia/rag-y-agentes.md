---
tipo: estudio
area: conocimiento
estado: borrador
confianza: media
resumen: "Bloque 6: asistentes que responden con los documentos de la empresa y agentes que ejecutan tareas, con sus riesgos y costos."
fuentes: ["[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]", "[[2026-10-youtube-eric-risco-software-factory]]"]
creado: 2026-11-03
actualizado: 2026-11-11
revisar_antes: 2027-02-03
etiquetas: []
---

# Asistentes con documentos propios (RAG) y agentes

## Qué es
RAG (generación aumentada por recuperación) significa que la IA busca en los documentos de la empresa antes de responder. Los agentes van un paso más allá: usan herramientas (correo, CRM, hojas) para ejecutar tareas, por ejemplo mediante el protocolo MCP. Este mismo segundo cerebro es un ejemplo del patrón «wiki mantenida por un LLM».

## Por qué lo demanda el cliente
Las medianas y grandes quieren «chatear con sus manuales, políticas y procesos». Es un producto de alto valor para el paquete Transforma (SUPUESTO por validar).

## Qué aprender
- [ ] **Básico (explicarlo):** qué es un RAG y cuándo basta con un asistente que tiene archivos adjuntos.
- [ ] **Intermedio (implementarlo):** preparar documentos, fragmentarlos, evaluar las respuestas con preguntas de prueba y gestionar permisos.
- [ ] **Avanzado (diseñarlo y venderlo):** agentes con herramientas, supervisión humana, riesgos (acciones no deseadas, filtración de datos) y costos; cuándo NO usar agentes.

## Ejercicio práctico
Crea un asistente con el manual de procedimientos de una empresa ficticia. Diseña 20 preguntas de prueba con su respuesta correcta y mide la tasa de acierto. Documenta qué falló y por qué.

## Recursos (por verificar)
- Documentación de los proveedores sobre asistentes con archivos, RAG y MCP.
- Este mismo repositorio: `PROMPT-MAESTRO.md` como caso de estudio del patrón wiki.

## Cómo se convierte en producto y contenido
- Módulo nuevo propuesto: «Asistente con los documentos de tu empresa» ([[paquete-a-la-medida]]).
- Video de YouTube: «Pon a la IA a responder con los manuales de tu empresa».

## Lo que hay que saber de los agentes (2026-11)
- **Agente = modelo + arnés.** Lo que hace fiable a un agente no es el modelo sino su entorno: instrucciones, memoria, herramientas, permisos y comprobaciones ([[arnes-de-agentes]], [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).
- **Fábricas de agentes.** Las empresas de vanguardia organizan varios agentes en línea, con pasos de código y aprobación humana entre ellos ([[fabrica-de-ia]], [[evaluacion-video-software-factory]]).
- **Seguridad.** Un agente puede obedecer instrucciones escondidas en un texto ajeno (inyección de instrucciones). El riesgo es máximo cuando se juntan datos privados, contenido no confiable y un canal de salida ([[gobernanza-y-regulacion]]).
- **Costo.** Cada paso de agente puede usar un modelo distinto; el que construye, el más capaz; los que revisan o clasifican, uno menor ([[enrutamiento-de-modelos]]).
- **Conectores y habilidades.** MCP conecta al agente con herramientas y datos; las habilidades (*Skills*) le enseñan procedimientos que carga solo cuando hacen falta. Basta con saber qué son y para qué sirven.
- **Herramientas para programadores.** Claude Code, Codex y [[pi-coding-agent]] son agentes de programación. No son parte del plan de la Fase 1.

> [!note] Hecho
> Stripe integra más de mil cambios de código por semana escritos por agentes, todos revisados por personas, y limita cada tarea a dos rondas de comprobación (febrero de 2026, [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

## Conexiones
- [[curriculo]]: bloque n.º 6.
- [[tendencias]]: los agentes son tendencia.
- [[gobernanza-y-regulacion]]: permisos y riesgos.
- [[fundamentos-llm]]: base técnica.
- [[arnes-de-agentes]]: lo que rodea al modelo y lo hace fiable.
- [[fabrica-de-ia]]: cómo se organizan varios agentes.
