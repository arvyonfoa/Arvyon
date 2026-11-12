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

## [2026-11-08] schema | Manual en un solo archivo
- A pedido del fundador, el manual pasa a ser un único archivo HTML autocontenido y descargable: `manual/manual-cerebro-arvyon.html`. Se eliminan las 9 páginas sueltas y `manual/assets/`. Se retira la copia publicada en claude.ai.

## [2026-11-08] lint | Limpieza de todo el repositorio
- Revisión de salud del cerebro: 0 errores, 0 avisos. Revisión de los archivos fuera del cerebro.
- Eliminados (decisión del fundador):
  - `Cerebro.md` y `Raw.md` en la raíz: notas vacías (0 bytes) creadas por Obsidian.
  - `Raw/` en la raíz: copia idéntica de `raw/00-internos/` (la presentación queda solo dentro del cerebro).
  - `.obsidian/` de la raíz: la bóveda de Obsidian es `Cerebro/`; se añade un `.gitignore` en la raíz para que no se vuelva a subir.
- Actualizados: `README.md` y `CLAUDE.md` de la raíz, y el manual a v1.1 (referencias a `Raw/` y estado de los pull requests).
- Se conservan los `.gitkeep` de `raw/`: mantienen las subcarpetas vacías que el agente usará.

## [2026-11-08] lint | Revisión de salud antes de empezar la Fase 1
- `revisar_wiki.py`: 105 páginas, 0 errores, 0 avisos. Estados: borrador=65, semilla=35, estable=5.
- Contradicciones abiertas: 1 (artículo 4 del Reglamento Europeo de IA tras el Ómnibus Digital; pendiente de leer el texto final en EUR-Lex).
- Lagunas abiertas: 16. Callouts «Por verificar»: 6. Decisiones abiertas: 6 de 9.
- Avance del currículo: 0 niveles marcados (la Fase 1 empieza el 2026-11-09).
- Revisiones que vencen pronto: ninguna antes del 2027-02-03; ese mes vencen unas 70 páginas de mercado y herramientas.
- Entidades mencionadas en 5 o más páginas sin página propia: n8n, Microsoft Copilot, Make, Zapier, HubSpot, Siigo, Alegra. Se propone crearlas cuando se estudien en la Etapa 2.

## [2026-11-11] research | Fábricas de IA, harness engineering con Pi y enrutamiento de modelos
- Pregunta del fundador: ¿aportan a mi aprendizaje la fábrica de software y la de contenido del video de Eric Risco, el *harness engineering* basado en Pi y la disciplina de elegir modelo y razonamiento para ahorrar? ¿Qué le faltó al video? ¿Qué más debo saber?
- El plan de estudio del día queda pendiente por decisión del fundador.
- Entregado primero en PDF (20 páginas), aprobado por el fundador antes de entrar al cerebro: `raw/informes/2026-11-11-informe-fabricas-de-ia-arneses-enrutamiento.pdf`.
- Investigación de escritorio: no se contactó a nadie ni se probó ninguna herramienta (Fase 1).

## [2026-11-11] ingest | Video de Eric Risco «Monta tu Software Factory» e investigación web asociada
- Fuentes en raw: `raw/transcripciones/2026-10-23-eric-risco-software-factory.md` (subtítulos automáticos completos), `raw/articulos/2026-11-11-investigacion-web-fabricas-arneses-enrutamiento.md` y el informe en PDF.
- Páginas nuevas (8): [[2026-10-youtube-eric-risco-software-factory]], [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]], [[fabrica-de-ia]], [[arnes-de-agentes]], [[enrutamiento-de-modelos]], [[eric-risco]], [[pi-coding-agent]], [[evaluacion-video-software-factory]].
- Páginas tocadas (10): [[curriculo]], [[automatizacion-de-procesos]], [[rag-y-agentes]], [[medicion-de-roi]], [[gobernanza-y-regulacion]], [[contenido-y-marca-personal]], [[youtube]] (primeras lecciones de formato), [[tendencias]], [[lagunas]], [[glosario]].
- Fiabilidad: video 3 de 5 (practicante con interés comercial y sin cifras propias); fuentes de contraste entre 2 y 5 (tabla en la página de la investigación).
- Paso 4 del flujo (conversar los puntos clave): se cumplió con el PDF previo y el «Ingiérelo» del fundador.
- Contradicciones marcadas: 2 (si Pi trae conectores MCP; nombres de las versiones del modelo Sol) y una advertencia de término («AI factory» también nombra los centros de datos de Nvidia).
- Tesis: sin cambios; ninguna hipótesis central se refuerza ni se debilita. Decisiones: sin cambios.
- Currículo: no cambia el calendario; se añadió dónde entra cada idea (semanas 2 a 5 y Fase 2). Avance: 0 niveles marcados.
- Lagunas nuevas: 9 (comentarios del video, publicación de RSC Factory, cifras originales de OpenAI, políticas de YouTube y de Anthropic, precios por modelo, entre otras).
- Límites: no se vio la imagen del video; la página original de OpenAI no se pudo leer; varias cifras llegan por fuentes secundarias.
- Manual: no se tocó. Sigue vigente; no menciona los conceptos nuevos.
- Siguiente: retomar el plan de estudio (semana 1, «IA Para Todos»); en la semana 3, diseñar la demo de cotización como una fábrica de IA.

## [2026-11-12] ingest | Documentación oficial de OpenCode (versión 2)
- Motivo: el fundador migra de Claude Code a OpenCode. Investigación de escritorio sobre la herramienta con la que se mantiene el cerebro; no se instaló ni se probó.
- Fuente en raw: `raw/articulos/2026-11-12-investigacion-web-opencode.md` (12 páginas de `opencode.ai/docs`).
- Páginas nuevas (2): [[2026-11-investigacion-web-opencode]], [[opencode]].
- Páginas tocadas (4): [[stack-herramientas]], [[arnes-de-agentes]], [[glosario]], [[lagunas]].
- Fiabilidad: 4 de 5 (fuente primaria del proveedor; cambia a menudo).
- Hallazgos que obligan a cambiar el esquema: la versión 2 solo lee `AGENTS.md` (ya no usa `CLAUDE.md` como respaldo) y permite casi todas las acciones sin preguntar.
- Contradicción marcada: 1 (la documentación de la versión 1 y la de la versión 2 sobre `CLAUDE.md`).
- Lagunas nuevas: 4 (integración con GitHub en la versión 2, ruta de las credenciales, suscripción de Claude, comando `/init`).
- Tesis, decisiones y currículo: sin cambios.

## [2026-11-12] schema | El esquema pasa a AGENTS.md y el manual sube a v2.0 (migración a OpenCode)
- A pedido del fundador. Nuevo `AGENTS.md` en la raíz del repositorio.
- `Cerebro/AGENTS.md` es ahora el esquema completo y vale para cualquier agente. `Cerebro/CLAUDE.md` y el `CLAUDE.md` de la raíz solo importan el `AGENTS.md` de su carpeta, para Claude Code. Hay una única copia de las reglas.
- Reglas nuevas en el esquema, porque fuera de la nube ya no las impone la herramienta: sección «Git y GitHub» (rama de trabajo `verificacion`, nada directo en `main`, sin *force push*, los *pull requests* los une el fundador, nada de claves en el repositorio), sincronizar con `git pull` al empezar en una copia local y no pedir claves en el chat.
- `PROMPT-MAESTRO.md` y los dos `README.md`: las menciones al esquema apuntan a `AGENTS.md`.
- Manual v2.0: capítulo nuevo 7 «OpenCode en tu computador» (qué cambia, instalación, modelos, conexión con GitHub, protecciones, sesión de trabajo, errores comunes); se conserva todo lo de Claude Code; estado, historial de *pull requests* y glosario al día. Los capítulos de la empresa y del glosario pasan a ser el 8 y el 9.
- Corrección en el manual: las puntas de flecha de los diagramas no se dibujaban fuera del capítulo Inicio (identificadores repetidos); ahora cada diagrama tiene los suyos.
- No se creó `opencode.jsonc`: el manual trae un ejemplo de permisos sin probar para que el fundador lo pida si lo quiere.
- `revisar_wiki.py`: 115 páginas, 0 errores, 0 avisos.
- Siguiente: instalar OpenCode, conectar un modelo y GitHub con el capítulo 7, y retomar el plan de estudio (semana 1, «IA Para Todos»).

## [2026-11-12] schema | Prompt maestro puesto al día
- A pedido del fundador. `PROMPT-MAESTRO.md` queda coherente con `AGENTS.md` y con la wiki.
- Nuevo en el prompt: regla de oro 6 (las reglas las cumple el agente, no la herramienta), sección 3.1 «Git y GitHub», flujo 7.11 «Abrir y cerrar cada sesión», y `manual/` y los archivos de la raíz en la estructura de carpetas.
- Currículo (sección 9.2): los bloques 1, 2, 4, 5, 6, 8, 10, 11 y 12 recogen las ideas de la investigación del 2026-11-11 ([[arnes-de-agentes]], [[fabrica-de-ia]], [[enrutamiento-de-modelos]], seguridad de agentes, costo por resultado exitoso). El calendario de la sección 9.3 no cambia.
- Agenda (sección 8): canales de referencia en [[youtube]] y tendencias nuevas en [[tendencias]].
- Regla aclarada, pendiente de que el fundador la confirme: la fiabilidad máxima de 3 para fuentes de vendedores se aplica cuando hablan del mercado o de los beneficios de lo que venden; la documentación técnica de un proveedor sobre su propia herramienta puede llegar a 4. Así se puntuó ya en las ingestas del 2026-11-11 y del 2026-11-12.
- Reglas de calidad (sección 11): commit, push y *pull request*; no trabajar en `main`; no pedir claves en el chat; no escribir reglas en `CLAUDE.md`.
- No se tocaron la tesis, las decisiones, el calendario de estudio ni el manual.
- `revisar_wiki.py`: 115 páginas, 0 errores, 0 avisos.

## [2026-11-12] schema | Fiabilidad de las fuentes: escala de 2 a 5 con tabla de criterios y validación
- Decisión del fundador: se aplica la regla aclarada (un vendedor no pasa de 3 cuando habla del mercado o de sus beneficios; la documentación técnica sobre su propia herramienta puede llegar a 4) y la tabla de notas de 2 a 5 queda como criterio oficial.
- `PROMPT-MAESTRO.md`: nueva sección 5.7 con la tabla (5, 4, 3 y 2), el tope para vendedores, cuándo se baja un punto, la regla de que por debajo de 2 no se ingiere, las notas múltiples y la relación con `confianza`. El paso 3 de la ingesta (7.2) remite a esa tabla.
- `AGENTS.md`: resumen de la escala en las convenciones y en el paso 3 de la ingesta.
- `herramientas/revisar_wiki.py`: da error si una página de fuente no tiene nota de fiabilidad o si la nota está fuera de 2 a 5.
- Plantilla de fuente y las 7 páginas de `14-fuentes/`: la fila pasa a llamarse «Fiabilidad (2–5)». Se revisaron las 27 notas existentes contra la tabla: todas están entre 2 y 5 y ninguna cambia. Solo se reescribió el motivo de dos (Anthropic y OpenCode) para citar el tope de 4.
- [[glosario]]: término «Fiabilidad (de una fuente)».
- Manual: no se tocó. No menciona la escala de fiabilidad, y su descripción de la revisión de salud no incluye la comprobación nueva.
- `revisar_wiki.py`: 115 páginas, 0 errores, 0 avisos.

## [2026-11-12] schema | Skill estructura-cerebro, manual v2.1 y prompt maestro al día
- A pedido del fundador.
- **Skill nueva `estructura-cerebro`** en la raíz del repositorio: `.agents/skills/estructura-cerebro/SKILL.md` (el mapa: qué es cada carpeta y archivo, dónde va cada cosa y qué se actualiza junto) y `mapa.py` (imprime la estructura real y avisa si no coincide con el mapa). Para Claude Code hay un puntero en `.claude/skills/estructura-cerebro/SKILL.md`, sin contenido propio. La skill no tiene reglas: las reglas siguen en `AGENTS.md` y en el prompt maestro.
- Por qué en `.agents/skills/`: es una carpeta neutral que OpenCode lee; `.claude/skills/` es la única que busca Claude Code. Fuente: `raw/articulos/2026-11-12-investigacion-web-opencode-skills.md`, añadida a [[2026-11-investigacion-web-opencode]] y a [[opencode]].
- `AGENTS.md` (raíz y `Cerebro/`), `PROMPT-MAESTRO.md` (sección 4, flujo 7.11 y reglas de la sección 11) y el `README.md` de la raíz remiten a la skill.
- **Manual v2.1:** sección nueva «Cuánto confiar en cada fuente» (capítulo 2), árbol de la raíz y apartado de la skill (capítulo 3), la comprobación de fiabilidad en la revisión de salud, `@estructura-cerebro` en la tabla de OpenCode, dos términos del glosario y dos preguntas frecuentes. `index.md` cita la versión nueva del manual.
- [[glosario]]: término «Skill». [[lagunas]]: probar que OpenCode carga la skill.
- No se probó la skill en OpenCode (no está instalado en esta sesión). `mapa.py` sí se ejecutó: 0 problemas.
- `revisar_wiki.py`: 115 páginas, 0 errores, 0 avisos.
- Siguiente: unir el pull request, instalar OpenCode con el capítulo 7 del manual y retomar el plan de estudio (semana 1, «IA Para Todos»).

## [2026-11-12] lint | Verificación final de la migración a OpenCode (prueba con la versión 2.2.7)
- A pedido del fundador: comprobar qué faltaba y actualizar prompt maestro, `AGENTS.md`, skill y manual.
- **Prueba real.** Se instaló OpenCode 2.2.7 en una carpeta temporal de la sesión, sin conectar un modelo ni enviar mensajes. Resultados en `raw/articulos/2026-11-12-prueba-opencode-2-2-7.md`:
  - abierto en `Cerebro/`, vigila `Cerebro/AGENTS.md` y el `AGENTS.md` de la raíz; no lee `CLAUDE.md`;
  - encuentra la skill `estructura-cerebro` en `.agents/skills/`, desde la raíz y desde `Cerebro/`;
  - aplica las reglas de `opencode.jsonc`; un archivo inválido no se aplica;
  - no existe `opencode github`; sí existen `/init`, `/review` y `/goal`, y los agentes `build` y `plan`.
- **Lo que faltaba y se añadió:**
  - `opencode.jsonc` en la raíz: pregunta antes de cada `git push` y deniega subir a `main`, el *force push* y `gh pr merge`. Sustituye a las protecciones que ponía la nube.
  - Requisitos del computador (Git, GitHub CLI y Python 3) y qué hacer si falta Python: sección «Herramientas del sistema» en `AGENTS.md`, flujo 7.11 del prompt maestro y manual.
  - Regla de no ejecutar `/init` ni reescribir `AGENTS.md`.
  - Skill y `mapa.py`: conocen `opencode.jsonc`.
  - Manual v2.2: «Lista para migrar» con una prueba de arranque de cinco preguntas, requisitos del computador, el archivo de permisos ya creado y tres errores comunes nuevos.
- Wiki: [[opencode]], [[2026-11-investigacion-web-opencode]], [[stack-herramientas]] y [[lagunas]] (4 lagunas cerradas, 1 nueva: la primera conversación real con OpenCode).
- Auditoría de restos: sin referencias a la rama antigua ni a la escala 1–5 de fiabilidad fuera del historial; sin nombres de archivo problemáticos en Windows; versión del manual igual en cabecera, portada, pie e índice.
- Claude Code: en esta sesión aparece la skill `estructura-cerebro` (el puntero de `.claude/skills/` funciona) y el `CLAUDE.md` importa `AGENTS.md`.
- Sin comprobar: una conversación real con un modelo, la aplicación de escritorio y el sistema operativo del fundador.
- `revisar_wiki.py`: 115 páginas, 0 errores, 0 avisos. `mapa.py`: 0 problemas.
- Siguiente: unir el pull request, seguir la «Lista para migrar» del capítulo 7 y retomar el plan de estudio (semana 1, «IA Para Todos»).
