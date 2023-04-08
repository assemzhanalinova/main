function deleteConfirm(form_id) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: false,
        confirmButtonText: 'Yes, delete it!',
        customClass: {
            confirmButton: 'btn btn-primary',
        },
        buttonsStyling: false
    }).then(function (result) {
        if (result.value) {
            document.getElementById('form-' + form_id).submit();
        }
    });
}