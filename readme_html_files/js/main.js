// main javascript

$( document ).ready(function() {
    
    $('.versionAndDownloadBar').clone().appendTo('.main')

    $(function () {
        $('[data-toggle="popover"]').popover()
    })



    $( "#licenseModalBtn" ).on( "click", function() {

        spinner = "<div class='spinner'><i class='fa fa-spinner fa-spin fa-5x fa-fw'></i></div>"
    
        $("#licenseModal .modal-body").html(spinner)



        $('<iframe>', {
            src: 'https://choosealicense.com/licenses/gpl-3.0/',
            id:  'myFrame',
            frameborder: 0,
            scrolling: 'yes',
            onload: 'iframeLoaded()'
            }).appendTo('#licenseModal .modal-body');

        $("#licenseModal").modal("show");
       
        $('html').addClass('modal-open')
    });

    $('#licenseModal').on('hidden.bs.modal', function (e) {
        $('html').removeClass('modal-open')
        $('#licenseModal .modal-body').removeClass('iframeLoaded')
    })

    

    
});