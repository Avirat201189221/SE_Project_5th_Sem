$(window).scroll(function () {
  if ($(window).scrollTop() < 600) {
    $(".navbar").addClass("fixed-navbar-prop");
  } else {
    $(".navbar").removeClass("fixed-navbar-prop");
  }
});

$(window).scroll(function () {
  if ($(window).scrollTop() < 600) {
    $(".navbar").addClass("fixed-navbar-prop");
  } else {
    $(".navbar").removeClass("fixed-navbar-prop");
  }
});

if (window.innerWidth < 600) {
  $(".nav-link").click(() => {
    $(".navbar-toggler").toggleClass("collapsed");
    $(".navbar-toggler")[0]["ariaExpanded"] = false;
    // $(".navbar-collapse").toggleClass("collapsing");
    // $(".navbar-collapse").toggleClass("collapse");
    // setTimeout(() => {
    //   $(".navbar-collapse").toggleClass("collapsing");
    //   $(".navbar-collapse").toggleClass("collapse");
    // }, 500);
    $(".navbar-collapse.collapse").toggleClass("show");
  });
  $(".ball-animation").click(() => {
    $(".navbar-toggler").toggleClass("collapsed");
    $(".navbar-toggler")[0]["ariaExpanded"] = false;
    // $(".navbar-collapse").toggleClass("collapsing");
    // $(".navbar-collapse").toggleClass("collapse");
    // setTimeout(() => {
    //   $(".navbar-collapse").toggleClass("collapsing");
    //   $(".navbar-collapse").toggleClass("collapse");
    // }, 500);
    $(".navbar-collapse.collapse").toggleClass("show");
  });
}
