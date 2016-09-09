$(document).ready(function() {
    $(".zikaSubmitMap").change(function() {
        $("#id_lat").val($(".zikaSubmitMap").attr("data-lat"));
        $("#id_long").val($(".zikaSubmitMap").attr("data-lng"));
    });
});
