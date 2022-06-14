//animation when user clicks "Signup" button
$("#signup").click(function () {
    $(".light_background").animate({left: '-100%'}, "slow");
    $("#login_form").animate({opacity: '0'}, "slow").css('display', 'none');
    $("#register_form").css('display', 'block').animate({opacity: '1'}, "slow");
});

//animation when user clicks "Login" button
$("#login").click(function () {
    $(".light_background").animate({left: '0%'}, "slow");
    $("#register_form").animate({opacity: '0'}, "slow").css('display', 'none');
    $("#login_form").css('display', 'block').animate({opacity: '1'}, "slow");
});

//Event listeners for active input elements- change CSS class
$("input").focusin(function () {
    var label = $("label[for='" + $(this).attr("id") + "']");
    $(label).addClass("active");
});

$("input").focusout(function () {
    var label = $("label[for='" + $(this).attr("id") + "']");
    $(label).removeClass("active");
});