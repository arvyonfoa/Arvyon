/* Manual Cerebro Arvyon · comportamiento compartido
   - Barra lateral de capítulos generada desde una sola lista (para no repetirla en cada página).
   - Índice de la página (secciones h2) con resaltado al desplazarse.
   - Tema claro/oscuro, botones de copiar y filtro del glosario. */
(function () {
  "use strict";

  var CAPITULOS = [
    ["index.html", "Inicio"],
    ["proyecto.html", "El proyecto Arvyon"],
    ["segundo-cerebro.html", "Qué es un segundo cerebro"],
    ["mapa-del-cerebro.html", "Mapa del cerebro"],
    ["uso-diario.html", "Cómo se usa"],
    ["github.html", "GitHub sin miedo"],
    ["nube.html", "La nube de Claude Code"],
    ["empresa.html", "Cómo se crea la empresa"],
    ["glosario.html", "Glosario y preguntas"]
  ];

  // Tema
  var raiz = document.documentElement;
  try {
    var guardado = localStorage.getItem("manual-arvyon-tema");
    if (guardado === "dark" || guardado === "light") raiz.setAttribute("data-theme", guardado);
  } catch (e) {}

  function temaActual() {
    var t = raiz.getAttribute("data-theme");
    if (t) return t;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var boton = document.getElementById("theme-btn");
    function rotular() { if (boton) boton.textContent = temaActual() === "dark" ? "Tema claro" : "Tema oscuro"; }
    rotular();
    if (boton) boton.addEventListener("click", function () {
      var nuevo = temaActual() === "dark" ? "light" : "dark";
      raiz.setAttribute("data-theme", nuevo);
      try { localStorage.setItem("manual-arvyon-tema", nuevo); } catch (e) {}
      rotular();
    });

    // Capítulos
    var actual = (location.pathname.split("/").pop() || "index.html");
    var lista = document.getElementById("chapters");
    if (lista) {
      CAPITULOS.forEach(function (c, i) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = c[0];
        a.innerHTML = '<span class="nav-num">' + (i === 0 ? "·" : i) + "</span><span>" + c[1] + "</span>";
        if (c[0] === actual) a.setAttribute("aria-current", "page");
        li.appendChild(a); lista.appendChild(li);
      });
    }

    // Anterior / siguiente
    var pager = document.getElementById("pager");
    if (pager) {
      var idx = -1;
      CAPITULOS.forEach(function (c, i) { if (c[0] === actual) idx = i; });
      if (idx > 0) {
        var p = CAPITULOS[idx - 1];
        pager.insertAdjacentHTML("beforeend", '<a class="prev" href="' + p[0] + '"><small>Anterior</small>' + p[1] + "</a>");
      }
      if (idx >= 0 && idx < CAPITULOS.length - 1) {
        var n = CAPITULOS[idx + 1];
        pager.insertAdjacentHTML("beforeend", '<a class="next" href="' + n[0] + '"><small>Siguiente</small>' + n[1] + "</a>");
      }
    }

    // Índice de la página
    var toc = document.getElementById("toc");
    var secciones = Array.prototype.slice.call(document.querySelectorAll(".content h2[id]"));
    if (toc && secciones.length) {
      secciones.forEach(function (h) {
        var li = document.createElement("li");
        var a = document.createElement("a");
        a.href = "#" + h.id; a.textContent = h.textContent;
        li.appendChild(a); toc.appendChild(li);
      });
      if ("IntersectionObserver" in window) {
        var enlaces = toc.querySelectorAll("a");
        var obs = new IntersectionObserver(function (entradas) {
          entradas.forEach(function (en) {
            if (en.isIntersecting) {
              enlaces.forEach(function (a) { a.classList.toggle("is-active", a.getAttribute("href") === "#" + en.target.id); });
            }
          });
        }, { rootMargin: "-80px 0px -70% 0px" });
        secciones.forEach(function (h) { obs.observe(h); });
      }
    } else if (toc) {
      var bloque = toc.closest(".toc-block"); if (bloque) bloque.hidden = true;
    }

    // Copiar
    document.querySelectorAll(".prompt").forEach(function (caja) {
      var b = document.createElement("button");
      b.type = "button"; b.className = "copy-btn"; b.textContent = "Copiar";
      b.addEventListener("click", function () {
        var texto = caja.getAttribute("data-copy") || caja.firstChild.textContent.trim();
        function hecho() { b.textContent = "Copiado"; setTimeout(function () { b.textContent = "Copiar"; }, 1600); }
        function seleccionar() {
          var r = document.createRange(); r.selectNodeContents(caja.firstChild);
          var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = "Seleccionado";
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(texto).then(hecho, seleccionar);
        } else { seleccionar(); }
      });
      caja.appendChild(b);
    });

    // Glosario
    var buscador = document.getElementById("gloss-search");
    if (buscador) {
      var items = Array.prototype.slice.call(document.querySelectorAll(".gloss .def"));
      var vacio = document.getElementById("gloss-empty");
      buscador.addEventListener("input", function () {
        var q = buscador.value.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
        var visibles = 0;
        items.forEach(function (it) {
          var t = it.textContent.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
          var ok = !q || t.indexOf(q) !== -1; it.hidden = !ok; if (ok) visibles++;
        });
        if (vacio) vacio.hidden = visibles !== 0;
      });
    }
  });
})();
