# Investigación web: fábricas de IA, arneses de agentes, Pi y enrutamiento de modelos

- Fecha de captura: 2026-11-11
- Objetivo: contrastar lo que afirma el video de Eric Risco «Programar con agentes ya no basta: monta tu Software Factory» y averiguar qué son el *harness engineering* con Pi y la disciplina de elegir modelo y nivel de razonamiento para gastar menos.
- Método: búsqueda web y lectura de las páginas indicadas. Es un resumen de lo que decían las páginas en esa fecha. Cuando un dato llegó por una fuente secundaria, se indica.
- Capturado por: el agente, a pedido del fundador.
- Límite general: la página original de OpenAI devolvió un error 403 a la lectura automática; sus datos vienen de InfoQ y de resúmenes de búsqueda.

## 1. Fábricas de software con agentes

### Stripe, «Minions: Stripe's one-shot, end-to-end coding agents»
- URL: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- Fecha y autor: 2026-02-09, Alistair Gray. Fuente primaria.
- Dice: más de mil *pull requests* integrados cada semana en Stripe son producidos por completo por «minions» («Over a thousand pull requests merged each week»). Los revisan personas, pero «they contain no human-written code».
- Las tareas se inician normalmente desde Slack (se etiqueta la aplicación en un hilo); también desde la plataforma de documentación, la de *feature flags* y la de tiques, y por interfaz web o de línea de comandos.
- La orquestación intercala «agent loops and deterministic code»: bucles de agente y código determinista (git, comprobadores de estilo, pruebas), para que los pasos obligatorios se ejecuten siempre. La página leída no usa la palabra «blueprint»; ese nombre aparece en la segunda parte y en análisis de terceros.
- Entorno: máquinas de desarrollo precalentadas («spun up in 10 seconds»), aisladas de los recursos de producción y de internet.
- Límites: un *hook* local ejecuta comprobadores en menos de cinco segundos; en la integración continua hay «at most two rounds of CI». Stripe tiene más de tres millones de pruebas. Si falla tras la segunda ronda, el proceso termina. La razón es el costo en *tokens*, cómputo y tiempo.
- Herramientas: «Toolshed», servidor MCP interno con «more than 400 MCP tools».
- Limitaciones que reconoce: trabajar sobre una base de código grande y madura es «inherently much harder»; una ejecución «not entirely correct» suele servir de punto de partida para un ingeniero.
- Dato secundario (ByteByteGo, Port, InfoQ, marzo de 2026): 1.300 PR por semana en febrero de 2026; el agente parte de una bifurcación de Goose, de Block.

### StrongDM, «Software Factory»
- URL: https://factory.strongdm.ai/
- Fecha y autor: 2026-02-06, Justin McCarthy (cofundador y director de tecnología). El equipo se fundó el 2025-07-14 con Jay Taylor y Navan Chauhan. Fuente primaria (manifiesto).
- Principios textuales: «Code **must not be** written by humans» y «Code **must not be** reviewed by humans».
- «Scenarios»: historias de usuario de extremo a extremo, «often stored outside the codebase», como un conjunto reservado (*holdout*); las valida un modelo.
- «Satisfaction»: métrica probabilística; de todas las trayectorias observadas en todos los escenarios, qué fracción probablemente satisface al usuario. Sustituye al éxito booleano («the test suite is green»).
- «Digital Twin Universe»: clones de comportamiento de los servicios de terceros de los que depende el software (Okta, Jira, Slack, Google Docs, Google Drive, Google Sheets).
- Guía de gasto: si no se han gastado al menos «$1,000 on tokens today» por ingeniero humano, la fábrica tiene margen de mejora. Es una referencia aspiracional, no un gasto medido.
- Dato secundario: Dan Shapiro propuso cinco niveles y llama al quinto «dark factory» (fábrica oscura). Stanford CodeX publicó el 2026-02-08 «Built by Agents, Tested by Agents, Trusted by Whom?» (https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/).

### OpenAI, «Harness engineering: leveraging Codex in an agent-first world»
- URL original (no se pudo leer, error 403): https://openai.com/index/harness-engineering/
- Leído a través de InfoQ, 2026-02-21, Leela Kumili: https://www.infoq.com/news/2026/02/openai-harness-engineering-codex
- Según InfoQ: experimento interno de cinco meses; una beta de producto; cerca de un millón de líneas sin código escrito a mano; «un equipo pequeño». Los agentes de Codex escriben código, pruebas, configuración de integración continua, documentación y observabilidad. La documentación vive en un directorio estructurado que es la fuente única de verdad para los agentes. Las capas de arquitectura se hacen cumplir con reglas mecánicas y pruebas estructurales.
- Según resúmenes de búsqueda (sin verificar en el original): publicado el 2026-02-11 por Ryan Lopopolo; primer commit a finales de agosto de 2025; unos 1.500 PR; 3,5 PR por ingeniero y día; un `AGENTS.md` corto, de unas 100 líneas, que funciona como mapa.
- Cita de Martin Fowler (LinkedIn, vía InfoQ): el arnés incluye «context engineering, architectural constraints, and garbage collection».

### Repositorios de terceros basados en el video (fiabilidad baja)
- https://github.com/mieresantonio/fabrica-de-software : su archivo `flujo-paralelo.md` reconstruye el diagrama del video (parte 6, «En paralelo») a partir de una captura: entrada → spec writer → builder → seguridad, UX, UI y código en paralelo → approver → puerta humana → main o PR → producción. Atribuye los modelos así: builder Opus 5.5; seguridad, UX y UI «ChatGPT Sol y Astra»; código Sonnet 5.5.
- https://github.com/DOKK-droid/ai-factory : implementación sobre OpenCode «siguiendo la arquitectura del video». Una máquina de estados de solo lectura (`next-step.sh`) decide el orden de los pasos, no un prompt; `launch-reviewers.sh` lanza los cuatro revisores; `max_rounds` limita las vueltas; hay una parada `HUMAN_CONFIRM_SPEC`.
- https://github.com/ericrisco/rsc-harness : 586 estrellas el 2026-11-11; licencia MIT; se describe como «meta-harness» para Claude Code, Codex y 15 asistentes más. En esa fecha no había ningún repositorio público «rsc-factory» en la cuenta del autor.

## 2. *Harness engineering*

### Birgitta Böckeler, «Harness engineering», martinfowler.com
- URL: https://martinfowler.com/articles/harness-engineering.html
- Fecha: 2026-04-02 (nota breve el 2026-02-17). Autora: Distinguished Engineer en Thoughtworks.
- El arnés es «everything in an AI agent except the model itself». La fórmula «Agent = Model + Harness» aparece enlazada a un artículo del blog de LangChain.
- Un buen arnés aumenta «the probability that the agent gets it right in the first place» y corrige antes de la revisión humana.
- Guías (*feedforward*): orientan antes de que el agente actúe. Sensores (*feedback*): observan después y permiten corregir.
- Computacional (determinista y rápido: pruebas, comprobadores de estilo y de tipos) frente a inferencial (análisis semántico, revisión con IA, «LLM as judge»: más lento, más caro, menos determinista).
- Tres categorías de regulación: mantenibilidad (la más fácil hoy), arquitectura (*fitness functions*) y comportamiento, «the elephant in the room». Sobre las pruebas generadas por IA: «that's not good enough yet».
- Papel humano: dirigir iterando sobre el arnés; el objetivo no es eliminar la intervención humana sino «to direct it to where our input is most important».
- Preguntas abiertas: «If sensors never fire, is that a sign of high quality or inadequate detection mechanisms?»; falta una forma de evaluar la cobertura y la calidad de un arnés.

### Naresh Jain, «Are Harnesses Worth the Cost?», martinfowler.com
- URL: https://martinfowler.com/articles/are-harnesses-worth-the-cost.html
- Fecha: 2026-10-13. Serie «Exploring Gen AI».
- Medias de 10 ejecuciones; costos estimados equivalentes a API, no facturados:

| Modelo | Arnés | Tokens | Tiempo | Costo | Aceptadas |
|---|---|---|---|---|---|
| GPT-6 Sol | Sí | 11.331.970 | 19 min 53 s | ~2,679 USD | 10/10 |
| GPT-6 Sol | No | 1.076.371 | 6 min 51 s | ~0,406 USD | 10/10 |
| GPT-6 Luna | Sí | 22.933.648 | 35 min | ~0,273 USD | 10/10 |
| GPT-6 Luna | No | 5.860.736 | 15 min 56 s | ~0,086 USD | 3/10 |

- Con Sol, el arnés usó unas 10,5 veces más tokens, casi 3 veces más tiempo y unas 7 veces más costo, sin mejorar la aceptación. Luna con arnés costó alrededor de un 33 % menos que Sol sin arnés.
- Tesis: «A behavioral harness is not an automatic win for every model on every task». Con modelos capaces basta una verificación independiente al final; con modelos de resultados inconsistentes los sensores deben correr durante el desarrollo.
- Límites que reconoce: un único servicio nuevo en Java, un encargo muy completo, razonamiento bajo, muestra pequeña; no mide el esfuerzo de escribir y mantener el arnés.

### Curso «Learn Harness Engineering» (walkinglabs)
- URL: https://github.com/walkinglabs/learn-harness-engineering (versión en español en `docs-readme/es-ES/README.md`).
- 14 lecciones, 8 proyectos sobre una aplicación de escritorio y una biblioteca de plantillas. Desde agosto de 2026 incluye cuatro análisis de arneses de producción: Pi, Claude Code, Codex y DeepSeek.
- Define el arnés con cinco subsistemas: instrucciones, estado, verificación, alcance y ciclo de vida de la sesión.
- Requisitos: terminal, git, leer y escribir código, y un agente de programación.
- Capítulo sobre Pi (`docs/es/harness-designs/pi/index.md`): núcleo mínimo y extensiones programables; compactación automática que conserva unos 20.000 tokens recientes; sesiones en árbol; carga de habilidades bajo demanda; Pi no trae un control de pruebas obligatorio.

## 3. Pi

### Sitio oficial
- URL: https://pi.dev/ (leído el 2026-11-11). Lo mantiene «Earendil Inc. y colaboradores». Licencia MIT. Lema: «There are many agent harnesses but this one is yours».
- Se define como «minimal agent harness». No incluye subagentes, ventanas de permiso, modo plan, lista de tareas ni procesos en segundo plano.
- MCP: el sitio dice «No MCP» tachado y «Now with MCP+Codemode: MCP is built in, and Codemode lets agents compose tool calls in a JavaScript sandbox. MCP extensions are still supported too.»
- Extensiones en TypeScript (subagentes, modo plan, control de permisos, protección de rutas, SSH, aislamiento). Habilidades cargadas bajo demanda. Plantillas de instrucciones. Paquetes por npm o git.
- Más de 15 proveedores de modelos; autenticación por clave de API u OAuth. Modos: interactivo, impresión/JSON, RPC y SDK. Sesiones en árbol. Compactación automática. Lee `AGENTS.md` y `SYSTEM.md`.

### Mario Zechner, «What I learned building an opinionated and minimal coding agent»
- URL: https://www.mariozechner.at/posts/2025-11-30-pi-coding-agent/
- Fecha: 2025-11-30. Fuente primaria (el creador).
- Motivo: quería un agente más simple y predecible que Claude Code, que según él se había vuelto «a spaceship». Filosofía: «if I don't need it, it won't be built».
- Cuatro paquetes: pi-ai, pi-agent-core, pi-tui y pi-coding-agent. Cuatro herramientas por defecto: `read`, `write`, `edit` y `bash`. Las instrucciones de sistema y las definiciones de herramientas quedan «below 1000 tokens».
- Sin permisos por defecto: considera las medidas de otros agentes «mostly security theater». Sin MCP en esa fecha (un servidor MCP de Playwright ocupa «13.7k tokens»). Subagentes: «a black box within a black box».
- Dato secundario: el proyecto pasó a Earendil en abril de 2026 (entrada «I've sold out», 2026-04-08); los paquetes usan ahora el prefijo `@earendil-works`.

### Fazt, tutorial de Pi en español
- URL: https://fazt.dev/contenido/pi-agent-tutorial-harness-skills-extensiones-mcp
- Fecha: 2026-09-12 (actualizado el 2026-09-24).
- Instalación con guion oficial o con `npm install -g` (Node.js 22.19 o superior). `/login` admite suscripción (ChatGPT/Codex, Claude, GitHub Copilot, Kimi) o clave de API. `/model` cambia de modelo y `/thinking` ajusta el razonamiento.
- Dice que Pi no trae MCP de fábrica (contradice al sitio oficial del 2026-11-11: el cambio es posterior a la guía).
- Advierte que los paquetes pueden ejecutar código en la máquina y que Pi corre con los permisos del usuario.

### Suscripciones de Claude en herramientas de terceros
- The Register, 2026-02-20: https://www.theregister.com/software/2026/02/20/anthropic-clarifies-ban-on-third-party-tool-access-to-claude/5014546
- Dice: Anthropic revisó sus condiciones para limitar la autenticación OAuth de los planes Free, Pro y Max a Claude Code y Claude.ai. Otras notas secundarias sitúan un bloqueo técnico el 2026-01-09 y un corte general el 2026-04-04. No se leyó el texto de Anthropic.

## 4. Enrutamiento de modelos y costo

### FinOps Foundation, «Managing AI Token Costs from Direct Model Provider APIs»
- URL: https://www.finops.org/wg/token-economics-saas/
- Última actualización: 2026-10-28. Licencia CC BY 4.0.
- Tabla «Where to Start» (cifras indicativas; pide validarlas con datos propios):

| Palanca | Ahorro indicativo | Esfuerzo |
|---|---|---|
| Elegir el modelo adecuado y enrutar | 60–90 % | Medio |
| API por lotes | ~50 % | Bajo–medio |
| Caché de instrucciones | 50–90 % sobre tokens en caché | Bajo |
| Gestión del contexto | 20–60 % | Medio–alto |
| Control de la longitud de salida | 10–40 % | Bajo–medio |
| Descuentos por volumen o compromiso | 10–30 % | Bajo |

- Otros datos: el enrutamiento puede reducir el costo medio por consulta un 60–80 %; el token de salida suele costar de 3 a 5 veces el de entrada; un modelo puntero puede costar de 50 a 100 veces más por token que el más pequeño; un RAG bien hecho puede reducir los tokens de contexto un 80–95 %.
- Métricas: costo por consulta, costo por usuario activo al mes, **costo por resultado exitoso** (cuenta solo las ejecuciones que superan el umbral de calidad; las fallidas también cuestan) y costo por transacción de negocio.
- El «harness» (bases vectoriales, orquestación, cachés, observabilidad) puede ser el 40–60 % del costo total de una funcionalidad en arquitecturas RAG o agénticas.
- No da cifras para los tokens de razonamiento.

### Anthropic, «Building effective agents»
- URL: https://www.anthropic.com/engineering/building-effective-agents
- Fecha: 2024-12-19.
- Flujos (*workflows*): modelos y herramientas orquestados por «predefined code paths». Agentes: el modelo dirige su propio proceso y el uso de herramientas.
- Patrones: encadenar instrucciones, enrutar, paralelizar, orquestador con trabajadores, evaluador con optimizador.
- Sobre el enrutamiento: enviar las consultas fáciles a modelos «smaller, cost-efficient» y las difíciles a modelos «more capable».
- Consejo: «find the simplest solution possible» y «only increasing complexity when needed».

### Anthropic, herramienta «advisor»
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool y https://claude.com/blog/the-advisor-strategy (vistos a través de resultados de búsqueda).
- Un modelo ejecutor más económico decide cuándo consultar a un modelo asesor más capaz. En beta (cabecera `advisor-tool-2026-03-01`). `max_uses` limita las consultas. Anthropic recomienda comparar con el conjunto de evaluaciones propio las tres opciones: ejecutor solo, ejecutor con asesor y modelo grande solo.

### Artículos académicos (cifras vistas a través de resúmenes)
- RouteLLM, Ong y otros, 2024: https://arxiv.org/abs/2406.18665 . Resúmenes citan una reducción de costo del 85 % en MT Bench manteniendo el 95 % de la calidad de GPT-4.
- FrugalGPT, Chen, Zaharia y Zou, 2023: https://arxiv.org/abs/2305.05176 . El artículo reporta hasta un 98 % de reducción de costo en el mejor caso.

## 5. Evidencia para contrastar el video

- Panickssery, Bowman y Feng, «LLM Evaluators Recognize and Favor Their Own Generations», NeurIPS 2024: https://arxiv.org/abs/2404.13076 . Los modelos prefieren sus propios resúmenes y esa preferencia se relaciona linealmente con su capacidad de reconocerlos. Medido en resúmenes de texto, no en código.
- METR: ensayo aleatorizado de julio de 2025, desarrolladores expertos tardaron un 19 % más con IA; actualización del 2026-02-24 (https://metr.org/blog/2026-02-24-uplift-update/) no concluyente por efectos de selección. Visto a través de resúmenes.
- DORA, «State of AI-assisted Software Development 2025»: https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf . Casi 5.000 encuestados; la IA es un «amplifier»; mejora la velocidad de entrega y sigue aumentando la inestabilidad. Visto a través de resúmenes.
- «Clinejection»: Simon Willison, 2026-03-06, https://simonwillison.net/2026/Mar/6/clinejection/ ; Snyk, https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions . El flujo de clasificación de *issues* de Cline pasaba el título del *issue* al modelo sin filtrar. El 2026-02-17 se publicó sin autorización `cline@2.3.0` en npm, que instalaba OpenClaw; unas 4.000 máquinas afectadas. Divulgado por Adnan Khan el 2026-02-09.
- Simon Willison, «the lethal trifecta» (2025-06-16): datos privados, contenido no confiable y un canal de comunicación externo. Meta formuló la «Agents Rule of Two» a finales de 2025. Visto a través de resúmenes.
- OWASP, «Top 10 for Agentic Applications», 2025-12-09 (ASI01 a ASI10). Visto a través de resúmenes.
- Modelos citados en el video: «GPT-6 Astra» (https://openai.com/index/gpt-6-astra/, septiembre de 2026; OpenAI lo presenta como el más avanzado en uso del computador) y «Sol» (The Batch de DeepLearning.AI: https://www.deeplearning.ai/the-batch/sol-nearly-eclipses-astra; GPT-6.1 Sol presentado en el DevDay del 2026-09-29). Las fuentes no coinciden en el nombre exacto de las versiones de Sol.

## 6. Fábrica de contenido y YouTube

- Proyectos públicos con la misma arquitectura (el modelo orquesta; FFmpeg corta; Whisper transcribe; Remotion genera animaciones): https://github.com/wilwaldon/Claude-Code-Video-Toolkit , https://github.com/earondemands-sys/YouTubeAgent , https://github.com/ersinkoc/AI-Video-Factory . Solo se leyeron sus descripciones.
- Pexo, guía de 2026: «Claude Code is a reasoning and orchestration tool. The actual video frame rendering requires a separate tool».
- Política de YouTube de «contenido no auténtico» (*inauthentic content*): nombre vigente desde julio de 2025; aclarada en julio de 2026 (TechCrunch, 2026-07-20: https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/). No prohíbe la IA; retira la monetización al contenido repetitivo, genérico o producido en masa. No se leyó la página oficial de YouTube.

## 7. Supervisión humana en n8n
- URL: https://docs.n8n.io/advanced-ai/human-in-the-loop-tools
- Una herramienta de un agente puede exigir revisión humana: el flujo se pausa hasta que una persona aprueba o rechaza. Canales: Slack, Discord, Telegram, Microsoft Teams, Gmail, WhatsApp Business Cloud, Google Chat y Outlook. Si se rechaza, la acción se cancela y el agente es informado.
