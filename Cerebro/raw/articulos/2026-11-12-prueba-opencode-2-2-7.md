# Prueba de OpenCode 2.2.7 sobre este repositorio

- **Fecha:** 2026-11-12
- **Quién la hizo:** el agente, en la máquina temporal de la sesión en la nube (Linux), para verificar la migración.
- **Qué se instaló:** el paquete `@opencode/cli` del registro de npm, versión **2.2.7** (repositorio `github.com/anomalyco/opencode`), en una carpeta temporal fuera del repositorio.
- **Qué no se hizo:** no se conectó ningún modelo de IA ni se envió ningún mensaje. No se probó una conversación real, ni la aplicación de escritorio, ni Windows o macOS.
- **Cómo se consultó:** con los comandos `opencode --help`, `opencode debug paths`, `opencode debug agents` y con un servidor local (`opencode serve`) al que se le preguntó por sus skills, agentes, comandos y permisos.

## Resultados

### 1. Instrucciones (`AGENTS.md`)
- Al abrir OpenCode en `Arvyon/Cerebro`, el registro del programa muestra que vigila tres archivos: el global `~/.config/opencode/AGENTS.md`, `Arvyon/Cerebro/AGENTS.md` y `Arvyon/AGENTS.md`.
- `CLAUDE.md` no aparece ni una vez en el registro: OpenCode 2.2.7 no lo lee.
- Límite: no se vio el texto que recibe el modelo, porque eso exige enviar un mensaje a un modelo.

### 2. Skill `estructura-cerebro`
- OpenCode la lista con la ruta `.agents/skills/estructura-cerebro/SKILL.md`, tanto abierto en la raíz del repositorio como en `Cerebro/`.
- Si existe a la vez una copia en `.opencode/skills/`, gana esa. La de `.agents/skills/` gana a la de `.claude/skills/`.
- Las skills tardan unos segundos en cargarse al arrancar: una consulta hecha en el primer segundo devuelve la lista vacía o incompleta.
- OpenCode trae skills propias: `opencode` (documentación del programa), `report` y `browser`.

### 3. Permisos
- Sin archivo de configuración, el agente `build` tiene `{ "action": "*", "resource": "*", "effect": "allow" }` y solo pregunta antes de leer archivos `.env`.
- Con el archivo `opencode.jsonc` de la raíz, las cinco reglas (`git push *` → preguntar; `git push origin main *`, `git push --force *`, `git push -f *` y `gh pr merge *` → denegar) aparecen en los permisos del agente `build`, en ese orden y después de la regla general. Se aplican igual abierto en la raíz que en `Cerebro/`. El archivo admite comentarios.
- Un archivo con un valor inválido (`"effect": "quizas"`) no se aplica y deja un aviso en el registro.
- Límite: no se comprobó qué comandos reales coinciden con cada patrón, porque eso exige que un modelo ejecute comandos.
- La opción `--auto` de la línea de comandos aprueba sola todo lo que no esté denegado.

### 4. Comandos y agentes
- Comandos del proyecto: `/init` («guided AGENTS.md setup»), `/review` y `/goal`.
- Agentes visibles: `build` (el normal) y `plan` («Read-only agent for exploring the codebase and planning work before implementation»).
- Subcomandos de la línea de comandos: `upgrade`, `uninstall`, `acp`, `api`, `debug`, `auth`, `mcp`, `plugin`, `models`, `stats`, `mini`, `run`, `session`, `service`, `reload`, `pair`, `serve`. **No existe `opencode github`.**
- `opencode auth`: `list`, `login`, `logout`, `export`, `import`, `switch`.

### 5. Dónde guarda sus datos
- `opencode debug paths` muestra las carpetas. En Linux: datos en `~/.local/share/opencode` (con la base `opencode.db`), configuración en `~/.config/opencode`, caché en `~/.cache/opencode`. En otros sistemas las rutas pueden cambiar: hay que ejecutar el comando.
- OpenCode no creó ningún archivo dentro del repositorio durante la prueba.

## Lo que sigue sin comprobarse
- Una conversación real con un modelo: que el agente siga las reglas, cargue la skill por su cuenta y respete los permisos al ejecutar comandos.
- La aplicación de escritorio y el funcionamiento en el sistema operativo del fundador.
- Si OpenCode admite una suscripción personal de Claude.
