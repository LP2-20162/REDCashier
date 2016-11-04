app

    .factory("cajaService", function($resource, configCaja) {
    var url = configCaja.cajaUrl;
    return {

        PeriodoContable: $resource(url + "periodoContable/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },

        }),


    };
});
