﻿var baseUrl = 'http://localhost:9000/';
var loginUrl = 'http://localhost:9001/auth_web/';
var iotecaUrl = 'http://localhost:9001/redcashier_web/';



<<<<<<< HEAD
var clientId = 'aEFq1GNIzRzvwHFTbB535M7E1jL7esuuJ3YAVI7A';
var clientSecret = 'EKNChnUJzjOFfc8FnkWZ0N0GstW76NkwXCz01IIF3SDLKMk9PewyvOlSkJutgAPECe3rHWX67uxHEYqL8fK7UP37SSwae5mGTus8StA1Ivf8viCEzXtivFcaGh8BvRqP';
=======
var clientId = 'Lldwv0KPHZgnFRcYhea2rvEpyvw5Ldv830V1ctBt';
var clientSecret = 'o3UFGLx4FvLg6JWpRFDVDzs0gBkwhg5phKh1ZL2Rfy4GtWaJ2kyZWa1mrqJrxZbzeHPvjEXsTgGx82lnLM6hphNPGPFfiT7XEMyRdhbARFeuSlKKvNcExDW8PvLpU0FW';
>>>>>>> 92d595764936f75165ea37f317e95a3f1c617236
var grantType = 'password';

var config = {

    baseUrl: baseUrl,
    loginUrl: loginUrl,
    iotecaUrl: iotecaUrl,

    clientId: clientId,
    clientSecret: clientSecret,
    grantType: grantType,

};

app.value('config', config);

app
    .run(function($rootScope, $state, $stateParams, $window, loginService) {
        // It's very handy to add references to $state and $stateParams to the $rootScope
        // so that you can access them from any scope within your applications.For example,
        // <li ng-class="{ active: $state.includes('contacts.list') }"> will set the <li>
        // to active whenever 'contacts.list' or one of its decendents is active.
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        /*******************************agregado**************************/
        console.log("run");

        if (loginService.authentication.isAuth === false) {
            $window.location = loginUrl;
        }
        /******************************************************************/

    })

.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    //$httpProvider.interceptors.push('authInterceptorService');
})

.config(function($resourceProvider) {
    // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
});
