
  document.addEventListener('contextmenu', event => event.preventDefault());
  document.addEventListener('keydown', event => {
    if (event.keyCode === 123) { // F12 key
      event.preventDefault();
    }
  });

