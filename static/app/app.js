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
    ]).config(config);


    function config($urlRouterProvider, baSidebarServiceProvider, $authProvider, $stateProvider, $httpProvider) {


        $authProvider.loginUrl = '/auth/login/';


        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';


        $urlRouterProvider.otherwise(function ($injector) {
            var $state = $injector.get('$state');


            $state.go('auth');
        });

        $stateProvider
            .state('BlurAdmin', {
                views: {
                    'layout': {
                        templateUrl: 'pages/layout.html'
                    }
                }
            })


    }


})();


