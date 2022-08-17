function ShowPDF(element) {
    let pdf = $(element).data('pdf');
    let title = $(element).data('title');
    $('#pdf').attr('src', pdf)
    $('#pdfModalLabel').html(title);
    $('#pdfModal').modal('show');
}

var owl = $(".main-carousel");
var owlGallery = $(".gallery");
var owlNews = $(".news");
owls = [owl, owlGallery, owlNews]
owls.forEach(function (item) {
    item.owlCarousel({
        autoplay: true,
        dots: true,
        lazyLoad: true,

        loop: true,
        center: true,
        rtl: true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            700: {
                items: 2
            },
            960: {
                items: 3
            },
            1200: {
                items: 3
            },
        }
    });
});
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Initiate the wowjs animation library
new WOW().init();
$(window).scroll(function () {
    if ($(this).scrollTop()) {
        $('#toTop').fadeIn();
    } else {
        $('#toTop').fadeOut();
    }
});

$("#toTop").click(function () {
    //1 second of animation time
    //html works for FFX but not Chrome
    //body works for Chrome but not FFX
    //This strange selector seems to work universally
    $("html, body").animate({scrollTop: 0}, 1000);
});