# AGENTS.md (raíz del repositorio)

Este repositorio es de **Arvyon**, una consultora de IA. El trabajo vive en la carpeta **`Cerebro/`**: un segundo cerebro (wiki mantenida por un LLM). Estas instrucciones valen para cualquier agente (OpenCode, Claude Code, Codex, Pi…).

Antes de hacer cualquier cosa:
1. Lee completo `Cerebro/AGENTS.md`: tiene las reglas, la fase vigente del proyecto y la forma de trabajar con Git y GitHub.
2. Trabaja dentro de `Cerebro/`. El contexto completo está en `Cerebro/PROMPT-MAESTRO.md`.
3. No modifiques `Cerebro/raw/`: son las fuentes originales (ahí está también la presentación para socios). Solo se añaden archivos nuevos.
4. No hagas commits ni push a `main`. Trabaja en la rama `verificacion`; los cambios llegan a `main` por un *pull request* que une el fundador.

Si dudas de dónde va algo, carga la skill `estructura-cerebro` (`.agents/skills/estructura-cerebro/SKILL.md`): es el mapa de todo el repositorio. Su script `mapa.py` muestra la estructura real.

`opencode.jsonc` son los permisos de OpenCode para este repositorio: pregunta antes de cada `git push` y deniega subir a `main`, el *force push* y unir *pull requests*.

El manual para humanos está en `Cerebro/manual/manual-cerebro-arvyon.html` (un solo archivo HTML).

Los archivos `CLAUDE.md` (aquí y en `Cerebro/`) no tienen reglas propias: solo importan el `AGENTS.md` de su carpeta para Claude Code.
