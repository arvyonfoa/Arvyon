# Investigación web: documentación oficial de OpenCode (versión 2)

- **Fecha de captura:** 2026-11-12
- **Quién la hizo:** el agente, a pedido del fundador (migración del cerebro de Claude Code a OpenCode).
- **Método:** lectura de las páginas oficiales de `opencode.ai/docs` con una herramienta que resume cada página. Las frases entre comillas son citas literales cortas en inglés; el resto es resumen. No se instaló ni se probó OpenCode.
- **Límite:** la documentación cambia a menudo. Todo lo de aquí vale para el 2026-11-12.

## 1. Índice de la documentación · https://opencode.ai/docs/llms.txt
- El índice corresponde a **OpenCode V2**. Secciones: Docs (Intro, Config, Migrate from V1, Troubleshooting), Configure (Agents, Models, Skills, Commands, Plugins, Providers, Web search, Network, Snapshots, Compaction, Tools, MCP servers, Permissions, Policies, Instructions…), CLI (TUI, Settings, Web, Providers, Commands, ACP, Keybinds…), Build, API y Console (Models, Providers, Go, Workspaces, Budgets, Billing, Harnesses).
- **No hay ninguna página de GitHub en el índice de V2.**

## 2. Introducción · https://opencode.ai/docs/
- OpenCode es un agente de programación de código abierto.
- Formas de uso: terminal (CLI), aplicación de escritorio (Desktop), web (con `opencode pair`) y Docker.
- Escritorio: «Download the latest OpenCode Desktop build for your platform.» macOS (Apple silicon e Intel, .dmg), Windows (x64 y ARM64, .exe), Linux (.deb, .rpm, AppImage).
- Instalación de la CLI:
  - `curl -fsSL https://opencode.ai/v2/install | bash`
  - `brew install anomalyco/tap/opencode-v2`
  - `npm install -g @opencode/cli`
  - también Bun, pnpm, Yarn, AUR (`paru -S opencode-beta`) y mise (`mise use -g opencode`; mise 2026.10.9 o posterior, las versiones anteriores instalan OpenCode 1).
- Windows: «Windows package managers are not supported.» Se ofrecen binarios independientes en .zip (ARM64, x64 y x64 baseline).
- Web: «Access the OpenCode web interface with the `opencode pair` command.» Los enlaces «work once and expire in 5 minutes».
- Proveedores: se conectan desde la interfaz con `/connect`.
- OpenCode Go: «a $10/month subscription plan that grants you access to the best coding models.» OpenCode Console: acceso a los modelos recomendados (`opencode.ai/console`).
- La página no indica el número de versión vigente; un ejemplo de Docker usa la etiqueta `2.0.0` y la página de comandos menciona `2.0.21`.

## 3. Instrucciones (AGENTS.md) · https://opencode.ai/docs/instructions/
- «OpenCode V2 recognizes `AGENTS.md` only. It does not use `CLAUDE.md` as a fallback.»
- Carga «every `AGENTS.md` from the current workspace directory toward the home directory». Si la carpeta de trabajo está fuera de la carpeta personal, se detiene en la raíz del proyecto.
- Subcarpetas: «Reading a file or listing a directory loads any `AGENTS.md` files between that target and the workspace.»
- Archivo global: `~/.config/opencode/AGENTS.md`.
- «OpenCode combines the files and does not resolve conflicts between them.»
- `OPENCODE_DISABLE_PROJECT_CONFIG=1` omite los `AGENTS.md` del proyecto sin desactivar el global.
- El campo `instructions` de `opencode.jsonc` carga archivos adicionales (rutas, patrones o URL) después de los `AGENTS.md`.

## 4. Reglas en la versión 1 · https://opencode.ai/docs/rules/
- En V1, `CLAUDE.md` se usaba como respaldo cuando no existía `AGENTS.md`. Esa compatibilidad se desactivaba con `OPENCODE_DISABLE_CLAUDE_CODE=1`.
- El comando `/init` creaba o actualizaba `AGENTS.md`. (No se confirmó `/init` en la documentación de V2.)

## 5. Migrar de V1 a V2 · https://opencode.ai/docs/migrate-v1/
- V1 y V2 usan el mismo comando `opencode`; el instalador de V2 reemplaza el binario de V1.
- V2 lee la configuración de V1 en las mismas ubicaciones. Cambios de nombres: `provider` → `providers`, `agent` → `agents`, `command` → `commands`, `snapshot` → `snapshots`, `plugin` → `plugins`.
- Los permisos pasan a una lista ordenada `permissions`; las acciones cambian (`bash` → `shell`, `write`/`patch` → `edit`).
- V2 solo descubre `AGENTS.md`: si una configuración de V1 dependía de `CLAUDE.md`, hay que pasar esas instrucciones a `AGENTS.md`.
- La guía no menciona la integración con GitHub.

## 6. Configuración · https://opencode.ai/docs/config/
- Archivos: `opencode.json` u `opencode.jsonc`. Esquema: `https://opencode.ai/config.json`.
- Ubicaciones: global `~/.config/opencode/opencode.json(c)`; proyecto `opencode.json(c)` en la carpeta del proyecto o `.opencode/opencode.json(c)`; gestionada por el sistema (`/etc/opencode`, `/Library/Application Support/opencode`, `%ProgramData%\opencode`).
- Las claves se pueden referenciar con `{env:NOMBRE}` o `{file:ruta}`. La página no dice en qué ruta guarda OpenCode las credenciales.

## 7. Permisos · https://opencode.ai/docs/permissions/
- Cada regla tiene `action`, `resource` y `effect` (`allow`, `deny`, `ask`). «The last matching rule wins.»
- Política base (para todos los agentes): `{ "action": "*", "resource": "*", "effect": "allow" }`, más `ask` para leer archivos `.env`. Es decir: **por defecto se permite casi todo sin preguntar**.
- Acciones: `read`, `edit`, `glob`, `grep`, `shell`, `subagent`, `skill`, `question`, `webfetch`, `websearch`, `external_directory`, herramientas MCP, entre otras.
- Para `shell`, el recurso es el comando. Ejemplos de la página: `{ "action": "shell", "resource": "git push *", "effect": "deny" }`, `{ "action": "shell", "resource": "rm *", "effect": "deny" }`. Un patrón que termina en ` *` también cubre el comando sin argumentos.
- Ante un `ask`, el cliente ofrece: permitir una vez, permitir siempre (guarda el patrón para el proyecto) o rechazar. Lo guardado nunca anula un `deny`.

## 8. Proveedores · https://opencode.ai/docs/providers/
- «Run `/connect`, choose a provider, and enter its credentials.» Después, `/models`.
- GitHub Copilot: `/connect` → GitHub Copilot → «Login with GitHub Copilot» (flujo de dispositivo, sin clave de API). «The connected account needs Copilot Chat access.»
- OpenAI: se puede usar un plan ChatGPT Plus o Pro con «Sign in with ChatGPT». «Usage counts against your plan, so these models show no cost.»
- OpenCode Go: suscripción opcional; la clave se obtiene en la consola y se conecta como «OpenCode Go».
- Anthropic: la página no tiene sección de inicio de sesión; no dice si se puede usar una suscripción Claude Pro o Max.

## 9. Interfaz de terminal · https://opencode.ai/docs/cli/tui/
- Se inicia con `cd carpeta-del-proyecto` y `opencode`.
- Comandos: `/models`, `/new`, `/sessions`, `/agents`, `/undo` («revert the latest user message and the work that followed it»), `/redo`, `/editor`, `/btw <pregunta>`. `Ctrl+P` abre la paleta de comandos.
- `@` adjunta un archivo; `!` al inicio de un mensaje vacío ejecuta un comando de terminal. `Shift+Tab` cambia de agente.

## 10. Comandos de la CLI · https://opencode.ai/docs/cli/commands/
- Subcomandos: `run`, `mini`, `session`, `auth` («Manages AI providers and credentials»; `list`, `login`, `logout`, `switch`, `export`, `import`), `models`, `mcp`, `plugin`, `stats`, `serve`, `pair`, `service`, `reload`, `api`, `acp`, `debug`, `upgrade` (alias `update`), `uninstall`.
- **No existe `opencode github` en esta página.** Hay un ejemplo de GitHub Actions que revisa un *pull request* con `opencode run --standalone`, instalando `@opencode/cli` y pasando la clave del proveedor como secreto: «In CI, pass a provider API key as a secret and use standalone mode so the private server receives it.»

## 11. Instantáneas · https://opencode.ai/docs/snapshots/
- «Snapshots let you undo recent conversation and file changes together.» «Filesystem snapshots require a Git repository.»
- No crean commits ni mueven ramas. Se guardan en una base interna dentro de la carpeta de datos de OpenCode.
- Los efectos de los comandos de terminal pueden no revertirse. Se desactivan con `"snapshots": false`.

## 12. Integración con GitHub (documentación de la versión 1) · https://opencode.ai/docs/github/
- La página avisa de que documenta **OpenCode V1** y remite al índice de V2.
- `opencode github install` guía la instalación de la app de GitHub (`github.com/apps/opencode-agent`), crea `.github/workflows/opencode.yml` y configura los secretos.
- Se activa al escribir `/opencode` o `/oc` en un comentario de un *issue* o de un *pull request*. Puede explicar un *issue*, crear una rama y abrir un *pull request*, o aplicar un cambio en un *pull request* existente.
- La clave del proveedor de IA va en *Settings → Secrets and variables → Actions* del repositorio.

## Lo que no se pudo confirmar
- Si `opencode github install` y la app `opencode-agent` siguen funcionando con la versión 2.
- En qué ruta guarda OpenCode las credenciales.
- Si OpenCode permite usar una suscripción personal de Claude.
- Si `/init` existe en la versión 2.
