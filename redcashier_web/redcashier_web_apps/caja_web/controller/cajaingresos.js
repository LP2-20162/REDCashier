app
// =========================================================================
// Show View and Delete caja 
// =========================================================================
    .controller("CajaIngresoCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.fields = 'concepto';
    var params = {};
    $scope.lista = [];
    $scope.cajaingreso = {};

    $scope.list = function(params) {
        $scope.isLoading = true;
        cajaService.Cajaingreso.query(params, function(r) {
            $scope.lista = r;
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

    $scope.onReorder = function(order) { //TODO
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

// =========================================================================
// Create and Update caja
// =========================================================================
.controller("CajaIngresoSaveCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.cajaingreso = {};

    $scope.sel = function() {
        cajaService.Cajaingreso.get({ id: $stateParams.id }, function(r) {
            $scope.Cajaingreso = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.cajaingreso.id) {
            cajaService.Cajaingreso.update({ id: $scope.cajaingreso.id }, $scope.cajaingreso, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó caja ' + r.concepto, 'Cajaingreso');
                $state.go('caja.caja.cajaingresos');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            cajaService.Cajaingreso.save($scope.cajaingreso, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó caja ' + r.concepto, 'Cajaingreso');
                $state.go('caja.caja.cajaingresos');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('caja.caja.cajaingresos');


        
    };
});
