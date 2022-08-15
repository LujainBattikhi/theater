function ShowPDF(element) {
    let pdf = $(element).data('pdf');
    let title = $(element).data('title');
    $('#pdf').attr('src', pdf)
    $('#pdfModalLabel').html(title);
    $('#pdfModal').modal('show');
}

$(document).ready(function () {
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
});