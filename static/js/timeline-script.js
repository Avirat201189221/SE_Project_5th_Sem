// (function () {
//     "use strict";

//     // define variables
//     var items = document.querySelectorAll(".timeline li");

//     // check if an element is in viewport
//     // http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport
//     function isElementInViewport(el) {
//       var rect = el.getBoundingClientRect();
//       return (
//         rect.top >= 0 &&
//         rect.left >= 0 &&
//         rect.bottom <=
//           (window.innerHeight || document.documentElement.clientHeight) &&
//         rect.right <= (window.innerWidth || document.documentElement.clientWidth)
//       );
//     }

//     function callbackFunc() {
//       for (var i = 0; i < items.length; i++) {
//         if (isElementInViewport(items[i])) {
//           items[i].classList.add("in-view");
//         }
//       }
//     }

//     // listen for events
//     window.addEventListener("load", callbackFunc);
//     window.addEventListener("resize", callbackFunc);
//     window.addEventListener("scroll", callbackFunc);
//   })();

$(document).ready(function () {
  var mySwiper = new Swiper(".swiper", {
    autoHeight: true,
    autoplay: {
      delay: 100_000_000_000,
      disableOnInteraction: false,
    },
    speed: 500,
    direction: "horizontal",
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      type: "progressbar",
    },
    loop: false,
    effect: "slide",
    spaceBetween: 0,
    on: {
      init: function () {
        $(".swiper-pagination-custom .swiper-pagination-switch").removeClass(
          "active"
        );
        $(".swiper-pagination-custom .swiper-pagination-switch")
          .eq(0)
          .addClass("active");
      },
      slideChangeTransitionStart: function () {
        $(".swiper-pagination-custom .swiper-pagination-switch").removeClass(
          "active"
        );
        $(".swiper-pagination-custom .swiper-pagination-switch")
          .eq(mySwiper.realIndex)
          .addClass("active");
      },
    },
  });
  $(".swiper-pagination-custom .swiper-pagination-switch").click(function () {
    mySwiper.slideTo($(this).index());
    $(".swiper-pagination-custom .swiper-pagination-switch").removeClass(
      "active"
    );
    $(this).addClass("active");
  });
});
