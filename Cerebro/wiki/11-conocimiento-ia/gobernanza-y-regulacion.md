---
tipo: estudio
area: conocimiento
estado: borrador
confianza: media
resumen: "Bloque 8: política de uso de IA, IA en la sombra, Ley 1581, RGPD, Reglamento Europeo de IA y marcos como ISO/IEC 42001 y NIST AI RMF."
fuentes: ["[[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]"]
creado: 2026-11-03
actualizado: 2026-11-11
revisar_antes: 2027-02-03
etiquetas: []
---

# Gobernanza, ética y regulación de la IA

## Qué es
La gobernanza define quién puede usar qué IA, con qué datos y bajo qué reglas. Es el diferencial europeo de Arvyon convertido en producto ([[posicionamiento]]).

## Por qué lo demanda el cliente
Al empresario «le da miedo exponer sus datos» ([[dolores-y-necesidades]]) y las grandes necesitan «reglas de uso y protección de datos» ([[segmentos]]). Además, muchos empleados ya usan IA sin que la empresa lo sepa ([[ia-en-la-sombra]]).

## Qué aprender
- [ ] **Básico (explicarlo):** la [[ley-1581-de-2012]], qué datos no deben ir a una IA y la diferencia entre planes gratuitos y de empresa.
- [ ] **Intermedio (implementarlo):** escribir una política de uso de IA de 2 páginas, el inventario de herramientas y una clasificación de datos simple (pública, interna, confidencial, sensible).
- [ ] **Avanzado (diseñarlo y venderlo):** el [[reglamento-europeo-de-ia]] (niveles de riesgo, alfabetización, transparencia), el [[rgpd]] y los marcos ISO/IEC 42001 y NIST AI RMF como referencia para empresas grandes.

## Ejercicio práctico
Redacta la política de uso de IA de una pyme ficticia de 30 empleados: herramientas permitidas, datos prohibidos, revisión humana, responsables y formación. Debe caber en 2 páginas y entenderse sin abogado.

## Recursos (por verificar)
- Texto oficial de la Ley 1581 de 2012 y guías de la [[sic]].
- Reglamento (UE) 2024/1689 en EUR-Lex y guías de la Comisión Europea.
- Normas ISO/IEC 42001 y el marco NIST AI RMF (resúmenes oficiales).

## Cómo se convierte en producto y contenido
- Módulo: «Política de IA y datos» ([[paquete-a-la-medida]]) y la política de Transforma; versión ligera en la guía de Inicia.
- Video de YouTube: «Qué datos NUNCA debes pegar en ChatGPT (y cómo poner reglas en tu empresa)».

## Seguridad de agentes (2026-11)
- **Inyección de instrucciones** (*prompt injection*): un texto ajeno (un correo, un mensaje de WhatsApp, una página web) le da órdenes al agente y este las obedece.
- **La «tríada letal»** (Simon Willison, 2025): el riesgo es máximo cuando un agente tiene a la vez datos privados, contenido no confiable y un canal para enviar información fuera. La defensa es quitar una de las tres.
- **Caso real:** en febrero de 2026, el título de un aviso en GitHub manipuló al robot de clasificación del proyecto Cline y acabó en la publicación no autorizada de una versión que se instaló en unas 4.000 máquinas ([[2026-11-investigacion-web-fabricas-arneses-enrutamiento]]).
- **Referencia:** OWASP publicó en diciembre de 2025 su lista de los diez riesgos de aplicaciones con agentes.
- **Regla práctica para una política de uso:** permisos mínimos para cada agente, aprobación humana para acciones con dinero, datos personales o textos legales, y registro de lo que hace ([[fabrica-de-ia]]).

> [!question] Por verificar
> El contenido exacto de la lista de OWASP y de la «regla de dos» de Meta se conoce por resúmenes; falta leer los documentos originales ([[lagunas]]).

## Conexiones
- [[curriculo]]: bloque n.º 8.
- [[proteccion-de-datos]]: el cumplimiento propio de Arvyon.
- [[alfabetizacion-en-ia]]: obligación del Reglamento Europeo de IA.
- [[politica-publica-ia]]: contexto colombiano.
- [[arnes-de-agentes]]: los permisos y las comprobaciones son parte del arnés.
