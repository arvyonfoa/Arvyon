# Registro del segundo cerebro de Arvyon

> Registro cronológico en el que solo se añaden entradas al final; nunca se editan las anteriores. Formato: `## [AAAA-MM-DD] tipo | Título`.
> Tipos: `setup`, `ingest`, `query`, `research`, `study`, `lint`, `decision`, `schema`.
> Últimas entradas: `grep "^## \[" log.md | tail -5`

## [2026-11-03] setup | Creación de la estructura del segundo cerebro
- Se creó `Cerebro/` con las tres capas: `raw/` (inmutable), `wiki/` (mantenida por el agente) y el esquema (`CLAUDE.md`, `AGENTS.md`).
- Archivos de soporte: `PROMPT-MAESTRO.md`, `README.md`, `index.md`, `log.md`, configuración de Obsidian (`.obsidian/`) y `herramientas/revisar_wiki.py`.
- 10 plantillas en `wiki/_plantillas/`: fuente, tema, entidad, concepto, competidor, entrevista, análisis, decisión, estudio y riesgo.
- Páginas de cada área creadas en estado `semilla`, con las preguntas a investigar y las fuentes sugeridas.
- Currículo del consultor de IA: [[curriculo]], con 12 bloques de estudio en `11-conocimiento-ia/`.

## [2026-11-03] ingest | Presentación para socios · Consultora de IA (octubre 2026)
- Fuente: `raw/00-internos/presentacion-consultora-ia.pdf` (+ `.html`) → [[presentacion-socios-2026-10]].
- Páginas tocadas:
  - Panorama: [[tesis-arvyon]], [[hoja-de-ruta-90-dias]], [[preguntas-abiertas]].
  - Mercado: [[adopcion-ia-colombia]], [[mipymes-colombia]], [[sectores-prioritarios]], [[politica-publica-ia]].
  - Demanda: [[segmentos]], [[dolores-y-necesidades]], [[programa-10-entrevistas]], [[objeciones]].
  - Competencia: [[posicionamiento]].
  - Oferta: [[paquetes-estandar]], [[paquete-a-la-medida]], [[diagnostico-expres]], [[metodo-4d]], [[acompanamiento-mensual]].
  - Finanzas: [[modelo-de-ingresos]], [[estrategia-de-precios]], [[cobros-y-cambio]].
  - Legal: [[acuerdo-de-socios]], [[roles-de-socios]], [[figura-legal]].
  - Marketing: [[embudo]], [[instagram]], [[linkedin]], [[whatsapp-business]], [[pagina-web]].
  - Operación: [[husos-horarios]], [[stack-herramientas]], [[proceso-de-entrega]].
  - Riesgos y oportunidades: [[registro-de-riesgos]], [[dofa]].
  - Entidades y conceptos: [[arvyon]], [[conpes-4144]], [[ley-1581-de-2012]], [[rgpd]], [[reglamento-europeo-de-ia]], [[endeavor]], [[mincomercio]], [[brecha-de-adopcion]], [[caso-de-exito]], [[iman-de-clientes]].
  - Decisiones: [[registro-de-decisiones]] y dec-001 a dec-007.
- Aportes del fundador posteriores a la fuente: nombre **Arvyon** ([[dec-001-nombre-de-la-consultora]]) y YouTube como canal estratégico ([[dec-008-youtube-como-canal-estrategico]], [[youtube]]).
- Contradicción o precisión: el dato 61 % / 37,7 % es de empresas de 50+ empleados y no aplica a micro ([[adopcion-ia-colombia]]).
- Siguiente paso propuesto: Sprint 1 de [[agenda-de-investigacion]] (entrevistas, contador, competencia).

## [2026-11-06] decision | Fase de aprendizaje: se elimina el Sprint 1
- El fundador está aprendiendo y no hará entrevistas ni otras acciones con terceros por ahora → [[dec-009-fase-de-aprendizaje]].
- Se elimina el Sprint 1 de [[agenda-de-investigacion]]; los demás sprints se renumeran (1 a 5) y quedan en pausa. Se cierra sin unir el PR del plan del Sprint 1.
- Páginas tocadas: [[agenda-de-investigacion]], [[preguntas-abiertas]], [[programa-10-entrevistas]] (en pausa), [[impuestos-y-facturacion]], [[dec-003-figura-legal-y-pais-de-facturacion]], [[registro-de-decisiones]], [[curriculo]] (ahora es la prioridad), [[tesis-arvyon]].

## [2026-11-06] schema | El prompt maestro arranca por el estudio
- `PROMPT-MAESTRO.md`: §7.1 y §12 proponen el siguiente paso de estudio en lugar del Sprint 1; §10 sin el Sprint 1 y con la fase de aprendizaje como fase actual.

## [2026-11-08] decision | Fechas de la Fase 1: del 2026-11-09 al 2026-12-15
- El fundador fija la fase de aprendizaje del lunes 2026-11-09 al 2026-12-15 → [[dec-009-fase-de-aprendizaje]], con criterios de paso a la Fase 2.
- [[curriculo]]: el plan de 12 semanas pasa a 5 semanas en 3 etapas; los bloques 6, 9, 11-A y 12 quedan para la Fase 2.

## [2026-11-08] schema | Principio rector: primero se aprende, después se actúa
- `PROMPT-MAESTRO.md`: principio rector con las dos fases y los criterios de paso; el agente también es tutor; flujos 7.9 (sesión de estudio) y 7.10 (cambio de fase); la agenda y los sprints son de la Fase 2; plan 9.3 de 5 semanas; primera tarea según la fase; tipo de registro `study`.
- `CLAUDE.md`: bloque de fase vigente y sesión de estudio.

## [2026-11-08] research | Cursos de la Etapa 1, competidores y artículo 4 del Reglamento de IA
- Fuentes guardadas e ingeridas (modo agrupado, investigación ligera pedida por el fundador):
  - [[2026-11-investigacion-web-cursos-etapa-1]] (`raw/cursos/`)
  - [[2026-11-barrido-ligero-competidores]] (`raw/competencia/`)
  - [[2026-11-comision-europea-faq-alfabetizacion-ia]] (`raw/legal/`)
- Páginas nuevas: [[guia-etapa-1]], [[capacidades-de-la-competencia]], [[alfabetizacion-tecnica]].
- Páginas tocadas: [[curriculo]], [[mapa-competitivo]], [[estrategia-de-precios]], [[posicionamiento]], [[tesis-arvyon]], [[metodo-4d]] (choque de nombre con las «4D» de Anthropic), [[reglamento-europeo-de-ia]] y [[alfabetizacion-en-ia]] (Ómnibus Digital 2026/1744), [[whatsapp-business]], [[automatizacion-de-procesos]], [[ia-en-whatsapp-y-atencion]], [[herramientas-para-pymes]], [[fundamentos-llm]], [[prompting-para-empresas]], [[lagunas]].
- Contradicción registrada: el artículo 4 ya no exige un nivel «suficiente» de alfabetización.

## [2026-11-08] query | ¿Debo aprender Python, TypeScript o PostgreSQL?
- Archivado en [[programacion-y-bases-de-datos]]: no en la Fase 1; sí [[alfabetizacion-tecnica]]; Python y SQL básicos en la Fase 2; TypeScript y administración de PostgreSQL solo si se construyen productos.
- Siguiente paso: empezar la Etapa 1 el lunes 2026-11-09 con «IA Para Todos (Español)», módulo 1 ([[guia-etapa-1]]).

## [2026-11-08] schema | Manual Cerebro Arvyon v1.0
- Nuevo sitio HTML de 9 páginas en `manual/` (estilo y comportamiento comunes en `manual/assets/`): inicio, el proyecto, qué es un segundo cerebro, mapa del cerebro, cómo se usa, GitHub, la nube de Claude Code y sus entornos, cómo se crea la empresa, glosario y preguntas.
- Regla: el manual solo se actualiza cuando el fundador lo pide (en `CLAUDE.md` y en el prompt maestro).
- Nuevo `CLAUDE.md` en la raíz del repositorio que apunta a `Cerebro/CLAUDE.md`, para que el agente encuentre las reglas aunque la sesión empiece en la raíz.
