const chips = Array.from(document.querySelectorAll('.chip'));
const collapseButtons = Array.from(document.querySelectorAll('.collapse-btn'));
let statValue = 0;

function renderStats() {
  document.getElementById('statValue').textContent = statValue;
}

chips.forEach(chip => {
  chip.addEventListener('click', () => {
    chips.forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
  });
});

collapseButtons.forEach(button => {
  button.addEventListener('click', () => {
    const item = button.parentElement;
    item.classList.toggle('open');
  });
});

document.getElementById('updateStatBtn').addEventListener('click', () => {
  statValue += 1;
  renderStats();
});

renderStats();
