/*
 Modifies the style of an element once the content is loaded and the DOM
 is ready
*/

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');

  header.style.color = '#FF0000';
});
