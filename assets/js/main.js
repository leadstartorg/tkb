/* ==========================================================================
   TKB Ventures — site behaviour
   No dependencies. Every block is guarded so pages can include only what
   they use.
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     Mobile navigation
     ------------------------------------------------------------------ */
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  var scrim = document.querySelector("[data-nav-scrim]");

  function setNav(open) {
    if (!nav || !toggle) return;
    nav.setAttribute("data-open", String(open));
    toggle.setAttribute("aria-expanded", String(open));
    if (scrim) scrim.setAttribute("data-open", String(open));
    document.body.style.overflow = open && window.innerWidth <= 900 ? "hidden" : "";
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      setNav(nav.getAttribute("data-open") !== "true");
    });
  }
  if (scrim) scrim.addEventListener("click", function () { setNav(false); });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setNav(false);
  });

  /* ------------------------------------------------------------------
     Accordions
     ------------------------------------------------------------------ */
  document.querySelectorAll(".accordion__btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var panel = document.getElementById(btn.getAttribute("aria-controls"));
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      if (panel) panel.setAttribute("data-open", String(!open));
    });
  });

  /* ------------------------------------------------------------------
     Modals (native <dialog>)
     ------------------------------------------------------------------ */
  document.querySelectorAll("[data-open-modal]").forEach(function (trigger) {
    trigger.addEventListener("click", function (e) {
      e.preventDefault();
      var dlg = document.getElementById(trigger.getAttribute("data-open-modal"));
      if (!dlg) return;
      setNav(false);
      if (typeof dlg.showModal === "function") {
        dlg.showModal();
      } else {
        // Very old browsers: fall back to the full contact page.
        window.location.href = "contact.html";
      }
    });
  });

  document.querySelectorAll("[data-close-modal]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var dlg = btn.closest("dialog");
      if (dlg) dlg.close();
    });
  });

  // Click on the backdrop closes the dialog.
  document.querySelectorAll("dialog.modal").forEach(function (dlg) {
    dlg.addEventListener("click", function (e) {
      if (e.target === dlg) dlg.close();
    });
  });

  /* ------------------------------------------------------------------
     Tabs (contact page)
     ------------------------------------------------------------------ */
  document.querySelectorAll("[data-tabs]").forEach(function (group) {
    var tabs = Array.prototype.slice.call(group.querySelectorAll('[role="tab"]'));

    function select(tab) {
      tabs.forEach(function (t) {
        var selected = t === tab;
        t.setAttribute("aria-selected", String(selected));
        t.tabIndex = selected ? 0 : -1;
        var panel = document.getElementById(t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !selected;
      });
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab); });
      tab.addEventListener("keydown", function (e) {
        var next = null;
        if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
        if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
        if (next) { e.preventDefault(); next.focus(); select(next); }
      });
    });
  });

  /* ------------------------------------------------------------------
     ZIP / service-area lookup

     >>> VERIFY BEFORE LAUNCH <<<
     These are 3-digit ZIP prefixes covering metro Atlanta, keyed off the
     Lilburn office. Confirm the real coverage list with Carolyn and edit
     SERVICE_PREFIXES below. Nothing here comes from a published coverage map.
     ------------------------------------------------------------------ */
  var SERVICE_PREFIXES = [
    "300", // Lilburn, Norcross, Duluth, Roswell, Marietta, Lawrenceville, Decatur, Snellville
    "301", // north and northeast metro
    "302", // south metro — McDonough, Newnan, Peachtree City, Stockbridge
    "303"  // Atlanta proper
  ];

  // Optional second tier: ZIPs served with extra scheduling lead time. Empty
  // while coverage is metro-only — add prefixes here to switch it back on.
  var EDGE_PREFIXES = [];

  document.querySelectorAll("[data-zip-form]").forEach(function (form) {
    var input = form.querySelector("input");
    var result = form.parentElement.querySelector("[data-zip-result]");

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!input || !result) return;

      var zip = (input.value || "").trim();


      if (!/^\d{5}$/.test(zip)) {
        result.setAttribute("data-state", "error");
        result.textContent = "Enter a 5-digit ZIP code.";
        return;
      }

      var prefix = zip.slice(0, 3);

      if (SERVICE_PREFIXES.indexOf(prefix) !== -1) {
        result.setAttribute("data-state", "in");
        result.innerHTML =
          "Yes — " + zip + " is in our service area. " +
          '<a class="link-plain" href="#" data-open-modal="modal-walkthrough">Request a walk-through</a>';
      } else if (EDGE_PREFIXES.indexOf(prefix) !== -1) {
        result.setAttribute("data-state", "out");
        result.innerHTML =
          zip + " sits at the edge of our radius. We do serve it — " +
          '<a class="link-plain" href="contact.html">call us to confirm scheduling</a>.';
      } else {
        result.setAttribute("data-state", "out");
        result.innerHTML =
          "We don't run routes in " + zip + " yet. For multi-site contracts we can still bid it — " +
          '<a class="link-plain" href="#" data-open-modal="modal-rfp">submit an RFP</a>.';
      }

      // Re-bind modal triggers that were just written into the result line.
      result.querySelectorAll("[data-open-modal]").forEach(function (t) {
        t.addEventListener("click", function (ev) {
          ev.preventDefault();
          var dlg = document.getElementById(t.getAttribute("data-open-modal"));
          if (dlg && typeof dlg.showModal === "function") dlg.showModal();
        });
      });
    });
  });

  /* ------------------------------------------------------------------
     Forms

     >>> WIRE UP BEFORE LAUNCH <<<
     Set data-endpoint on each <form> to a real POST URL. Until then the
     form validates, shows the success panel, and logs the payload to the
     console — it does not send anything.
     ------------------------------------------------------------------ */
  function showError(field, message) {
    var input = field.querySelector("input, select, textarea");
    var slot = field.querySelector(".field__error");
    if (input) input.setAttribute("aria-invalid", "true");
    if (slot) slot.textContent = message;
  }

  function clearError(field) {
    var input = field.querySelector("input, select, textarea");
    var slot = field.querySelector(".field__error");
    if (input) input.removeAttribute("aria-invalid");
    if (slot) slot.textContent = "";
  }

  function validate(form) {
    var ok = true;
    var firstBad = null;

    form.querySelectorAll(".field").forEach(function (field) {
      var input = field.querySelector("input, select, textarea");
      if (!input) return;
      clearError(field);

      if (input.required && !String(input.value).trim()) {
        showError(field, "This field is required.");
        ok = false;
        if (!firstBad) firstBad = input;
        return;
      }
      if (input.type === "email" && input.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value)) {
        showError(field, "Enter a valid email address.");
        ok = false;
        if (!firstBad) firstBad = input;
      }
      if (input.type === "tel" && input.value && input.value.replace(/\D/g, "").length < 10) {
        showError(field, "Enter a 10-digit phone number.");
        ok = false;
        if (!firstBad) firstBad = input;
      }
    });

    if (firstBad) firstBad.focus();
    return ok;
  }

  document.querySelectorAll("form[data-form]").forEach(function (form) {
    var status = form.querySelector("[data-form-status]");

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(form)) return;

      var endpoint = form.getAttribute("data-endpoint");
      var payload = Object.fromEntries(new FormData(form).entries());

      function succeed() {
        if (status) {
          status.setAttribute("data-state", "ok");
          status.textContent =
            "Thanks — we've got it. Someone from TKB Ventures will be in touch within one business day.";
        }
        form.reset();
      }

      function fail() {
        if (status) {
          status.setAttribute("data-state", "fail");
          status.innerHTML =
            'That didn\'t send. Call <a href="tel:+17700000000">(770) 000-0000</a> or ' +
            'email <a href="mailto:info@tkbventures.com">info@tkbventures.com</a> and we\'ll pick it up from there.';
        }
      }

      if (!endpoint) {
        console.log("[TKB] Form not wired to an endpoint yet. Payload:", payload);
        succeed();
        return;
      }

      fetch(endpoint, { method: "POST", body: new FormData(form) })
        .then(function (res) { return res.ok ? succeed() : fail(); })
        .catch(fail);
    });
  });

  /* ------------------------------------------------------------------
     Footer year
     ------------------------------------------------------------------ */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
