document.addEventListener('DOMContentLoaded', () => {
    const typingItems = document.querySelectorAll('[data-typing]');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const typeText = async (element) => {
        const text = element.dataset.typing;
        if (reducedMotion) {
            element.textContent = text;
            return;
        }

        for (const character of text) {
            element.textContent += character;
            await new Promise((resolve) => setTimeout(resolve, 105));
        }
    };

    (async () => {
        for (const item of typingItems) {
            await typeText(item);
        }
    })();

    const revealItems = document.querySelectorAll('.scroll-reveal');

    if (!('IntersectionObserver' in window)) {
        revealItems.forEach((item) => item.classList.add('is-visible'));
        return;
    }

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            entry.target.classList.toggle('is-visible', entry.isIntersecting);
        });
    }, { threshold: 0.12 });

    revealItems.forEach((item) => revealObserver.observe(item));
});