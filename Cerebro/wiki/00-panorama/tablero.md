---
tipo: panorama
area: panorama
estado: estable
confianza: alta
resumen: "Consultas Dataview: páginas por estado, revisiones vencidas, decisiones abiertas y fuentes recientes."
fuentes: []
creado: 2026-11-03
actualizado: 2026-11-03
revisar_antes: 2027-11-03
etiquetas: []
---

# Tablero (Dataview)

> [!note] Requiere el plugin **Dataview** en Obsidian. Sin él, verás solo el código.

## Páginas en semilla (por investigar)
```dataview
TABLE area, actualizado
FROM "wiki"
WHERE estado = "semilla"
SORT area ASC
```

## Revisiones vencidas
```dataview
TABLE area, revisar_antes
FROM "wiki"
WHERE revisar_antes AND date(revisar_antes) < date(today)
SORT revisar_antes ASC
```

## Decisiones
```dataview
TABLE estado, resumen
FROM "wiki/16-decisiones"
WHERE tipo = "decision"
SORT file.name ASC
```

## Últimas fuentes ingeridas
```dataview
TABLE resumen, creado
FROM "wiki/14-fuentes"
SORT creado DESC
LIMIT 10
```

## Confianza baja (prioridad de verificación)
```dataview
LIST resumen
FROM "wiki"
WHERE confianza = "baja" AND estado != "semilla"
```

## Conexiones
- [[tesis-arvyon]]: la síntesis que este tablero ayuda a mantener.
- [[agenda-de-investigacion]]: qué hacer con las páginas en semilla.
- [[lagunas]]: lo que falta verificar.
