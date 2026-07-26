/* Progressive enhancement only. Every page is fully readable with JS off. */
(function () {
  'use strict';

  /* --- copy-permalink buttons --------------------------------------- */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.copy');
    if (!btn) return;
    var text = btn.getAttribute('data-copy');
    if (text === 'HERE') text = window.location.href.split('#')[0];
    var done = function () {
      var old = btn.textContent;
      btn.textContent = 'Copied';
      btn.setAttribute('data-done', '1');
      setTimeout(function () {
        btn.textContent = old;
        btn.removeAttribute('data-done');
      }, 1600);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, function () {});
    } else {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); done(); } catch (err) {}
      document.body.removeChild(ta);
    }
  });

  /* --- section anchors copy their own deep link ---------------------- */
  document.querySelectorAll('.body a.anchor').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      if (!navigator.clipboard || !window.isSecureContext) return;
      var url = window.location.href.split('#')[0] + a.getAttribute('href');
      navigator.clipboard.writeText(url).then(function () {
        a.textContent = '✓';
        setTimeout(function () { a.textContent = '§'; }, 1300);
      }, function () {});
    });
  });

  /* --- rail: highlight the section you are reading ------------------- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.rail nav a[href^="#"]'));
  if (!links.length || !('IntersectionObserver' in window)) return;

  var map = {};
  var targets = [];
  links.forEach(function (a) {
    var el = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    if (el) { map[el.id] = a; targets.push(el); }
  });

  var visible = new Set();
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) visible.add(en.target.id);
      else visible.delete(en.target.id);
    });
    var first = targets.find(function (t) { return visible.has(t.id); });
    links.forEach(function (a) { a.classList.remove('active'); });
    if (first && map[first.id]) map[first.id].classList.add('active');
  }, { rootMargin: '-72px 0px -70% 0px', threshold: 0 });

  targets.forEach(function (t) { io.observe(t); });
})();
