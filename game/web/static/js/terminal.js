// game/web/static/js/terminal.js
const socket = io();
const terminal = document.getElementById('terminal');
const input = document.getElementById('command-input');

input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        socket.emit('command', input.value);
        input.value = '';
    }
});

socket.on('output', (msg) => {
    terminal.innerHTML += `<div>> ${msg}</div>`;
    terminal.scrollTop = terminal.scrollHeight;
});