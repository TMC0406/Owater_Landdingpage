// <!-- Initialize Swiper Header -->
var swiper = new Swiper(".mySwiper", {
    loop: true,
    centeredSlides: true,
    effect: "fade",
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});
// Home
var swiperHome = new Swiper("#slideHome", {
    centeredSlides: true,
    effect: "fade",
    autoplay: {
        delay: 35000,
        disableOnInteraction: false,
    },
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: "#slideHome .swiper-button-next",
        prevEl: "#slideHome .swiper-button-prev",
    },
});
// Swiper Product
var swiper1 = new Swiper(".mySwiper1", {
    loop: true,
    spaceBetween: 10,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesProgress: true,
});
var swiper2 = new Swiper(".mySwiper2", {
    loop: true,
    spaceBetween: 10,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    thumbs: {
        swiper: swiper1,
    },
});
// Technology

var swiperTechnology = new Swiper("#slideTech", {
    slidesPerView: 1,
    spaceBetween: 20,
    freeMode: true,
    grabCursor: true,
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1024: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
    },
});

if (window.innerWidth < 991) {
    var swiperTechnology = new Swiper("#aboutSwiper", {
        slidesPerView: 1,
        freeMode: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        loop: true,
        pagination: {
            el: "#aboutSwiper .swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: "#aboutSwiper .swiper-button-next",
            prevEl: "#aboutSwiper .swiper-button-prev",
        },
    });
}