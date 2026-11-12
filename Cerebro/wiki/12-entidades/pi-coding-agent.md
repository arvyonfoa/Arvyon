---
tipo: entidad
area: conocimiento
estado: borrador
confianza: media
resumen: "Agente de programación minimalista y de código abierto, pensado para que cada quien construya su propio arnés; herramienta para programadores, fuera del plan de la Fase 1."
fuentes: ["[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]"]
creado: 2026-11-11
actualizado: 2026-11-11
revisar_antes: 2027-02-11
etiquetas: [herramienta, agentes]
---

# Pi (agente de programación)

## Qué es
Pi es un agente de programación de código abierto que se usa desde la terminal. Lo creó Mario Zechner a finales de 2025 porque Claude Code le parecía «una nave espacial» llena de funciones que no usaba. Su lema es «Hay muchos arneses de agentes, pero este es tuyo» ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

## Datos básicos
| Campo | Valor |
|---|---|
| Tipo | herramienta |
| País | Austria (creador); lo mantiene la empresa Earendil desde abril de 2026 |
| Web oficial | https://pi.dev/ |
| Licencia | MIT (código abierto) |
| Núcleo | Cuatro herramientas (leer, escribir, editar y ejecutar comandos) e instrucciones de sistema de menos de 1.000 *tokens* |
| Lo que no trae a propósito | Subagentes, modo plan, ventanas de permiso, lista de tareas y procesos en segundo plano |
| Cómo se amplía | Extensiones en TypeScript, habilidades que se cargan bajo demanda, plantillas de instrucciones y paquetes |
| Modelos | Más de 15 proveedores; se cambia de modelo y de nivel de razonamiento en la misma sesión |

> [!warning] Contradicción · conectores MCP
> El sitio oficial dice el 2026-11-11 que MCP ya viene integrado. Guías de septiembre de 2026 y el artículo original de su creador dicen que no. Es un cambio reciente; manda el sitio oficial.

## Qué significa «harness engineering basado en Pi»
Es usar Pi como base en blanco para construir un [[arnes-de-agentes]] propio, pieza a pieza, en vez de aceptar uno ya armado. Es el camino opuesto al del proyecto RSC Harness de [[eric-risco]], que instala un arnés completo encima de Claude Code o Codex. Existe un curso abierto, «Learn Harness Engineering», con versión en español, 14 lecciones, 8 proyectos y un capítulo sobre el arnés de Pi; exige manejar terminal, git y código.

## Riesgos
- **No pide permiso antes de actuar.** Ejecuta con los permisos del usuario. Su autor considera «teatro de seguridad» las ventanas de permiso de otros agentes y recomienda aislarlo en un contenedor.
- **Los paquetes ejecutan código en la máquina.** Hay que revisarlos antes de instalarlos.

> [!question] Por verificar
> Según The Register (2026-02-20), Anthropic limita el acceso con suscripción personal de Claude a Claude Code y Claude.ai, así que para usar Claude dentro de Pi lo previsto sería una clave de API de pago por uso. No se leyó el texto de las condiciones de Anthropic ([[lagunas]]).

## Relevancia para Arvyon
**El concepto, sí; la herramienta, no por ahora.** Pi es para quien programa a diario y no es lo que usa ni vende una consultora para pymes ([[programacion-y-bases-de-datos]]). Sirve como ejemplo de una idea útil: menos funciones y más control sobre lo que ve el modelo. Si después del 15 de diciembre el fundador quiere ver un arnés por dentro, este cerebro es un caso más sencillo.

## Menciones
- [[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]: sitio oficial, artículo de su creador, tutorial en español y curso.

## Conexiones
- [[arnes-de-agentes]]: el concepto que Pi lleva al extremo.
- [[programacion-y-bases-de-datos]]: por qué no entra en la Fase 1.
- [[rag-y-agentes]]: el bloque donde se estudian los agentes.
- [[stack-herramientas]]: no forma parte de las herramientas internas de Arvyon.
