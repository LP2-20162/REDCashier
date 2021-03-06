﻿var baseUrl = 'http://localhost:9000/';
var loginUrl = 'http://localhost:9001/auth_web/';

var config = {
    baseUrl: baseUrl,
    loginUrl: loginUrl,
};

app.value('config', config);

app
    .config(function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.interceptors.push('authInterceptorService');
    })

.run(function($rootScope, $state, $stateParams, $window, authService) {
    // It's very handy to add references to $state and $stateParams to the $rootScope
    // so that you can access them from any scope within your applications.For example,
    // <li ng-class="{ active: $state.includes('contacts.list') }"> will set the <li>
    // to active whenever 'contacts.list' or one of its decendents is active.
    $rootScope.$state = $state;
    $rootScope.$stateParams = $stateParams;

    /*******************************agregado**************************/
    //console.log("run");

    authService.fillAuthData();
    if (authService.authentication.isAuth === false) {
        $window.location = loginUrl;
    }
    /******************************************************************/

})


.config(function($resourceProvider) {
    // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
})

/*
angular.module('app').config(function($mdDateLocaleProvider) {
    $mdDateLocaleProvider.formatDate = function(date) {
       return moment(date).format('YYYY-MM-DD');
    };
});

*/
.config(function($mdDateLocaleProvider, $provide) {
<<<<<<< HEAD

=======
>>>>>>> 92d595764936f75165ea37f317e95a3f1c617236
    $mdDateLocaleProvider.shortDays = [
        'Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'
    ];
    
    // Can change week display to start on Domingo.
    $mdDateLocaleProvider.firstDayOfWeek = 0;

<<<<<<< HEAD
=======
    $mdDateLocaleProvider.firstDayOfWeek = 0;

>>>>>>> 92d595764936f75165ea37f317e95a3f1c617236
    // Example uses moment.js to parse and format dates.
    $mdDateLocaleProvider.parseDate = function(dateString) {
        var m = moment(dateString, 'DD/MM/YYYY', true);
        return m.isValid() ? m.toDate() : new Date(NaN);
    };
    /*$mdDateLocaleProvider.formatDate = function(date) {
        if (angular.isDate(date)) {
            var m = moment(date);
            return m.isValid() ? m.format('DD/MM/YYYY') : '';
        }
        return '';
    };*/
<<<<<<< HEAD

=======
>>>>>>> 92d595764936f75165ea37f317e95a3f1c617236
})

.config(
    function($mdIconProvider, $$mdSvgRegistry) {
        // Add default icons from angular material para versiones no estables mayores a v1.0.9
        // la version v1.0.9 no necesita hacer esto
        $mdIconProvider
            .icon('md-close', $$mdSvgRegistry.mdClose)
            .icon('md-menu', $$mdSvgRegistry.mdMenu)
            .icon('md-toggle-arrow', $$mdSvgRegistry.mdToggleArrow);
    }
);



app.constant('ROUTERS_T', [{
    "estado.nombre.1": {
        "url": "/url",
        "data": {
            "section": "Menu name",
            "page": "Menu item name"
        },
        "templateUrl": "appname_web_apps/appname_web/views/model/index.html"
    }

}, {
    "estado.nombre.2": {
        "url": "/url2",
        "data": {
            "section": "Menu name2",
            "page": "Menu item name2"
        },
        "templateUrl": "appname_web_apps/appname_web/views/model2/index.html"
    }

}]);


app.constant('ROUTERS', [{
    "estado.nombre": {
        "url": "/url",
        "data": {
            "section": "Menu name",
            "page": "Menu item name"
        },
        "templateUrl": "appname_web_apps/appname_web/views/model/index.html"
    },

}, {
    "catalogo": {
        "url": "/catalogo",
        "views": {
            "": {
                "templateUrl": "app/views/layout.html"
            },
            "aside": {
                "templateUrl": "app/views/aside.html"
            },
            "content": {
                "templateUrl": "app/views/content.html"
            }
        }
    },
    "catalogo.catalogo": {
        "url": "/catalogo",
        "template": "<div ui-view ></div>"
    }
}, {
    "catalogo.catalogo.categorias": {
        "url": "/categorias",
        "data": {
            "section": "Catálogo",
            "page": "Categorías"
        },
        "templateUrl": "redcashier_web_apps/catalogo_web/views/categorias/index.html"
    },
    "catalogo.catalogo.categoriasNew": {
        "url": "/categorias/new",
        "data": {
            "section": "Catálogo",
            "page": "Categorías"
        },
        "templateUrl": "redcashier_web_apps/catalogo_web/views/categorias/form.html"
    },
    "catalogo.catalogo.categoriasEdit": {
        "url": "/categorias/:id/edit",
        "data": {
            "section": "Catálogo",
            "page": "Categorías"
        },
        "templateUrl": "redcashier_web_apps/catalogo_web/views/categorias/form.html"
    }
}, {
    "catalogo.catalogo.autores": {
        "url": "/autores",
        "data": {
            "section": "Catálogo",
            "page": "Autores"
        },
        "templateUrl": "redcashier_web_apps/catalogo_web/views/autores/index.html"
    },
    "catalogo.catalogo.autoresNew": {
        "url": "/autores/new",
        "data": {
            "section": "Catálogo",
            "page": "Autores"
        },
        "templateUrl": "redcashier_web_apps/catalogo_web/views/autores/form.html"
    },
    "catalogo.catalogo.autoresEdit": {
        "url": "/autores/:id/edit",
        "data": {
            "section": "Catálogo",
            "page": "Autores"
        },
        "templateUrl": "redcashier_web_apps/catalogo_web/views/autores/form.html"
    },

}, {
    "caja": {
        "url": "/caja",
        "views": {
            "": {
                "templateUrl": "app/views/layout.html"
            },
            "aside": {
                "templateUrl": "app/views/aside.html"
            },
            "content": {
                "templateUrl": "app/views/content.html"
            }
        }
    },
    "caja.caja": {
        "url": "/caja",
        "template": "<div ui-view ></div>"
    }
}, {
     "caja.caja.usercashiers": {
        "url": "/usercashiers",
        "data": {
            "section": "Caja",
            "page": "Usercashiers"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/usercashier/index.html"
    },
    "caja.caja.usercashiersNew": {
        "url": "/usercashiers/new",
        "data": {
            "section": "Caja",
            "page": "Usercashiers"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/usercashier/form.html"
    },
    "caja.caja.usercashiersEdit": {
        "url": "/usercashiers/:id/edit",
        "data": {
            "section": "Caja",
            "page": "Usercashiers"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/usercashier/form.html"
        }
}, {
      "caja.caja.modcontables": {
        "url": "/modcontables",
        "data": {
            "section": "Caja",
            "page": "Modcontable"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/modcontable/index.html"
    },
    "caja.caja.modcontablesNew": {
        "url": "/modcontables/new",
        "data": {
            "section": "Caja",
            "page": "Modcontables"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/modcontable/form.html"
    },
    "caja.caja.modcontablesEdit": {
        "url": "/modcontables/:id/edit",
        "data": {
            "section": "Caja",
            "page": "Modcontables"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/modcontable/form.html"
        },
},{
    "caja.caja.cajaingresos": {
        "url": "/cajaingresos",
        "data": {
            "section": "Caja",
            "page": "Caja Ingreso"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/cajaingresos/index.html"
    },
    "caja.caja.cajaingresosNew": {
        "url": "/cajaingresos/new",
        "data": {
            "section": "Caja",
            "page": "Caja Ingreso"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/cajaingresos/form.html"
    },
    "caja.caja.cajaingresosEdit": {
        "url": "/cajaingresos/:id/edit",
        "data": {
            "section": "Caja",
            "page": "Caja Ingreso"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/cajaingresos/form.html"
    }
}, {
    "caja.caja.nivels": {
        "url": "/nivels",
        "data": {
            "section": "Nivel",
            "page": "Nivel"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/nivel/index.html"
    },
    "caja.caja.nivelsNew": {
        "url": "/nivels/new",
        "data": {
            "section": "Nivel",
            "page": "Nivel"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/nivel/form.html"
    },
    "caja.caja.nivelsEdit": {
        "url": "/nivels/:id/edit",
        "data": {
            "section": "Nivel",
            "page": "Nivel"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/nivel/form.html"
    }
}, {
    "caja.caja.periodoContables": {
        "url": "/periodoContables",
        "data": {
            "section": "PeriodoContable",
            "page": "PeriodoContable"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/periodoContable/index.html"
    },
    "caja.caja.periodoContablesNew": {
        "url": "/periodoContables/new",
        "data": {
            "section": "PeriodoContable",
            "page": "PeriodoContable"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/periodoContable/form.html"
    },
    "caja.caja.periodoContablesEdit": {
        "url": "/periodoContables/:id/edit",
        "data": {
            "section": "PeriodoContable",
            "page": "PeriodoContable"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/periodoContable/form.html"
    }

}, {
    "caja.caja.boletas": {
        "url": "/boletas",
        "data": {
            "section": "Boleta",
            "page": "Boleta"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/boleta/index.html"
    },
    "caja.caja.boletasNew": {
        "url": "/boletas/new",
        "data": {
            "section": "Boleta",
            "page": "Boleta"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/boleta/form.html"
    },
    "caja.caja.boletasEdit": {
        "url": "/boletas/:id/edit",
        "data": {
            "section": "Boleta",
            "page": "Boleta"
        },
        "templateUrl": "redcashier_web_apps/caja_web/views/boleta/form.html"
    }

}]);
