---
tipo: estudio
area: conocimiento
estado: semilla
confianza: media
resumen: "Bloque 6: asistentes que responden con los documentos de la empresa y agentes que ejecutan tareas, con sus riesgos y costos."
fuentes: []
creado: 2026-11-03
actualizado: 2026-11-03
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

## Conexiones
- [[curriculo]]: bloque n.º 6.
- [[tendencias]]: los agentes son tendencia.
- [[gobernanza-y-regulacion]]: permisos y riesgos.
- [[fundamentos-llm]]: base técnica.
