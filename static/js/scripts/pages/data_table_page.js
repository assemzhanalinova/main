/**
 * DataTables Basic
 */

$(function () {
    'use strict';
    var lang = 'Russian';
    var category_table = $('.datatables-data');

    // DataTable with buttons
    // --------------------------------------------------------------------
     if (category_table.length) {
        category_table.DataTable({
            columns: table_column,
            columnDefs: [
                {
                    // For Responsive
                    className: 'control',
                    orderable: false,
                    responsivePriority: 2,
                    targets: 0
                },
                {
                    targets: 2,
                },
            ],
            dom: '<"card-header border-bottom p-1"<"head-label"><"dt-action-buttons text-end"B>><"d-flex justify-content-between align-items-center mx-0 row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6"f>>t<"d-flex justify-content-between mx-0 row"<"col-sm-12 col-md-6"i><"col-sm-12 col-md-6"p>>',
            displayLength: 7,
            lengthMenu: [7, 10, 25, 50, 75, 100],
            buttons: [],
            responsive: {
            },
            language: {
                url: '//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/' + lang + '.json',
                paginate: {
                    // remove previous & next text from pagination
                    previous: '&nbsp;',
                    next: '&nbsp;'
                },
            }
        });
    }
});