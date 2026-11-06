# Registro del segundo cerebro de Arvyon

> Registro cronológico en el que solo se añaden entradas al final; nunca se editan las anteriores. Formato: `## [AAAA-MM-DD] tipo | Título`.
> Tipos: `setup`, `ingest`, `query`, `research`, `lint`, `decision`, `schema`.
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
