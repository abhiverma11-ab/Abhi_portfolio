/**
 * Interactive Neural Network / Particles Canvas for Abhi Verma Portfolio
 */
(function () {
  const canvas = document.getElementById('hero-particles');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let particlesArray = [];
  let animationFrameId;

  let mouse = {
    x: null,
    y: null,
    radius: 140
  };

  function resizeCanvas() {
    canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
    canvas.height = canvas.parentElement.offsetHeight || window.innerHeight;
    initParticles();
  }

  window.addEventListener('resize', resizeCanvas);

  window.addEventListener('mousemove', function (e) {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });

  window.addEventListener('mouseout', function () {
    mouse.x = null;
    mouse.y = null;
  });

  class Particle {
    constructor(x, y, dirX, dirY, size, color) {
      this.x = x;
      this.y = y;
      this.dirX = dirX;
      this.dirY = dirY;
      this.size = size;
      this.baseColor = color;
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
      ctx.fillStyle = this.baseColor;
      ctx.shadowBlur = 8;
      ctx.shadowColor = 'rgba(0, 242, 254, 0.4)';
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    update() {
      if (this.x > canvas.width || this.x < 0) {
        this.dirX = -this.dirX;
      }
      if (this.y > canvas.height || this.y < 0) {
        this.dirY = -this.dirY;
      }

      // Mouse collision / repulsion
      if (mouse.x !== null && mouse.y !== null) {
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx * dx + dy * dy);
        if (distance < mouse.radius) {
          const force = (mouse.radius - distance) / mouse.radius;
          const directionX = dx / distance;
          const directionY = dy / distance;
          this.x -= directionX * force * 3;
          this.y -= directionY * force * 3;
        }
      }

      this.x += this.dirX;
      this.y += this.dirY;
      this.draw();
    }
  }

  function initParticles() {
    particlesArray = [];
    const numberOfParticles = Math.floor((canvas.width * canvas.height) / 11000);
    const colors = ['rgba(0, 242, 254, 0.65)', 'rgba(79, 172, 254, 0.65)', 'rgba(99, 102, 241, 0.65)'];

    for (let i = 0; i < numberOfParticles; i++) {
      let size = Math.random() * 2 + 1.2;
      let x = Math.random() * (canvas.width - size * 2) + size * 2;
      let y = Math.random() * (canvas.height - size * 2) + size * 2;
      let dirX = (Math.random() * 0.8) - 0.4;
      let dirY = (Math.random() * 0.8) - 0.4;
      let color = colors[Math.floor(Math.random() * colors.length)];

      particlesArray.push(new Particle(x, y, dirX, dirY, size, color));
    }
  }

  function connect() {
    let maxDistance = 120;
    for (let a = 0; a < particlesArray.length; a++) {
      for (let b = a + 1; b < particlesArray.length; b++) {
        let dx = particlesArray[a].x - particlesArray[b].x;
        let dy = particlesArray[a].y - particlesArray[b].y;
        let distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < maxDistance) {
          let opacityValue = 1 - (distance / maxDistance);
          ctx.strokeStyle = `rgba(0, 242, 254, ${opacityValue * 0.22})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
          ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
      particlesArray[i].update();
    }
    connect();
    animationFrameId = requestAnimationFrame(animate);
  }

  resizeCanvas();
  animate();
})();
