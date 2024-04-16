$(function () {

    $('#id_disableTime').datetimepicker()
        .on('changeDate', function (event) {
        event.preventDefault();
        event.stopPropagation();
        $('#id_disableTime').datetimepicker('setStartDate', event.date);
    });

    $('#id_enableTime').datetimepicker()
        .on('changeDate', function (event) {
        event.preventDefault();
        event.stopPropagation();
        $("#id_enableTime").datetimepicker('setEndDate', event.date);
    });

});