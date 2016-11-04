app
.controller("ModcontableCaCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr){
	$scope.fields = 'regisanual';
	var params = {};
	$scope.lista = [];
	$scope.modcontable = {};

	$scope.list = function (params){
		$scope.isLoading = true;
		cajaService.Modcontable.query(params, function(r){
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
			cajaService.Modcontable.delete({id:d.id}, function(r){
				$log.log("se eliminó modcontable: " + JSON.stringify(D));
				toastr.success('se elimino modcontable ' + d.regisanual, 'Modcontable');
				$scope.list(params);
			}, function(err){
				$log.log("error in delete: " + JSON.stringify(err));
				toastr.error(err.data.detail, err.status+ '' + err.statusText);
			});

		}
	};
})

.controller("ModCaSaveCtrl", function($scope, $state, $stateParams, cajaService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.modcontable = {};

    $scope.sel = function() {
        cajaService.Modcontable.get({ id: $stateParams.id }, function(r) {
            $scope.modcontable = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.modcontable.id) {
            cajaService.Modcontable.update({ id: $scope.modcontable.id }, $scope.modcontable, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó modcontable ' + r.regisanual, 'Modcontable');
                $state.go('caja.caja.modcontables');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            cajaService.Modcontable.save($scope.modcontable, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó modcontable ' + r.regisanual, 'Modcontable');
                $state.go('caja.caja.modcontables');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('caja.caja.modcontables');


        
    };
});