(function () {
    "use strict";
  
    var carousels = function () {
      $(".owl-carousel1").owlCarousel({
        loop: true,
        center: true,
        margin: 0,
        responsiveClass: true,
        nav: false,
        responsive: {
          0: {
            items: 1,
            nav: false
          },
          680: {
            items: 2,
            nav: false,
            loop: false
          },
          1000: {
            items: 3,
            nav: true
          }
        }
      });
    };
  
    (function ($) {
      carousels();
    })(jQuery);
  })();
  
  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("pqrs_form").addEventListener("submit", function() {
        setTimeout(function() {
            document.getElementById("pqrs_form").reset();
        }, 500);
    });

    document.getElementById("search_form").addEventListener("submit", function() {
        setTimeout(function() {
            document.getElementById("search_form").reset();
        }, 500);
    });
});