---
name: estructura-cerebro
description: "Mapa de la estructura del repositorio Arvyon y de su segundo cerebro (Cerebro/): qué es cada carpeta y cada archivo, dónde se guarda cada cosa y qué archivos hay que actualizar juntos. Úsala al empezar una sesión, antes de crear, mover o renombrar un archivo y siempre que dudes de dónde va algo."
---

# Estructura del repositorio Arvyon y de su segundo cerebro

Esta skill es el **mapa**. Las **reglas** están en `Cerebro/AGENTS.md` (versión operativa) y en `Cerebro/PROMPT-MAESTRO.md` (versión completa). Si el mapa y las reglas se contradicen, mandan las reglas: corrige el mapa y avisa al fundador.

## 1. Mira primero la estructura real

Desde cualquier carpeta del repositorio:

```bash
python3 .agents/skills/estructura-cerebro/mapa.py
```

(desde `Cerebro/`: `python3 ../.agents/skills/estructura-cerebro/mapa.py`)

En Windows, `python3` puede llamarse `python` o `py`.

El script imprime el árbol real con el número de archivos de cada carpeta y avisa si falta algo esperado o si hay una carpeta que este mapa no conoce. Si avisa, resuélvelo o cuéntaselo al fundador antes de seguir.

## 2. Los tres niveles

### Raíz del repositorio (`arvyonfoa/Arvyon`)

| Archivo o carpeta | Qué es |
|---|---|
| `AGENTS.md` | Instrucciones cortas para cualquier agente; remite a `Cerebro/AGENTS.md` |
| `CLAUDE.md` | Solo importa `AGENTS.md`, para Claude Code. Sin reglas propias |
| `README.md` | Presentación del repositorio para humanos |
| `opencode.jsonc` | Permisos de OpenCode: pregunta antes de `git push` y deniega subir a `main`, el *force push* y unir *pull requests* |
| `.agents/skills/estructura-cerebro/` | Esta skill: `SKILL.md` y `mapa.py` |
| `.claude/skills/estructura-cerebro/` | Puntero a esta skill, para Claude Code. Sin contenido propio |
| `Cerebro/` | El segundo cerebro. **Todo el trabajo ocurre aquí** |

### `Cerebro/` (también es la bóveda de Obsidian)

| Archivo o carpeta | Qué es | Quién lo cambia |
|---|---|---|
| `AGENTS.md` | Esquema operativo: fase vigente, convenciones, flujos, Git y GitHub | Agente y fundador; cada cambio va al historial del archivo y a `log.md` |
| `CLAUDE.md` | Solo importa `AGENTS.md` | Nadie |
| `PROMPT-MAESTRO.md` | Prompt completo: rol, contexto, reglas, flujos, agenda y currículo | Agente, cuando el fundador lo pide o cambia el esquema |
| `README.md` | Guía rápida para el humano | Agente |
| `index.md` | Catálogo de todas las páginas de `wiki/`, con contadores | Agente, en cada ingesta |
| `log.md` | Registro cronológico. Solo se añaden entradas al final | Agente, en cada sesión |
| `herramientas/revisar_wiki.py` | Revisión de salud: debe dar 0 errores | Agente |
| `manual/manual-cerebro-arvyon.html` | Manual para humanos, en un solo archivo | Agente, **solo si el fundador lo pide** |
| `raw/` | Capa 1: fuentes originales. **Inmutable** | Solo se añaden archivos nuevos |
| `wiki/` | Capa 2: lo que escribe el agente | Agente |
| `.obsidian/` | Configuración compartida de Obsidian | No se toca sin pedirlo |

### Las dos capas de contenido

**`raw/` (fuentes).** Nunca se edita, renombra ni borra un archivo. Las fuentes web se guardan aquí antes de resumirlas, con la URL y la fecha de captura en la cabecera.

| Carpeta | Qué guarda |
|---|---|
| `00-internos/` | Presentaciones, actas de socios y notas propias |
| `articulos/` | Artículos web e investigaciones web del agente |
| `informes/` | PDF de estudios e informes |
| `datos/` | CSV y Excel |
| `entrevistas/` | Notas de entrevistas, siempre anonimizadas |
| `transcripciones/` | Videos, podcasts y webinars: `AAAA-MM-DD-canal-titulo.md` |
| `competencia/` | Capturas, páginas y precios de competidores |
| `legal/` | Normas, circulares y conceptos de profesionales |
| `cursos/` | Apuntes de cursos: `AAAA-MM-DD-curso-tema.md` |
| `assets/` | Imágenes descargadas |

**`wiki/` (conocimiento).** Cada página tiene frontmatter, termina en `## Conexiones`, tiene un nombre único en `kebab-case` y aparece en `index.md`.

| Carpeta | Qué contiene | Tipo de página |
|---|---|---|
| `00-panorama/` | Tesis, preguntas abiertas, tablero y hoja de ruta | panorama |
| `01-mercado/` | Tamaño, adopción de IA, mipymes, sectores, política pública | tema |
| `02-demanda-clientes/` | Segmentos, cliente ideal, dolores, objeciones y entrevistas (`entrevista-AAAA-MM-DD-…`) | tema, entrevista |
| `03-competencia/` | Mapa competitivo y una página por competidor (`competidor-…`) | tema, competidor |
| `04-oferta/` | Paquetes, diagnóstico exprés, Método 4D, casos de uso | tema |
| `05-finanzas/` | Ingresos, precios, costos, escenarios, cobros | tema |
| `06-administracion-legal/` | Figura legal, socios, impuestos, datos, contratos | tema |
| `07-marketing-canales/` | Embudo, Instagram, YouTube, LinkedIn, WhatsApp, web | tema |
| `08-operacion/` | Husos horarios, herramientas, proceso de entrega | tema |
| `09-riesgos/` | Registro de riesgos | tema |
| `10-oportunidades/` | DOFA, tendencias, nichos, financiación | tema |
| `11-conocimiento-ia/` | Currículo, guías de etapa y un bloque de estudio por página | estudio |
| `12-entidades/` | Instituciones, normas, empresas, personas y herramientas | entidad |
| `13-conceptos/` | Ideas reutilizables | concepto |
| `14-fuentes/` | **Una** página por fuente ingerida (`AAAA-MM-medio-tema`), con su fiabilidad de 2 a 5 | fuente |
| `15-analisis/` | Respuestas valiosas archivadas, comparaciones y cálculos | analisis |
| `16-decisiones/` | Registro de decisiones (`dec-NNN-…`) | decision |
| `_plantillas/` | Plantillas: se copian, no se enlazan ni se indexan | — |
| `_meta/` | Agenda de investigación, lagunas y glosario | meta |

## 3. ¿Dónde va esto?

| Lo que llega | Se guarda en `raw/` | Se escribe en `wiki/` |
|---|---|---|
| Artículo o página web | `articulos/` | `14-fuentes/` y los temas que toque |
| Informe en PDF | `informes/` | `14-fuentes/` y los temas que toque |
| Video o podcast | `transcripciones/` | `14-fuentes/`; las lecciones de formato van a `07-marketing-canales/youtube.md` |
| Apuntes de un curso | `cursos/` | `14-fuentes/` y la página del bloque en `11-conocimiento-ia/` |
| Entrevista a un empresario | `entrevistas/` (anonimizada) | `02-demanda-clientes/entrevista-…` |
| Material de un competidor | `competencia/` | `03-competencia/competidor-…` |
| Norma o concepto legal | `legal/` | `14-fuentes/`, `06-administracion-legal/` y `12-entidades/` |
| Persona, empresa, institución o herramienta | — | `12-entidades/` |
| Idea que se usa en varias páginas | — | `13-conceptos/` |
| Respuesta que vale más que el chat | — | `15-analisis/` |
| Decisión del fundador | — | `16-decisiones/dec-NNN-…` y el registro de decisiones |
| Dato que falta o afirmación sin confirmar | — | `_meta/lagunas.md` y un recuadro «Por verificar» |
| Término nuevo | — | `_meta/glosario.md` |
| Idea de contenido | — | `07-marketing-canales/sistema-de-contenido.md` |

## 4. Qué se actualiza junto

| Si haces esto | Actualiza también |
|---|---|
| Crear una página en `wiki/` | `index.md` (entrada y contador de páginas), un enlace desde otra página y `log.md` |
| Ingerir una fuente | El archivo en `raw/`, su página en `14-fuentes/` con la nota de fiabilidad, los temas, entidades y conceptos afectados, `index.md` (contador de fuentes), `_meta/lagunas.md` y `log.md` |
| Cambiar una regla | `Cerebro/AGENTS.md` (y su historial), `PROMPT-MAESTRO.md` y una entrada `schema` en `log.md`. Si la regla es de Git, también `opencode.jsonc`. Avisa de que el manual quedó desactualizado |
| Cambiar de fase | El bloque de fase de `AGENTS.md`, la decisión en `16-decisiones/`, la agenda de investigación y la hoja de ruta |
| Añadir, mover o quitar una carpeta o un archivo de la raíz o de `Cerebro/` | Esta skill (tablas y `mapa.py`), la sección 4 de `PROMPT-MAESTRO.md` y, si el fundador lo pide, el manual |
| Actualizar el manual | La versión en tres sitios (cabecera, portada y pie), la tabla «Cómo se actualiza este manual», la versión citada en `index.md` y una entrada `schema` en `log.md` |

## 5. Lo que no cambia

- `raw/` es inmutable y `log.md` solo crece.
- Las reglas viven en `AGENTS.md` y en `PROMPT-MAESTRO.md`. No se escriben en `CLAUDE.md`, en esta skill ni en archivos propios de una herramienta.
- El manual es un solo archivo HTML.
- `main` no se toca: se trabaja en la rama `verificacion` y los cambios llegan por un *pull request* que une el fundador.

## 6. Antes de terminar

```bash
python3 .agents/skills/estructura-cerebro/mapa.py
python3 Cerebro/herramientas/revisar_wiki.py
```

Los dos deben terminar sin errores.
