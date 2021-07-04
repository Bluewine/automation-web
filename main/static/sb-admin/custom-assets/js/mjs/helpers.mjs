const build_toast = () => {
    // Bootstrap Toast construction
    let toastElList = [].slice.call(document.querySelectorAll('.toast'));
    let toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl);
    });

    // Shows Toasts
    $.each(toastList, function (index, element) {
        element.show();
        console.log(element, "excelent");
    });
};

const popup_notification = (title="Default Title", content="Default Content", type="success") => {
    // Deletes DOM element if exists
    if ( $('div.my-toast').length !== 0 ) {
        $('div.my-toast').remove();
    }

    // Html template for Notifications
    let toast_template = "<div aria-live=\"polite\" aria-atomic=\"true\" class=\"my-toast\">\n" +
        "    <div class=\"toast-container position-absolute top-0 end-0 p-3\">\n" +
        "        <div class=\"toast\" role=\"alert\" aria-live=\"assertive\" aria-atomic=\"true\" data-delay=\"5000\">\n" +
        "            <div class=\"toast-header bg-" + type + "\">\n" +
        "                <strong class=\"me-auto\">" + title + "</strong>\n" +
        "                <small class=\"text-muted\">just now</small>\n" +
        "                <button type=\"button\" class=\"btn-close\" data-bs-dismiss=\"toast\"\n" +
        "                        aria-label=\"Close\"></button>\n" +
        "            </div>\n" +
        "            <div class=\"toast-body\">\n" +
        "               " + content + "\n" +
        "            </div>\n" +
        "        </div>\n" +
        "    </div>\n" +
        "</div>";

    // Test inserting forcefully toast
    $('body').find('.container-fluid').prepend(toast_template);

    // Build toast
    build_toast();
};

export { build_toast, popup_notification };