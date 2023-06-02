$(document).ready(function () {
    // Inicializa Select2
    $('.js-example-placeholder-multiple').each(function () {
        const placeholder = $(this).data('placeholder') || 'Seleccione una opción';
        $(this).select2({
            placeholder: placeholder,
            allowClear: true
        });
    });

    // Inicializa Date Range Picker
    const minDate = $('#id_fecha_inicio').data('mindate') || moment().format('YYYY-MM-DD');
    $('#id_fecha_inicio').daterangepicker({
        singleDatePicker: true,
        showDropdowns: true,
        startDate: minDate,
        minDate: minDate,
        locale: {
            format: 'YYYY-MM-DD',
            cancelLabel: 'Limpiar',
            applyLabel: 'Aplicar'
        }
    });

    $('#id_fecha_vigencia').daterangepicker({
        autoUpdateInput: false,
        locale: {
            cancelLabel: 'Limpiar',
            applyLabel: 'Aplicar',
            format: 'DD/MM/YYYY'
        }
    });

    // Actualiza el campo de fecha al seleccionar un rango
    $('#id_fecha_vigencia').on('apply.daterangepicker', function (ev, picker) {
        $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
    });

    // Limpia el campo de fecha al hacer clic en "Limpiar"
    $('#id_fecha_vigencia').on('cancel.daterangepicker', function (ev, picker) {
        $(this).val('');
    });
});
