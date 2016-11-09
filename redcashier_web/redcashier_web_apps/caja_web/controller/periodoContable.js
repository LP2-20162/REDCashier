app
// =========================================================================
// Show View and Delete Categoria 
// =========================================================================
    .controller("PeriodoContableCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.fields = 'nombre';
    var params = {};
    $scope.lista = [];
    $scope.periodoContable = {};

    
    //$window.location = "#" + $location.path();

    $scope.list = function(params) {
        $scope.isLoading = true;
        cajaService.PeriodoContable.query(params, function(r) {
            $scope.lista = r;
            //$scope.options = r.options;
            $scope.isLoading = false;
        }, function(err) {
            $log.log("Error in list:" + JSON.stringify(err));
            toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
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
            cajaService.PeriodoContable.delete({ id: d.id }, function(r) {
                $log.log("Se eliminó el periodo:" + JSON.stringify(d));
                toastr.success('Se eliminó la categoría ' + d.nombre, 'PeriodoContable');
                $scope.list(params);
            }, function(err) {
                $log.log("Error in delete:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

})

// =========================================================================
// Create and Update Categoria
// =========================================================================
.controller("PeriodoContableSaveCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.periodoContable = {};

    $scope.sel = function() {
        cajaService.PeriodoContable.get({ id: $stateParams.id }, function(r) {
            $scope.periodoContable = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.periodoContable.id) {
            cajaService.PeriodoContable.update({ id: $scope.periodoContable.id }, $scope.periodoContable, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó el periodo ' + r.nombre, 'PeriodoContable');
                $state.go('caja.caja.periodoContables');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            cajaService.PeriodoContable.save($scope.periodoContable, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó el periodo ' + r.nombre, 'PeriodoContable');
                $state.go('caja.caja.periodoContables');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('caja.caja.periodoContables');
    };
});
