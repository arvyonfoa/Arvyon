#!/usr/bin/env python3
"""Mapa real del repositorio Arvyon y de su segundo cerebro.

Uso (desde cualquier carpeta del repositorio):
    python3 .agents/skills/estructura-cerebro/mapa.py

Imprime la estructura real con el número de archivos de cada carpeta y la compara
con la estructura esperada (la de SKILL.md y PROMPT-MAESTRO.md, sección 4).
El código de salida es 1 si falta algo esperado o hay una carpeta no prevista.
Usa solo la biblioteca estándar de Python 3.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CEREBRO = REPO / "Cerebro"

RAIZ = {
    "AGENTS.md": "instrucciones para cualquier agente",
    "CLAUDE.md": "solo importa AGENTS.md",
    "README.md": "presentación del repositorio",
    "opencode.jsonc": "permisos de OpenCode",
    ".agents/skills/estructura-cerebro/SKILL.md": "esta skill",
    ".claude/skills/estructura-cerebro/SKILL.md": "puntero a la skill, para Claude Code",
    "Cerebro": "el segundo cerebro",
}
EN_CEREBRO = {
    "AGENTS.md": "esquema operativo (reglas)",
    "CLAUDE.md": "solo importa AGENTS.md",
    "PROMPT-MAESTRO.md": "prompt completo",
    "README.md": "guía rápida para el humano",
    "index.md": "catálogo de la wiki",
    "log.md": "registro; solo se añade",
    "herramientas/revisar_wiki.py": "revisión de salud",
    "manual/manual-cerebro-arvyon.html": "manual para humanos (un solo archivo)",
}
RAW = {
    "00-internos": "presentaciones, actas y notas propias",
    "articulos": "artículos e investigaciones web",
    "informes": "PDF de estudios",
    "datos": "CSV y Excel",
    "entrevistas": "entrevistas anonimizadas",
    "transcripciones": "videos, podcasts y webinars",
    "competencia": "material de competidores",
    "legal": "normas y conceptos",
    "cursos": "apuntes de cursos",
    "assets": "imágenes",
}
WIKI = {
    "00-panorama": "tesis, tablero, hoja de ruta",
    "01-mercado": "mercado y adopción de IA",
    "02-demanda-clientes": "clientes, dolores, entrevistas",
    "03-competencia": "mapa y competidores",
    "04-oferta": "paquetes y método",
    "05-finanzas": "ingresos, precios, costos",
    "06-administracion-legal": "figura legal, impuestos, datos",
    "07-marketing-canales": "embudo y canales",
    "08-operacion": "herramientas y entrega",
    "09-riesgos": "registro de riesgos",
    "10-oportunidades": "DOFA, tendencias, nichos",
    "11-conocimiento-ia": "currículo y bloques de estudio",
    "12-entidades": "instituciones, personas, herramientas",
    "13-conceptos": "ideas reutilizables",
    "14-fuentes": "una página por fuente",
    "15-analisis": "respuestas archivadas",
    "16-decisiones": "registro de decisiones",
    "_plantillas": "plantillas (no son contenido)",
    "_meta": "agenda, lagunas, glosario",
}
OCULTOS = {".gitkeep", ".DS_Store"}


def contar(carpeta: Path, patron: str = "*") -> int:
    return sum(1 for p in carpeta.rglob(patron) if p.is_file() and p.name not in OCULTOS)


def main() -> int:
    problemas: list[str] = []

    def linea(ruta: Path, texto: str, nota: str = "") -> None:
        marca = "  " if ruta.exists() else "✗ "
        if not ruta.exists():
            problemas.append(f"falta {ruta.relative_to(REPO)}")
        print(f"{marca}{texto:<46}{nota}")

    print(f"Repositorio: {REPO}\n")
    print("RAÍZ")
    for nombre, que in RAIZ.items():
        linea(REPO / nombre, nombre, que)

    print("\nCerebro/")
    for nombre, que in EN_CEREBRO.items():
        linea(CEREBRO / nombre, "  " + nombre, que)

    for capa, esperadas, patron, unidad in (("raw", RAW, "*", "archivos"), ("wiki", WIKI, "*.md", "páginas")):
        base = CEREBRO / capa
        print(f"\nCerebro/{capa}/")
        for nombre, que in esperadas.items():
            carpeta = base / nombre
            n = contar(carpeta, patron) if carpeta.is_dir() else 0
            linea(carpeta, f"  {nombre}/", f"{n:>3} {unidad} · {que}")
        if base.is_dir():
            for extra in sorted(p for p in base.iterdir() if p.name not in esperadas and p.name not in OCULTOS):
                tipo = "carpeta" if extra.is_dir() else "archivo suelto"
                problemas.append(f"{tipo} no previsto en Cerebro/{capa}/: {extra.name}")
                print(f"? {'  ' + extra.name:<46}no está en el mapa")

    if (CEREBRO / "wiki").is_dir():
        total = sum(contar(CEREBRO / "wiki" / n, "*.md") for n in WIKI if n != "_plantillas")
        print(f"\nPáginas de contenido en wiki/ (sin plantillas): {total}")

    print(f"\nPROBLEMAS ({len(problemas)})")
    for p in problemas:
        print(f"  ✗ {p}")
    print("\nResultado:", "OK" if not problemas else "LA ESTRUCTURA NO COINCIDE CON EL MAPA")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
