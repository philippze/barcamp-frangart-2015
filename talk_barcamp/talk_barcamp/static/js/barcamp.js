$(document).ready(function () {
    
    $('.stretch-vertically').stretchToWindowHeight();
    
    $('body').on('keyup', function (e) {
        if (e.keyCode === 39 || e.keyCode === 32) {
            var href = $('.next').attr('href');
            if (href !== undefined) {
                window.location = href;
            }
        } else if (e.keyCode === 37) {
            var href = $('.prev').attr('href');
            if (href !== undefined) {
                window.location = href;
            }
        } else if (e.keyCode === 38) {
            window.location = '/en/';
        }
    });
    
    function adjust_twocolumn() {
        var height = $(window).height() - 120;
        $('.twocolumn .col-md-6').css({'max-height': height + 'px'});
    }
    adjust_twocolumn();
    $(window).resize(adjust_twocolumn);
    
});
