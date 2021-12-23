// This function enables the sidenav.
document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});


// The following two functions are used to enable the Carousel seen on the home page
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.carousel');
  var instances = M.Carousel.init(elems);
});


var instance = M.Carousel.init({
  fullWidth: true
});