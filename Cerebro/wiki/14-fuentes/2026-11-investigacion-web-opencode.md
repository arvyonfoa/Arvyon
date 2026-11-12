---
tipo: fuente
area: operacion
estado: borrador
confianza: media
resumen: "Documentación oficial de OpenCode versión 2 (2026-11-12): solo lee AGENTS.md, permite casi todo por defecto, se conecta a modelos con /connect y su integración con GitHub está documentada para la versión 1."
fuentes: []
creado: 2026-11-12
actualizado: 2026-11-12
revisar_antes: 2027-02-12
etiquetas: [herramienta, agentes]
---

# Investigación web: documentación oficial de OpenCode (versión 2)

## Ficha
| Campo | Valor |
|---|---|
| Autor / institución | Equipo de OpenCode (documentación oficial) |
| Medio | Web: `opencode.ai/docs` |
| Fecha de captura | 2026-11-12 |
| Archivo en raw/ | [[2026-11-12-investigacion-web-opencode]] (`raw/articulos/`) |
| Tipo | investigación web agrupada (12 páginas) |
| Idioma | inglés |
| Fiabilidad (2–5) | 4 — motivo: documentación técnica del proveedor sobre su propia herramienta (tope de 4); cambia a menudo |
| Universo / muestra | No aplica |

## Resumen en 5 líneas
OpenCode es un agente de código abierto que funciona en el computador del usuario, en la terminal o en una aplicación de escritorio. La versión 2 solo lee `AGENTS.md` y ya no usa `CLAUDE.md` como respaldo. Por defecto permite casi todas las acciones sin preguntar. Los modelos se conectan con `/connect`. La integración con GitHub (`opencode github install`) está documentada para la versión 1; en la versión 2 solo aparece un ejemplo de GitHub Actions.

## Ideas clave
1. **Solo `AGENTS.md`.** «OpenCode V2 recognizes `AGENTS.md` only. It does not use `CLAUDE.md` as a fallback.» Por eso el esquema del cerebro pasó a `AGENTS.md`.
2. **Carga varios `AGENTS.md`.** Lee todos los que hay desde la carpeta de trabajo hacia arriba y los combina sin resolver contradicciones.
3. **Permisos abiertos por defecto.** La política base permite todo, salvo leer archivos `.env`, que pregunta. Las restricciones se escriben en `opencode.jsonc`.
4. **Modelos con `/connect`.** Admite OpenCode Go (10 USD al mes), un plan ChatGPT Plus o Pro, GitHub Copilot y claves de API de otros proveedores.
5. **Deshacer con `/undo`.** Revierte el último mensaje y sus cambios en archivos, si la carpeta es un repositorio Git. No crea commits.
6. **GitHub.** En el computador, OpenCode usa el Git ya instalado. La integración que responde a `/oc` dentro de GitHub está documentada para la versión 1.

## Datos y cifras
| Dato | Valor | Universo y año | Página |
|---|---|---|---|
| Precio de OpenCode Go | 10 USD al mes | Precio público, 2026-11-12 | Introducción |
| Caducidad del enlace de `opencode pair` | 5 minutos, un solo uso | 2026-11-12 | Introducción |
| Archivo global de instrucciones | `~/.config/opencode/AGENTS.md` | 2026-11-12 | Instrucciones |

> [!question] Por verificar
> El precio está en dólares. No se convirtió a EUR ni a COP: hay que hacerlo con la tasa del día en que se contrate ([[cobros-y-cambio]]).

## Qué cambia en la wiki
- [[opencode]]: página nueva de la herramienta.
- [[stack-herramientas]]: el agente del cerebro pasa a ser OpenCode, con Claude Code como alternativa.
- [[arnes-de-agentes]]: la guía del cerebro es ahora `AGENTS.md`.
- [[lagunas]]: cuatro puntos por verificar.

## Contradicciones con la wiki
> [!warning] Contradicción · versiones de la documentación
> La página de reglas (versión 1) dice que `CLAUDE.md` se usa como respaldo. La página de instrucciones (versión 2) dice que no. Manda la versión 2, que es la que se instala hoy.

## Preguntas que abre
- [ ] ¿Funciona `opencode github install` con la versión 2?
- [ ] ¿Dónde guarda OpenCode las credenciales?
- [ ] ¿Se puede usar una suscripción personal de Claude dentro de OpenCode?
- [ ] ¿Existe `/init` en la versión 2?

## Conexiones
- [[opencode]]: la herramienta que describe.
- [[stack-herramientas]]: dónde encaja en las herramientas internas.
- [[arnes-de-agentes]]: `AGENTS.md` y los permisos son piezas del arnés.
- [[pi-coding-agent]]: otro agente de código abierto ya descrito en la wiki.
- [[lagunas]]: lo que quedó por verificar.
