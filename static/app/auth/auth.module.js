(function () {
    'use strict';

    angular.module('BlurAdmin.auth', [])
        .config(routeConfig);


    /** @ngInject */
    function routeConfig($stateProvider, $urlRouterProvider) {
        $stateProvider
            .state('auth', {
                url: '/login/',
                templateUrl: 'static/app/auth/login/login.html',
                title: 'Authentication',
                controller: 'LoginCtrl',
                controllerAs: 'vm',
                sidebarMeta: {
                    order: 0
                }
            }).state('reg', {
            url: '/register',
            templateUrl: 'static/app/tables/smart/tables.html',
            title: 'Register',
            controller: 'RegisterController',
            controllerAs: 'vm',
            sidebarMeta: {
                order: 100
            }
        });
        // $urlRouterProvider.when('/login', '/register');
    }

})();