---
tipo: entidad
area: operacion
estado: borrador
confianza: media
resumen: "Agente de código abierto que funciona en el computador del usuario; desde el 2026-11-12 es el agente con el que se mantiene este cerebro, con Claude Code como alternativa."
fuentes: ["[[2026-11-investigacion-web-opencode]]"]
creado: 2026-11-12
actualizado: 2026-11-12
revisar_antes: 2027-02-12
etiquetas: [herramienta, agentes]
---

# OpenCode

## Qué es
OpenCode es un agente de código abierto que lee y escribe archivos, ejecuta comandos y usa Git en el computador de quien lo usa. Se maneja desde la terminal o desde una aplicación de escritorio. No trae un modelo propio: se conecta al proveedor que elija el usuario ([[2026-11-investigacion-web-opencode]]).

## Datos básicos
| Campo | Valor |
|---|---|
| Tipo | herramienta |
| Web oficial | https://opencode.ai/ |
| Versión vigente | 2.2.7 el 2026-11-12 (la que se probó sobre este repositorio) |
| Dónde funciona | En el computador del usuario: terminal, aplicación de escritorio (macOS, Windows y Linux) o navegador con `opencode pair` |
| Qué instrucciones lee | Solo `AGENTS.md`. La versión 2 no usa `CLAUDE.md` como respaldo |
| Permisos por defecto | Permite casi todo sin preguntar; solo pregunta antes de leer archivos `.env`. En este repositorio los ajusta `opencode.jsonc` |
| Modelos | Se conectan con `/connect`: OpenCode Go (10 USD al mes), plan ChatGPT Plus o Pro, GitHub Copilot o claves de API |
| Deshacer | `/undo` y `/redo`; restaura archivos si la carpeta es un repositorio Git |
| Skills | Las busca en `.opencode/skills` y, por compatibilidad, en `.agents/skills` y `.claude/skills`. La del cerebro es `estructura-cerebro`, en `.agents/skills/` |

## Diferencias con Claude Code en la nube
| | Claude Code en la nube | OpenCode |
|---|---|---|
| Dónde trabaja | En una máquina temporal | En el computador del fundador |
| Qué lee | `CLAUDE.md` | `AGENTS.md` |
| Acceso a GitHub | La app de Claude y un proxy | El Git y la cuenta de GitHub del computador |
| Claves | Secretos de red del entorno | `/connect`, guardadas en el computador |
| Protecciones | Rama asignada y *force push* bloqueado | Las que se escriban en `AGENTS.md` y en `opencode.jsonc` |

> [!note] Hecho
> Como la herramienta ya no impone la rama ni bloquea el *force push*, esas reglas pasaron al esquema: están en la sección «Git y GitHub» de `AGENTS.md` ([[2026-11-investigacion-web-opencode]]).

## Riesgos
- **Permite casi todo por defecto.** Por eso el repositorio trae un `opencode.jsonc` que pregunta antes de cada `git push` y deniega subir a `main`, el *force push* y unir *pull requests*. La opción `--auto` aprueba sola todo lo que no esté denegado: no conviene usarla.
- **`/init` propone reescribir `AGENTS.md`.** El esquema ya está escrito; no hace falta ejecutarlo.
- **El trabajo queda en el disco hasta que se sube.** Si no se hace commit y push, GitHub no lo tiene.
- **Dos copias del cerebro.** Si se alterna con Claude Code, hay que hacer `git pull` antes de empezar en cada sitio.

> [!note] Hecho · probado en la versión 2.2.7
> Abierto en `Cerebro/`, OpenCode vigila los dos `AGENTS.md`, encuentra la skill `estructura-cerebro` y aplica `opencode.jsonc`. No trae el comando `opencode github`. La prueba se hizo sin conectar un modelo ([[2026-11-investigacion-web-opencode]]).

> [!question] Por verificar
> Una conversación real con un modelo; la aplicación de escritorio en el sistema del fundador; y si OpenCode admite una suscripción personal de Claude ([[lagunas]]).

## Relevancia para Arvyon
Es la herramienta con la que el fundador mantiene el cerebro desde el 2026-11-12. No es un producto que Arvyon venda ni un tema del currículo de la Fase 1. Sirve, además, como ejemplo cercano de un [[arnes-de-agentes]]: instrucciones (`AGENTS.md`), permisos y deshacer. El paso a paso para instalarlo y conectarlo con GitHub está en el capítulo 7 del manual.

## Menciones
- [[2026-11-investigacion-web-opencode]]: documentación oficial leída el 2026-11-12.

## Conexiones
- [[stack-herramientas]]: forma parte de las herramientas internas.
- [[arnes-de-agentes]]: el cerebro es un arnés y OpenCode es el agente que lo usa.
- [[pi-coding-agent]]: otro agente de código abierto, más minimalista.
- [[2026-11-investigacion-web-opencode]]: la fuente.
- [[lagunas]]: lo que falta verificar.
