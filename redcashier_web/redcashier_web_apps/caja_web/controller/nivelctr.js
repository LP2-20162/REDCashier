app
.controller("NivelCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr){
	$scope.fields = 'nombreSucs';
	var params = {};
	$scope.lista = [];
	$scope.usercashier = {};

	$scope.list = function (params){
		$scope.isLoading = true;
		cajaService.Nivel.query(params, function(r){
			$scope.lista = r.results;
			$scope.options = r.options;
			$scope.isLoading = false;
		}, function(err){
			$log.log("Error in list:" + JSON.stringify(err));
            toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
		});
	};
	$scope.list(params);
	$scope.buscar =function(){
		params.page = 1;
		params.fields = $scope.fields;
		params.query = $scope.query;
		$scope.list(params);
	};
	$scope.onReorder = function(order){
		$log.log('order: ' + order);
	};
	$scope.delete = function(d){
		if($window.confirm("seguro?")){
			cajaService.Nivel.delete({id:d.id}, function(r){
				$log.log("se eliminó nivel: " + JSON.stringify(D));
				toastr.success('se elimino nivel ' + d.nombreSucs, 'Nivel');
				$scope.list(params);
			}, function(err){
				$log.log("error in delete: " + JSON.stringify(err));
				toastr.error(err.data.detail, err.status+ '' + err.statusText);
			});

		}
	};
})

.controller("NivelSaveCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.nivel = {};

    $scope.sel = function() {
        cajaService.Nivel.get({ id: $stateParams.id }, function(r) {
            $scope.nivel = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.nivel.id) {
            cajaService.Nivel.update({ id: $scope.nivel.id }, $scope.nivel, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó nivel ' + r.nombreSucs, 'Nivel');
                $state.go('caja.caja.nivels');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            cajaService.Nivel.save($scope.nivel, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó nivel ' + r.nombreSucs, 'Nivel');
                $state.go('caja.caja.nivels');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('caja.caja.nivels');


        
    };
});