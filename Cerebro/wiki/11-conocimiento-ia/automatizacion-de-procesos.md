---
tipo: estudio
area: conocimiento
estado: semilla
confianza: media
resumen: "Bloque 4: automatizar cotizaciones, facturas, correos y reportes con Make, n8n o Zapier y con IA en medio del flujo."
fuentes: ["[[2026-11-barrido-ligero-competidores]]", "[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]"]
creado: 2026-11-03
actualizado: 2026-11-11
revisar_antes: 2027-02-03
etiquetas: []
---

# Automatización de procesos sin código

## Qué es
Las plataformas de automatización conectan aplicaciones mediante disparadores y acciones. Con un paso de IA en medio, pueden leer, clasificar, resumir y redactar. Es el corazón del paquete Optimiza.

## Por qué lo demanda el cliente
Las medianas dicen «crecimos y los procesos no dan abasto» ([[segmentos]]). La automatización es lo que convierte la IA en horas ahorradas medibles.

## Qué aprender
- [ ] **Básico (explicarlo):** disparadores, acciones, conectores, webhooks y manejo de errores básico.
- [ ] **Intermedio (implementarlo):** construir flujos con Make, n8n o Zapier conectados a Google Sheets, correo, formularios, WhatsApp y el software contable del cliente.
- [ ] **Avanzado (diseñarlo y venderlo):** mapear un proceso (BPMN simple), calcular las horas ahorradas, diseñar la supervisión humana y documentar el flujo para que el cliente lo mantenga.

## Ejercicio práctico
Automatiza de punta a punta una cotización: formulario → IA que redacta la propuesta a partir de una plantilla → PDF → correo al cliente → registro en una hoja. Mide el tiempo antes y después. Es la demo n.º 1 del [[diagnostico-expres]].

## Recursos (por verificar)
- Academias y documentación oficial de Make, n8n y Zapier.
- Documentación de las API del software contable colombiano (facturación electrónica).

## Cómo se convierte en producto y contenido
- Módulo: las 2 o 3 automatizaciones de Optimiza ([[paquetes-estandar]]) y el módulo «Automatización de procesos» ([[paquete-a-la-medida]]).
- Video de YouTube: «Automaticé las cotizaciones de una pyme en 1 hora (paso a paso)».

## Lo que usa la competencia (2026-11)
**n8n** es la herramienta más citada por las agencias que atienden pymes en Colombia, a veces instalada en el servidor del cliente; Make y Zapier aparecen como alternativas. Integran Siigo, Alegra, World Office, SAP, SIESA, Zoho, HubSpot y la facturación electrónica DIAN, y ofrecen lectura de facturas con OCR e IA ([[capacidades-de-la-competencia]], [[2026-11-barrido-ligero-competidores]]). Conclusión para la Etapa 2: aprender primero n8n.

## Flujo o agente, y el patrón de fábrica (2026-11)
- **Flujo o agente.** En un flujo, el camino lo fija el código; en un agente, el modelo decide su camino. Anthropic recomienda empezar por la solución más simple y añadir complejidad solo cuando haga falta. La mayoría de los casos de una pyme son flujos: más baratos y predecibles ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).
- **Los cinco patrones de flujo:** encadenar instrucciones, enrutar, paralelizar, orquestador con trabajadores y evaluador con optimizador.
- **El patrón de fábrica.** Toda automatización se puede dibujar como una tabla de pasos de tres tipos (código, agente, humano), cada uno con su forma de revisión ([[fabrica-de-ia]]). La demo de cotización de este bloque es el primer caso.
- **Supervisión humana en n8n.** Una herramienta de un agente puede exigir revisión: el flujo se pausa hasta que una persona aprueba o rechaza por WhatsApp, Slack, Telegram o correo ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).

> [!tip] Supuesto
> Regla de trabajo: usar código para todo lo que siempre se hace igual, un agente solo donde hay que entender o redactar, y una persona donde hay dinero, datos personales o textos legales. Se valida con la demo 1 de la semana 3.

## Conexiones
- [[curriculo]]: bloque n.º 4.
- [[casos-de-uso-por-sector]]: catálogo de flujos.
- [[medicion-de-roi]]: horas ahorradas.
- [[ia-en-whatsapp-y-atencion]]: el flujo más pedido.
- [[fabrica-de-ia]]: el patrón para dibujar cualquier automatización.
