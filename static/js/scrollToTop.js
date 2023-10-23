function topScroll() {
    if (document.querySelector("html").getBoundingClientRect().top < -100) {
        document.querySelector(".scrolltotop").classList.remove("scrolltotop-invisible")
    } else {
        document.querySelector(".scrolltotop").classList.add("scrolltotop-invisible")
    }
}

document.querySelector(".scrolltotop").addEventListener("click", e => { scrolltotop() })

function scrolltotop() {
    let y = window.scrollY;
    while (y >= 0) {
        y -= 100
        window.scrollTo(0, y)
    }
}

setInterval(topScroll, 100)