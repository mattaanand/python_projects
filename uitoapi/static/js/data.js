$(document).ready(function () {

    $("#login_btn").click(function (e) {
        $.post("http://localhost:8000/login",
            {"uname": $('#uname').val(), "pwd": $("#pwd").val()},
            function (result) {
                if(result.status == 201) {
                    $("#message").show()
                    $("#msg_text").text(result.reason).css({"backgroundColor":"green","color":"black"});
                } else {
                   $("#message").show()
                    $("#msg_text").text(result.reason).css({"backgroundColor":"red","color":"black"});
                }
        });
    });
});