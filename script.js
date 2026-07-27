// ---------------------------------------------------------
// Terminal "typing" intro — restarted by i18n.js on language change
// ---------------------------------------------------------
const typeEl = document.getElementById('typeLine');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
let typeTimeoutId = null;

window.restartTypingEffect = function restartTypingEffect(text) {
  if (!typeEl) return;
  if (typeTimeoutId) clearTimeout(typeTimeoutId);

  if (reduceMotion) {
    typeEl.textContent = text;
    return;
  }

  let i = 0;
  const step = () => {
    typeEl.textContent = text.slice(0, i);
    i++;
    if (i <= text.length) {
      typeTimeoutId = setTimeout(step, 40);
    }
  };
  step();
};

// ---------------------------------------------------------
// Scroll-reveal for sections
// ---------------------------------------------------------
const sections = document.querySelectorAll('.section');

if ('IntersectionObserver' in window && !reduceMotion) {
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  sections.forEach((section) => revealObserver.observe(section));
} else {
  sections.forEach((section) => section.classList.add('is-visible'));
}

// ---------------------------------------------------------
// Active nav-link highlighting
// ---------------------------------------------------------
const navLinks = document.querySelectorAll('.nav-link');
const navMap = new Map();
navLinks.forEach((link) => {
  const id = link.getAttribute('data-nav');
  navMap.set(id, link);
});

if ('IntersectionObserver' in window) {
  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const link = navMap.get(entry.target.id);
      if (!link) return;
      if (entry.isIntersecting) {
        navLinks.forEach((l) => l.classList.remove('is-active'));
        link.classList.add('is-active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });

  document.querySelectorAll('main .section').forEach((section) => {
    if (navMap.has(section.id)) navObserver.observe(section);
  });
}

// ---------------------------------------------------------
// "Download CV" — generates a PDF client-side from the live page,
// in whatever language is currently selected, with a small
// terminal-style animation while it works.
// ---------------------------------------------------------
const downloadBtn = document.getElementById('downloadCvBtn');
const pdfOverlay = document.getElementById('pdfOverlay');
const pdfLog = document.getElementById('pdfLog');
const pdfLangTag = document.getElementById('pdfLangTag');

const PDF_LOG_LINES = [
  'reading profile............ ok',
  'collecting experience....... ok',
  'collecting education........ ok',
  'compiling skills............. ok',
  'rendering layout............. ok'
];

function typeLogLines(lines, onDone) {
  let lineIndex = 0;
  let charIndex = 0;
  pdfLog.textContent = '';

  function step() {
    if (lineIndex >= lines.length) {
      onDone();
      return;
    }
    const currentLine = lines[lineIndex];
    pdfLog.textContent += currentLine.charAt(charIndex);
    charIndex++;
    if (charIndex < currentLine.length) {
      setTimeout(step, 12);
    } else {
      pdfLog.textContent += '\n';
      lineIndex++;
      charIndex = 0;
      setTimeout(step, 120);
    }
  }
  step();
}

if (downloadBtn && pdfOverlay && window.html2pdf) {
  downloadBtn.addEventListener('click', () => {
    if (downloadBtn.disabled) return;
    downloadBtn.disabled = true;

    const lang = document.documentElement.lang || 'en';
    if (pdfLangTag) pdfLangTag.textContent = lang;

    pdfOverlay.hidden = false;

    typeLogLines(PDF_LOG_LINES, () => {
      document.body.classList.add('pdf-mode');

      const target = document.querySelector('main');
      const opts = {
        margin: 10,
        filename: `Obadah_Aldweiri_CV_${lang.toUpperCase()}.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2, useCORS: true },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
      };

      window
        .html2pdf()
        .from(target)
        .set(opts)
        .save()
        .then(() => {
          pdfLog.textContent += '\ndone ✔ your CV is downloading';
        })
        .catch(() => {
          pdfLog.textContent += '\nsomething went wrong — please try again';
        })
        .finally(() => {
          document.body.classList.remove('pdf-mode');
          setTimeout(() => {
            pdfOverlay.hidden = true;
            downloadBtn.disabled = false;
          }, 1400);
        });
    });
  });
}
