# Investigación web: skills en OpenCode (versión 2)

- **Fecha de captura:** 2026-11-12
- **URL:** https://opencode.ai/docs/skills/
- **Quién la hizo:** el agente, para decidir dónde guardar la skill `estructura-cerebro`.
- **Método:** lectura de la página oficial con una herramienta que la resume. Las frases entre comillas son citas literales cortas. No se probó en OpenCode.
- **Complementa a:** `2026-11-12-investigacion-web-opencode.md`.

## Dónde busca las skills
- Globales: `~/.config/opencode/skills`. Por compatibilidad, también `~/.claude/skills` y `~/.agents/skills`.
- De proyecto: `.opencode/skills`. Por compatibilidad, también `.claude/skills` y `.agents/skills`.
- Para las de proyecto busca «from the current directory up to the project root» e incluye las carpetas que encuentra en cada nivel.
- Acepta archivos `*.md` en la raíz de la carpeta de skills o archivos llamados `SKILL.md` dentro de una subcarpeta. Omite carpetas ocultas y `node_modules`.
- Fuentes adicionales: la lista `skills` de `opencode.json` u `opencode.jsonc`.

## Formato de SKILL.md
- El identificador lo da la ruta (el nombre de la carpeta), no el campo `name`.
- `description`: resumen que ve el modelo. Sin descripción, la skill no se anuncia.
- Recomendación para skills portables: nombre en minúsculas con guiones, de 1 a 64 caracteres, igual al nombre de la carpeta.
- `disable-model-invocation: true` oculta la skill de la lista del modelo.

## Cómo se cargan y se invocan
- En cada paso el modelo ve solo el identificador, el nombre y la descripción. «The model loads a skill by calling the `skill` tool with its exact ID». El cuerpo se carga solo entonces.
- A mano, con `@identificador` en el mensaje. La página no menciona una forma con barra.
- Archivos de apoyo (scripts, plantillas): se admiten, con rutas relativas a la carpeta de `SKILL.md`. «Supporting file contents are not loaded automatically.»

## Permisos y precedencia
- Acción `skill`, con el identificador como recurso: `allow`, `ask` o `deny`.
- Si dos orígenes definen el mismo identificador, gana el registrado después. De menor a mayor prioridad: integradas, `.claude/skills`, `.agents/skills`, `~/.config/opencode/skills`, `.opencode/skills` del proyecto y las entradas de `skills` de la configuración.

## Lo que no se pudo confirmar
- Que OpenCode siga leyendo `.agents/skills` y `.claude/skills` en versiones futuras: la página las llama carpetas de compatibilidad.
- Cómo descubre Claude Code las skills: no se consultó su documentación; se usó la carpeta `.claude/skills/`, que es la que usa esta sesión.
