/**
 * Created by tobi on 6/7/17.
 */

(function () {
    'use strict';

    angular.module('BlurAdmin.pages.admin', [])
        .config(routeConfig);


    /** @ngInject */
    function routeConfig($stateProvider, $urlRouterProvider) {
        $stateProvider
            .state('app.admin', {
                url: '/admin/',
                templateUrl: '/static/app/pages/administration/admin.html',
                title: 'Benutzerverwaltung',
                controller: 'AdminController',
                sidebarMeta: {
                    order: 0
                }
            });

        // $urlRouterProvider.when('/admin');

    }

})();