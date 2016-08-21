$(document).ready(function () {
    //hide the add new message container
    $(".new-message-container.horiz-align-center-div").hide();
    addEventListeners();

});


function handleBorderRed(className) {
    if ($("." + className).val() == "") {
        $("." + className).addClass("border-red");
        return false;
    } else {
        $("." + className).removeClass("border-red");
        return true;
    }
}

function handleNewMessageConfirmation() {
    var inputGood = true;
    var toValidate = ["new-message-title", "new-message-text", "new-message-author"];
    for (var i = 0; i < toValidate.length; i++) {
        var inputValid = handleBorderRed(toValidate[i]);
        if (!inputValid) {
            inputGood = false;
        }
    }
    if (inputGood){
        $(".border-red").removeClass("border-red");
        $(".new-message-container.horiz-align-center-div").hide();
    }
}

function addEventListeners() {

    $("#plus").on("click", function () {
        $("#newDate").text(writeDate());
        $(".new-message-container.horiz-align-center-div").show();
    });

    $(".confirm-new-message").on("click", handleNewMessageConfirmation);

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