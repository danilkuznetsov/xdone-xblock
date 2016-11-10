/* Javascript for XDoneXBlock. */
function XDoneXBlock(runtime, element) {

    function updateDoneButton(result) {
        $('.done-button', element).removeClass('done-button-enable');
        $('.done-button', element).addClass('done-button-disable');
        $('.done-button', element).addClass('is-disabled');
    }

    var handlerUrl = runtime.handlerUrl(element, 'done_submit');

    $('.done-button', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({}),
            success: updateDoneButton
        });
    });

}