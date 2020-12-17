$(function() {
    function ratingEnable() {
        $("#r1").barrating("show", {
            theme: "bars-1to10"
        });
        $("#r2").barrating("show", {
            theme: "bars-1to10"
        });
        $("#r3").barrating("show", {
            theme: "bars-1to10"
        });
    }

    ratingEnable();
});