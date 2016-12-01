app

    .factory("cajaService", function($resource, configCaja) {
    var url = configCaja.cajaUrl;
    return {

        Usercashier: $resource(url + "usercashiers/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),

        Nivel: $resource(url + "nivels/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),
        Cajaingreso: $resource(url + "cajaingresos/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },

        }),
        Modcontable: $resource(url + "modcontables/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),
        Boleta: $resource(url + "boletas/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            "query": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results : angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options : {
                        "count": 1,
                        "pages": 1,
                        "page": 1,
                        "range": "all",
                        "previous": null,
                        "page_size": 1,
                        "next": null
                    };
                    return { results: results, options: options };
                }
            }
        }),
         Cliente: $resource(url + "clientes/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),
        PeriodoContable: $resource(url + "periodoContables/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },


            "query": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results : angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options : {
                        "count": 1,
                        "pages": 1,
                        "page": 1,
                        "range": "all",
                        "previous": null,
                        "page_size": 1,
                        "next": null
                    };
                    return { results: results, options: options };
                }
            }

        }),


    };


});


