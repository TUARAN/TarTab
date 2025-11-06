function updateClock() {
  const now = new Date();
  const time = now.toLocaleTimeString('zh-CN', { hour12: false });
  document.getElementById('clock').textContent = time;
}

setInterval(updateClock, 1000);
updateClock();

