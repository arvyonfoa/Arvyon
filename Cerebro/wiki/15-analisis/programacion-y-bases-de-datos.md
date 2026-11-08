---
tipo: analisis
area: conocimiento
estado: borrador
confianza: media
resumen: "Respuesta del consultor: no en la Fase 1; sí alfabetización técnica (API, JSON, webhooks, datos en tablas) y, después del 15 de diciembre, Python básico y SQL básico."
fuentes: ["[[2026-11-barrido-ligero-competidores]]"]
creado: 2026-11-08
actualizado: 2026-11-08
revisar_antes: 2027-02-08
etiquetas: [fase-1]
---

# ¿Debo aprender Python, TypeScript o PostgreSQL?

## Pregunta
¿Debería aprender un lenguaje de programación (Python o TypeScript) y algo técnico de bases de datos como PostgreSQL?

## Respuesta corta
**No durante la Fase 1** (hasta el 15 de diciembre). **Sí** necesitas **alfabetización técnica**: entender API, JSON, webhooks y datos en tablas, porque sin eso no podrás construir automatizaciones. Después del 15 de diciembre, **Python básico** y **SQL básico** sí valen la pena. **TypeScript y la administración de PostgreSQL no**, salvo que Arvyon decida construir productos de software.

## Desarrollo
**1. Lo que hace la competencia que atiende pymes.** Casi todas trabajan con herramientas sin código o de poco código: n8n, Make, Zapier, WhatsApp, CRM y el software contable ([[2026-11-barrido-ligero-competidores]]). El cliente compra resultados (horas ahorradas, respuestas más rápidas), no código.

**2. Lo que sí es imprescindible (Etapa 2, semana del 23 de noviembre):** la [[alfabetizacion-tecnica]]:
- qué es una API y cómo se conectan dos aplicaciones;
- leer y escribir JSON (el formato en que viajan los datos entre aplicaciones);
- webhooks (cuando una aplicación avisa a otra que pasó algo);
- claves de API y permisos (y por qué nunca se comparten);
- datos en tablas: filas, columnas, identificadores y relaciones entre tablas.

**3. El caso de n8n.** n8n permite escribir pequeñas expresiones y nodos de código en **JavaScript** (y también en Python). Basta con aprender a leer y adaptar expresiones cortas cuando las necesites; no hace falta un curso de JavaScript ni de TypeScript.

**4. Python, después del 15 de diciembre.** Es el lenguaje de los datos y de la IA. Con un nivel básico (variables, listas, leer un Excel o CSV, llamar a una API) puedes analizar datos de un cliente, prototipar con la API de un modelo y entender el código que te genera un asistente como Claude Code. Calcula unas 20 a 30 horas.

**5. Bases de datos.** No necesitas administrar PostgreSQL. Sí te conviene, en este orden:
- **Fase 1:** entender datos en tablas y relaciones (2 o 3 horas, dentro de la alfabetización técnica).
- **Fase 2:** **SQL básico** (SELECT, WHERE, GROUP BY, JOIN), útil para reportes y tableros ([[datos-y-reportes]]) y porque muchos asistentes con documentos propios guardan la información en bases de datos como PostgreSQL ([[rag-y-agentes]]).
- **Nunca, salvo que construyas productos:** administración de servidores de bases de datos.

**6. TypeScript.** Solo tiene sentido si Arvyon decide construir aplicaciones web propias. Hoy no es el modelo de negocio ([[modelo-de-ingresos]]).

## Método
Comparación entre lo que venden y usan los competidores ([[2026-11-barrido-ligero-competidores]]), lo que exige cada bloque del [[curriculo]] y el tiempo disponible en la Fase 1 (5 semanas).

> [!tip] Supuesto
> Con asistentes de programación (Claude Code, Copilot) un consultor puede construir más sin programar desde cero, pero **tiene que entender lo que el asistente genera** para no entregar algo que no sabe mantener. Por eso Python básico sí es una buena inversión después de la Fase 1.

## Fuentes
- [[2026-11-barrido-ligero-competidores]]

## Vigencia
Válido hasta 2027-02-08 o hasta que Arvyon decida construir productos de software propios.

## Conexiones
- [[alfabetizacion-tecnica]]: lo mínimo técnico que sí hay que aprender ahora.
- [[automatizacion-de-procesos]]: donde se usa.
- [[datos-y-reportes]]: donde SQL ayuda.
- [[curriculo]]: el plan de estudio.
