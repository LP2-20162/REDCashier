app

    .factory("cajaService", function($resource, configCaja) {
    var url = configCaja.cajaUrl;
    return {

        Usercashier: $resource(url + "usercashiers/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
        }),
<<<<<<< HEAD

        Nivel: $resource(url + "nivel/:id/", { 'id': '@id' }, {
=======
        Cajaingreso: $resource(url + "cajaingresos/:id/", { 'id': '@id' }, {
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4
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


