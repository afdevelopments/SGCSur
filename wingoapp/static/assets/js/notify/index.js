'use strict';
var notify = $.notify('<i class="fa fa-bell-o"></i><strong>Cargando</strong> No cierre esta página...', {
    type: 'theme',
    allow_dismiss: true,
    delay: 2000,
    showProgressbar: true,
    timer: 300,
    animate:{
        enter:'animated fadeInDown',
        exit:'animated fadeOutUp'
    }
});

setTimeout(function() {
    notify.update('message', '<i class="fa fa-bell-o"></i><strong>Cargando</strong> Datos Internos.');
}, 1000);
