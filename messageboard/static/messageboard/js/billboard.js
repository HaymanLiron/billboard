$(document).ready(function () {
    //hide the add new message container
    $(".new-message-container.horiz-align-center-div").hide();
    addEventListeners();

});


function addEventListeners() {

    $("#plus").on("click", function () {
        $("#newDate").text(writeDate());
        $(".new-message-container.horiz-align-center-div").show();
    });

    $(".confirm-new-message").on("click", function () {
        $(".new-message-container.horiz-align-center-div").hide();
    });

    $(".delete-new-message").on("click", function () {
        $(".new-message-container.horiz-align-center-div").hide();
    });
}

function writeDate() {
    var d = new Date();
    var day = d.getDate();
    var month = d.getMonth() + 1;
    var year = d.getFullYear();
    return day + "/" + month + "/" + year;
}