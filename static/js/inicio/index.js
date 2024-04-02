

$(document).ready(function () {

    $(document).on("click", ".nav-btn.nav-slider", function () {
        $(".overlay").toggleClass("show");
        $("nav").toggleClass("open");
    });


    $(".overlay").on("click", function () {
        if ($("nav").hasClass("open")) {
            $("nav").removeClass("open");
        }
        $(this).removeClass("show");
    });
});