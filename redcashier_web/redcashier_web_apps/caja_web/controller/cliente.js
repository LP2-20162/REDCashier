app
    .controller("ClienteCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    $scope.fields = 'codename';
    var params = {};
    $scope.lista = [];
    $scope.cliente = {};

    $scope.list = function(params) {
        $scope.isLoading = true;
        cajaService.Cliente.query(params, function(r) {
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

    $scope.onReorder = function(order) { 
        $log.log('Order: ' + order);
    };

    $scope.delete = function(d) {
        if ($window.confirm("Seguro?")) {
            cajaService.Cliente.delete({ id: d.id }, function(r) {
                $log.log("Se eliminó caja:" + JSON.stringify(d));
                toastr.success('Se eliminó caja ' + d.concepto, 'Cliente');
                $scope.list(params);
            }, function(err) {
                $log.log("Error in delete:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

})

.controller("ClienteSaveCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    $scope.cliente = {};

    $scope.sel = function() {
        cajaService.Cliente.get({ id: $stateParams.id }, function(r) {
            $scope.Cliente = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.boleta.id) {
            cajaService.Cliente.update({ id: $scope.boleta.id }, $scope.boleta, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó caja ' + r.concepto, 'Cliente');
                $state.go('caja.caja.clientes');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            cajaService.Cliente.save($scope.cajaingreso, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó caja ' + r.concepto, 'Cliente');
                $state.go('caja.caja.clientes');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('caja.caja.clientes');


        
    };
});