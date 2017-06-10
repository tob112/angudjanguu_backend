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
        'BlurAdmin.theme',
        'BlurAdmin.pages'
    ]).config(config);


    function config($urlRouterProvider, baSidebarServiceProvider, $authProvider, $stateProvider, $httpProvider, RestangularProvider) {


        $authProvider.loginUrl = '/auth/login/';
        RestangularProvider.setBaseUrl('api/v1/');
        RestangularProvider.setRequestSuffix('/');
        RestangularProvider.setRestangularFields({
            id: "username"
        });


        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';


        $urlRouterProvider.otherwise(function ($injector) {
            var $state = $injector.get('$state');


            $state.go('app.admin');
        });

        $stateProvider
            .state('app', {
                templateUrl: 'static/app/pages/layout.html'

            })


    }


})();


