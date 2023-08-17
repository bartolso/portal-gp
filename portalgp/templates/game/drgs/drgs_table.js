$(document).ready(function() {
    $('#dataTable').DataTable({
        processing: true,
        serverSide: true,
        responsive: true,
        ajax: {
            url: "{% url 'get_drgs_paginated_data' %}",
            data: function (d) {
                d.page = $('#dataTable').DataTable().page.info().page + 1;
            },
            dataSrc: 'data',
        },
        columns: [
            { 
                data: 'id',
                render: function(data, type, row) {
                    data = '<a href="/drgs/drg/' + data + '" type="button" class="btn btn-secondary btn-sm">' + data + '</a>';
                    return data;
                }
            },
            { 
                data: 'person_name',
                render: function(data, type, row) {
                    return data;
                }
            },
            { 
                data: 'date',
                render: function(data, type, row) {
                    return data;
                }
            },
            { 
                data: 'time',
                render: function(data, type, row) {
                    if (type === 'display') {
                        var formattedTime = moment(data, 'HH:mm:ss').format('HH:mm');
                    
                        return formattedTime;
                    }
                    return data;
                }
            },
            { 
                data: 'mbd_time',
                render: function(data, type, row) {
                    if (data == null) {
                        return '<td><span class="badge bg-warning">Sin M.B.D.</span></td>'
                    }
                    if (type === 'display') {
                        var data = moment(data, 'HH:mm:ss').format('HH:mm');
                    }
                    data = '<a href="/mbds/mbd/' + row.mbd_id + '" type="button" class="btn btn-secondary btn-sm">' + data + '</a>';
                    return data;
                }
            },
            { 
                data: 'valid',
                render: function(data, type, row) {
                    switch (data) {
                        case 'Si':
                            return '<td><span class="badge bg-success">Válido</span></td>';
                            break;
                        case 'No':
                            return '<td><span class="badge bg-danger">Inválido</span></td>';
                            break;
                        case 'Sin revisar':
                            return '<td><span class="badge bg-warning">Sin revisar</span></td>';;
                            break;
                        default:
                            return data;
                            break;
                    }
                    return data;
                }
            },
            
        ],
    });
});