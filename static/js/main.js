/**
 * Main JavaScript Engine for Abhi Verma Portfolio
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Theme Management (Dark / Light)
  const themeToggleBtn = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('portfolio-theme') || 'dark';

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('portfolio-theme', theme);
    if (themeToggleBtn) {
      const icon = themeToggleBtn.querySelector('i');
      if (icon) {
        icon.className = theme === 'dark' ? 'fas fa-sun text-warning' : 'fas fa-moon text-primary';
      }
    }
  }

  setTheme(currentTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const activeTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      setTheme(activeTheme === 'dark' ? 'light' : 'dark');
    });
  }

  // 2. Typed Text Hero Effect
  const typedTextSpan = document.getElementById('hero-typed-text');
  if (typedTextSpan) {
    const textArray = [
      'CSE (AI & ML) Student',
      'Python Developer',
      'Aspiring AI Engineer',
      'Data Analytics Enthusiast',
      'Full-Stack Developer'
    ];
    const typingDelay = 90;
    const erasingDelay = 45;
    const newTextDelay = 1800;
    let textArrayIndex = 0;
    let charIndex = 0;

    function type() {
      if (charIndex < textArray[textArrayIndex].length) {
        typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, typingDelay);
      } else {
        setTimeout(erase, newTextDelay);
      }
    }

    function erase() {
      if (charIndex > 0) {
        typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, erasingDelay);
      } else {
        textArrayIndex = (textArrayIndex + 1) % textArray.length;
        setTimeout(type, typingDelay + 300);
      }
    }

    setTimeout(type, 600);
  }

  // 3. Animated Statistics Counters
  const counterElements = document.querySelectorAll('.stat-number');
  if (counterElements.length > 0) {
    const counterObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const countTo = parseInt(target.getAttribute('data-count'), 10) || 0;
          let count = 0;
          const duration = 1500;
          const stepTime = Math.abs(Math.floor(duration / (countTo || 1)));

          const timer = setInterval(() => {
            count += 1;
            target.textContent = count;
            if (count >= countTo) {
              target.textContent = countTo + (target.getAttribute('data-suffix') || '+');
              clearInterval(timer);
            }
          }, Math.max(stepTime, 20));

          observer.unobserve(target);
        }
      });
    }, { threshold: 0.5 });

    counterElements.forEach(el => counterObserver.observe(el));
  }

  // 4. Back To Top Button
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 5. Dynamic Category Filtering (Client-side fast switcher)
  const filterButtons = document.querySelectorAll('.filter-btn');
  const filterableItems = document.querySelectorAll('.filterable-card');

  if (filterButtons.length > 0 && filterableItems.length > 0) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.getAttribute('data-filter');

        filterableItems.forEach(item => {
          const itemCategory = item.getAttribute('data-category');
          if (category === 'all' || category === 'All' || itemCategory === category) {
            item.style.display = '';
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            }, 50);
          } else {
            item.style.opacity = '0';
            item.style.transform = 'scale(0.95)';
            setTimeout(() => {
              item.style.display = 'none';
            }, 250);
          }
        });
      });
    });
  }

  // 6. Live Project Search Input Filter
  const projectSearchInput = document.getElementById('projectSearchInput');
  if (projectSearchInput && filterableItems.length > 0) {
    projectSearchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase().trim();
      filterableItems.forEach(item => {
        const title = item.querySelector('.project-title')?.textContent.toLowerCase() || '';
        const desc = item.querySelector('.project-desc')?.textContent.toLowerCase() || '';
        const tags = item.getAttribute('data-tech')?.toLowerCase() || '';

        if (title.includes(term) || desc.includes(term) || tags.includes(term)) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  }

  // 7. Interactive AJAX Contact Form Submission
  const contactForm = document.getElementById('portfolioContactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const alertBox = document.getElementById('contact-alert');

      const formData = {
        name: document.getElementById('contact-name').value.trim(),
        email: document.getElementById('contact-email').value.trim(),
        subject: document.getElementById('contact-subject').value.trim(),
        message: document.getElementById('contact-message').value.trim()
      };

      if (!formData.name || !formData.email || !formData.subject || !formData.message) {
        showAlert('Please fill out all fields.', 'danger');
        return;
      }

      // Loading state
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Sending...';

      try {
        const response = await fetch('/api/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (response.ok && data.success) {
          showAlert(data.message || 'Message sent successfully!', 'success');
          contactForm.reset();
        } else {
          showAlert(data.error || 'Failed to send message. Please try again.', 'danger');
        }
      } catch (err) {
        showAlert('A network error occurred. Please try again later.', 'danger');
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }

      function showAlert(msg, type) {
        if (!alertBox) return;
        alertBox.className = `alert alert-${type} alert-dismissible fade show`;
        alertBox.innerHTML = `
          <span>${msg}</span>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        alertBox.classList.remove('d-none');
        alertBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  }

  // 8. Certificate Lightbox Modal Handling with Prev / Next Navigation
  const certModal = document.getElementById('certModal');
  if (certModal) {
    let currentCertIndex = 0;
    let certCards = [];

    function updateCertCards() {
      certCards = Array.from(document.querySelectorAll('.cert-card')).filter(card => {
        const parent = card.closest('.filterable-card');
        return !parent || parent.style.display !== 'none';
      });
    }

    function showCertAtIndex(index) {
      updateCertCards();
      if (certCards.length === 0) return;

      if (index < 0) index = certCards.length - 1;
      if (index >= certCards.length) index = 0;
      currentCertIndex = index;

      const card = certCards[currentCertIndex];
      const title = card.getAttribute('data-cert-title') || 'Certificate';
      const org = card.getAttribute('data-cert-org') || '';
      const date = card.getAttribute('data-cert-date') || '';
      const img = card.getAttribute('data-cert-img') || '/static/images/certificate-placeholder.svg';
      const desc = card.getAttribute('data-cert-desc') || '';

      const titleEl = document.getElementById('certModalTitle');
      const orgEl = document.getElementById('certModalOrg');
      const dateEl = document.getElementById('certModalDate');
      const imgEl = document.getElementById('certModalImg');
      const descEl = document.getElementById('certModalDesc');
      const counterEl = document.getElementById('certModalCounter');

      if (titleEl) titleEl.textContent = title;
      if (orgEl) orgEl.textContent = org;
      if (dateEl) dateEl.textContent = date;
      if (imgEl) imgEl.src = img;
      if (descEl) descEl.textContent = desc;
      if (counterEl) counterEl.textContent = `${currentCertIndex + 1} / ${certCards.length}`;
    }

    certModal.addEventListener('show.bs.modal', function (event) {
      updateCertCards();
      const triggerCard = event.relatedTarget ? event.relatedTarget.closest('.cert-card') : null;
      if (triggerCard) {
        currentCertIndex = certCards.indexOf(triggerCard);
        if (currentCertIndex === -1) currentCertIndex = 0;
      }
      showCertAtIndex(currentCertIndex);
    });

    const prevBtn = document.getElementById('certModalPrev');
    const nextBtn = document.getElementById('certModalNext');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        showCertAtIndex(currentCertIndex - 1);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        showCertAtIndex(currentCertIndex + 1);
      });
    }

    // Keyboard Arrow Left/Right Navigation
    document.addEventListener('keydown', (e) => {
      if (certModal.classList.contains('show')) {
        if (e.key === 'ArrowLeft') showCertAtIndex(currentCertIndex - 1);
        if (e.key === 'ArrowRight') showCertAtIndex(currentCertIndex + 1);
      }
    });
  }
});
