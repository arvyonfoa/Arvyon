# Cerebro · Segundo cerebro de Arvyon

Es una wiki de Markdown que **mantiene un agente LLM** (Claude Code) y que tú lees en **Obsidian**. Tú consigues las fuentes y haces las preguntas. El agente resume, cruza, archiva y mantiene todo al día.

> **¿Primera vez?** Abre el manual: `manual/manual-cerebro-arvyon.html`. Es un solo archivo: descárgalo y ábrelo con doble clic en cualquier navegador.

## Qué hay aquí

| Archivo o carpeta | Para qué sirve |
|---|---|
| `PROMPT-MAESTRO.md` | El prompt completo: rol, reglas, flujos paso a paso, agenda de investigación y currículo de consultor de IA. Pégalo en cualquier agente. |
| `CLAUDE.md` / `AGENTS.md` | El esquema operativo que el agente lee en cada sesión. |
| `index.md` | El catálogo de todas las páginas. |
| `log.md` | Lo que pasó y cuándo. |
| `raw/` | Tus fuentes originales. **Nunca se editan.** |
| `wiki/` | Lo que escribe el agente. |
| `manual/` | El Manual Cerebro Arvyon: un solo archivo HTML que explica todo el sistema. |
| `herramientas/revisar_wiki.py` | La revisión de salud: enlaces rotos, huérfanas, frontmatter y páginas fuera del índice. |

## Puesta en marcha (una sola vez)

1. **Obsidian:** abre `Cerebro/` como bóveda (*Open folder as vault*). La configuración básica ya viene en `.obsidian/`: los adjuntos van a `raw/assets/` y las plantillas están en `wiki/_plantillas/`.
2. **Plugins** (*Settings → Community plugins*):
   - **Dataview**: hace que funcione `wiki/00-panorama/tablero.md`.
   - **Marp Slides**: para presentaciones generadas desde la wiki (opcional).
3. **Obsidian Web Clipper** (extensión del navegador): configura la carpeta de destino en `raw/articulos/`.
4. **Descarga de imágenes:** en *Settings → Hotkeys* busca "Download attachments for current file" y asígnale `Ctrl+Shift+D`. Después de recortar un artículo, pulsa el atajo.
5. **Agente:** abre Claude Code en esta carpeta y pega el contenido de `PROMPT-MAESTRO.md` (de *INICIO* a *FIN*). En las sesiones siguientes basta con decir lo que quieres hacer.

## Rutina recomendada

| Cuándo | Qué haces tú | Qué le pides al agente |
|---|---|---|
| Cada día (15–30 min) | Guardas 1 o 2 fuentes en `raw/` | "Ingiere `raw/…`" |
| Después de cada entrevista | Guardas las notas en `raw/entrevistas/` (anonimizadas) | "Ingiere la entrevista y actualiza los patrones" |
| Cada semana | Lees lo actualizado y revisas la vista gráfica | "Haz la revisión semanal" |
| Cada mes | Reunión de socios | "Haz la revisión mensual y prepara el resumen para socios" |

## Frases útiles para el agente

```text
Ingiere raw/informes/<archivo>.pdf y dime los 5 puntos clave antes de escribir.
¿Qué sabemos de la retención en la fuente al facturar desde Polonia? Archiva la respuesta.
Investiga en la web: competidores de automatización con WhatsApp en Colombia. Guarda las fuentes en raw/competencia/.
Haz la revisión semanal.
Prepara la decisión dec-005 con lo que ya sabemos y lo que falta.
Convierte el bloque 4 del currículo en un guion de video de YouTube de 10 minutos.
```

## Revisión de salud

```bash
python3 herramientas/revisar_wiki.py
```
