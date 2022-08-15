$(document).ready(function () {
        setInterval(function () {
            var docHeight = $(window).height();
            var footerHeight = $('footer').height();
            var footerTop = $('footer').position().top + footerHeight;
            var marginTop = (docHeight - footerTop - 35);

            if (footerTop < docHeight)
                $('footer').css('margin-top', marginTop + 'px'); // padding of 30 on footer
            else
                $('footer').css('margin-top', '0px');
            // console.log("docheight: " + docHeight + "\n" + "footerheight: " + footerHeight + "\n" + "footertop: " + footerTop + "\n" + "new docheight: " + $(window).height() + "\n" + "margintop: " + marginTop);
        }, 250);
    }
);

function ShowPDF(element) {
    let pdf = $(element).data('pdf');
    let title = $(element).data('title');
    $('#pdf').attr('src', pdf)
    $('#pdfModalLabel').html(title);
    $('#pdfModal').modal('show');
}

var owl = $(".main-carousel");
owl.owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    center: true,
    rtl: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        960: {
            items: 3
        },
        1200: {
            items: 3
        }
    }
});
owl.on('mousewheel', '.owl-stage', function (e) {
    if (e.deltaY > 0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
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