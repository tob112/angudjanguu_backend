(function () {
    'use strict';

    angular.module('BlurAdmin', [
        'ngAnimate',
        'ui.bootstrap',
        'ui.sortable',
        'ui.router',
        'ngTouch',
        'toastr',
        'smart-table',
        "xeditable",
        'ui.slimscroll',
        'ngJsTree',
        'angular-progress-button-styles',
        'restangular',
        'satellizer',


        'BlurAdmin.auth',
        'BlurAdmin.theme'
        // 'BlurAdmin.pages'
    ]).config(routeConfig);


    function routeConfig($urlRouterProvider, baSidebarServiceProvider, $authProvider, $stateProvider) {


        $urlRouterProvider.otherwise(function ($injector) {
            var $state = $injector.get('$state');


            $state.go('auth');
        });

        $stateProvider
            .state('appi', {
                views: {
                    'layout': {
                        templateUrl: 'pages/layout.html'
                    }
                }
            })


    }


})();


