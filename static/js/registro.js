var input = document.getElementById('password1');
input.oninvalid = function(event) {
    event.target.setCustomValidity('Debe contener al menos 8 caracteres, un número, una mayúscula y una minúscula');
var input = document.getElementById('username');
input.oninvalid = function(event) {
    event.target.setCustomValidity("Puede contener cualquier caracter alfanumérico, no espacios, ni cualquier símbolo");   