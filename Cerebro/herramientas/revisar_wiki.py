#!/usr/bin/env python3
"""Revisión de salud del segundo cerebro de Arvyon.

Uso (desde la carpeta Cerebro/):
    python3 herramientas/revisar_wiki.py            # informe completo
    python3 herramientas/revisar_wiki.py --fecha 2027-01-15   # simula otra fecha "hoy"

ERRORES (el código de salida es 1 si hay alguno):
  - páginas de wiki/ sin frontmatter o con campos obligatorios faltantes o inválidos
  - enlaces [[...]] que no apuntan a ningún archivo de la bóveda
  - nombres de página duplicados (Obsidian resuelve los enlaces por nombre)
  - páginas de wiki/ que no aparecen en index.md
  - páginas de tipo 'fuente' sin nota de fiabilidad, o con una nota fuera de 2 a 5

AVISOS:
  - páginas huérfanas (ninguna otra página de wiki/ las enlaza; index.md no cuenta)
  - páginas con revisar_antes vencido
  - páginas sin la sección "## Conexiones"
  - páginas en estado "semilla" (solo se cuentan)

Usa solo la biblioteca estándar de Python 3.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
WIKI = RAIZ / "wiki"
INDICE = RAIZ / "index.md"
EXCLUIDAS = {"_plantillas"}  # carpetas de wiki/ que no son contenido

CAMPOS = ["tipo", "area", "estado", "confianza", "resumen", "fuentes",
          "creado", "actualizado", "revisar_antes", "etiquetas"]
VALORES = {
    "tipo": {"tema", "entidad", "concepto", "fuente", "analisis", "decision",
             "competidor", "entrevista", "estudio", "panorama", "meta"},
    "area": {"panorama", "mercado", "demanda", "competencia", "oferta", "finanzas",
             "legal", "marketing", "operacion", "riesgos", "oportunidades",
             "conocimiento", "transversal"},
    "estado": {"semilla", "borrador", "estable", "obsoleto"},
    "confianza": {"alta", "media", "baja"},
}
FECHAS = ["creado", "actualizado", "revisar_antes"]

RE_ENLACE = re.compile(r"!?\[\[([^\]\n]+?)\]\]")
RE_BLOQUE_CODIGO = re.compile(r"```.*?```", re.S)
RE_CODIGO_LINEA = re.compile(r"`[^`\n]*`")
RE_FILA_FIABILIDAD = re.compile(r"^\|\s*Fiabilidad[^|]*\|(.*)\|\s*$", re.M)
RE_NOTA = re.compile(r"^\s*(\d+)(?:\s*[–-]\s*(\d+))?(?!\d)")
NOTA_MIN, NOTA_MAX = 2, 5  # escala de fiabilidad (PROMPT-MAESTRO.md, sección 5.7)


def leer_frontmatter(texto: str) -> dict[str, str] | None:
    """Devuelve las claves de primer nivel del frontmatter YAML (valores como texto)."""
    if not texto.startswith("---\n"):
        return None
    fin = texto.find("\n---", 4)
    if fin == -1:
        return None
    datos: dict[str, str] = {}
    for linea in texto[4:fin].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", linea)
        if m:
            datos[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return datos


def sin_codigo(texto: str) -> str:
    return RE_CODIGO_LINEA.sub("", RE_BLOQUE_CODIGO.sub("", texto))


def destino(enlace: str) -> str:
    """'pagina#seccion|alias' -> 'pagina' (sin extensión .md)."""
    # En tablas de Obsidian el alias se escribe [[pagina\|alias]]: se quita la barra invertida.
    objetivo = enlace.split("|", 1)[0].split("#", 1)[0].rstrip("\\").strip()
    objetivo = objetivo.rsplit("/", 1)[-1]
    return objetivo[:-3] if objetivo.endswith(".md") else objetivo


def notas_de_fiabilidad(texto: str) -> list[int] | None:
    """Notas de fiabilidad de una página de fuente; None si no tiene la fila en la ficha.

    La fila admite una nota ("4 — motivo"), un rango ("2–3: motivo") o varias separadas
    por "·" ("5 para … · 3 para …"). Si la fila no trae números (por ejemplo, "Ver la
    tabla por fuente"), las notas se leen de la columna "Fiab." de la tabla de fuentes.
    """
    fila = RE_FILA_FIABILIDAD.search(texto)
    if fila is None:
        return None
    notas: list[int] = []
    for parte in fila.group(1).split("·"):
        m = RE_NOTA.match(parte)
        if m:
            notas.extend(int(g) for g in m.groups() if g)
    if notas:
        return notas
    columna = None
    for linea in texto.splitlines():
        if not linea.startswith("|"):
            columna = None
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if columna is None:
            columna = next((i for i, c in enumerate(celdas) if c.startswith("Fiab.")), None)
        elif columna < len(celdas):
            m = RE_NOTA.match(celdas[columna])
            if m:
                notas.extend(int(g) for g in m.groups() if g)
    return notas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--fecha", help="fecha 'hoy' en formato AAAA-MM-DD")
    args = ap.parse_args()
    hoy = dt.date.fromisoformat(args.fecha) if args.fecha else dt.date.today()

    errores: list[str] = []
    avisos: list[str] = []

    # Todos los archivos de la bóveda que pueden ser destino de un enlace.
    nombres: dict[str, list[Path]] = defaultdict(list)
    for p in RAIZ.rglob("*"):
        if p.is_file() and ".obsidian" not in p.parts and ".git" not in p.parts:
            clave = p.stem if p.suffix == ".md" else p.name
            nombres[clave].append(p)

    paginas = sorted(
        p for p in WIKI.rglob("*.md")
        if not EXCLUIDAS.intersection(p.relative_to(WIKI).parts)
    )

    for nombre, rutas in nombres.items():
        md = [r for r in rutas if r.suffix == ".md" and WIKI in r.parents
              and not EXCLUIDAS.intersection(r.relative_to(WIKI).parts)]
        if len(md) > 1:
            errores.append(f"Nombre duplicado '{nombre}': " +
                           ", ".join(str(r.relative_to(RAIZ)) for r in md))

    texto_indice = INDICE.read_text(encoding="utf-8") if INDICE.exists() else ""
    en_indice = {destino(e) for e in RE_ENLACE.findall(sin_codigo(texto_indice))}
    if not INDICE.exists():
        errores.append("Falta index.md")

    entrantes: Counter[str] = Counter()
    estados: Counter[str] = Counter()

    archivos_revisados = paginas + [INDICE] if INDICE.exists() else paginas
    for p in archivos_revisados:
        rel = p.relative_to(RAIZ)
        texto = p.read_text(encoding="utf-8")

        for e in RE_ENLACE.findall(sin_codigo(texto)):
            d = destino(e)
            if d not in nombres:
                errores.append(f"{rel}: enlace roto [[{e}]]")
            elif p != INDICE and d != p.stem:
                entrantes[d] += 1

        if p == INDICE:
            continue

        fm = leer_frontmatter(texto)
        if fm is None:
            errores.append(f"{rel}: sin frontmatter")
            continue
        for campo in CAMPOS:
            if campo not in fm:
                errores.append(f"{rel}: falta el campo '{campo}'")
        for campo, permitidos in VALORES.items():
            v = fm.get(campo)
            if v is not None and v not in permitidos:
                errores.append(f"{rel}: valor inválido {campo}='{v}'")
        for campo in FECHAS:
            v = fm.get(campo)
            if v:
                try:
                    fecha = dt.date.fromisoformat(v)
                except ValueError:
                    errores.append(f"{rel}: fecha inválida {campo}='{v}'")
                    continue
                if campo == "revisar_antes" and fecha < hoy:
                    avisos.append(f"{rel}: revisar_antes vencido ({v})")
        if not fm.get("resumen"):
            errores.append(f"{rel}: 'resumen' vacío")
        estados[fm.get("estado", "?")] += 1

        if fm.get("tipo") == "fuente":
            notas = notas_de_fiabilidad(texto)
            if notas is None:
                errores.append(f"{rel}: falta la fila 'Fiabilidad (2–5)' en la ficha")
            elif not notas:
                errores.append(f"{rel}: la fila de fiabilidad no tiene ninguna nota")
            else:
                for n in notas:
                    if not NOTA_MIN <= n <= NOTA_MAX:
                        errores.append(f"{rel}: nota de fiabilidad {n} fuera de {NOTA_MIN} a {NOTA_MAX}")

        if p.stem not in en_indice:
            errores.append(f"{rel}: no aparece en index.md")
        if not re.search(r"^## Conexiones", texto, re.M):
            avisos.append(f"{rel}: sin sección '## Conexiones'")

    for p in paginas:
        if entrantes[p.stem] == 0:
            avisos.append(f"{p.relative_to(RAIZ)}: página huérfana (sin enlaces entrantes)")

    print(f"Revisión de salud · {hoy.isoformat()} · {len(paginas)} páginas en wiki/")
    print("Estados: " + ", ".join(f"{k}={v}" for k, v in sorted(estados.items())))
    print(f"\nERRORES ({len(errores)})")
    for e in errores:
        print(f"  ✗ {e}")
    print(f"\nAVISOS ({len(avisos)})")
    for a in avisos:
        print(f"  ! {a}")
    print("\nResultado:", "OK" if not errores else "HAY ERRORES QUE CORREGIR")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
