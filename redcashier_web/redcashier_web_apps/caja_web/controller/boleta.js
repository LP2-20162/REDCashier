app
    .controller("BoletaCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    $scope.fields = 'codename';
    var params = {};
    $scope.lista = [];
    $scope.boleta = {};

    $scope.list = function(params) {
        $scope.isLoading = true;
        cajaService.Boleta.query(params, function(r) {
            $scope.lista = r.results;
            $scope.options = r.options;
            $scope.isLoading = false;
        }, function(err) {
            $log.log("Error in list:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    $scope.list(params);

    $scope.buscar = function() {
        params.page = 1;
        params.fields = $scope.fields;
        params.query = $scope.query;
        $scope.list(params);
    };

    $scope.onReorder = function(order){ 
        $log.log('Order: ' + order);
    };

    $scope.delete = function(d) {
        if ($window.confirm("Seguro?")) {
            cajaService.Cajaingreso.delete({ id: d.id }, function(r) {
                $log.log("Se eliminó caja:" + JSON.stringify(d));
                toastr.success('Se eliminó caja ' + d.concepto, 'Cajaingreso');
                $scope.list(params);
            }, function(err) {
                $log.log("Error in delete:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

})

.controller("BoletaSaveCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr, $filter) {
    //Valores iniciales
    $scope.boleta = {};
    $scope.sel = function() {
        cajaService.Boleta.get({ id: $stateParams.id }, function(r) {
            $scope.boleta = r;
            if (r.fecha) $scope.boleta.fechaT = new Date($filter('date')(r.fecha));
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.boleta.fechaT) {
            $scope.boleta.fecha = $filter('date')(new Date($scope.boleta.fechaT), 'yyyy-MM-dd');
        }
        if ($scope.boleta.id) {
            cajaService.Boleta.update({ id: $scope.boleta.id }, $scope.boleta, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó boleta ' + r.codename, 'Boleta');
                $state.go('catalogo.catalogo.boletas');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            cajaService.Boleta.save($scope.boleta, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó boleta ' + r.codename, 'Boleta');
                $state.go('catalogo.catalogo.boletas');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }

    };

    $scope.cancel = function() {
        $state.go('catalogo.catalogo.boletas');



    };
});
/*drag triview para angular*/