/**
 * Created by tobi on 6/7/17.
 */

(function () {
    'use strict';

    angular.module('BlurAdmin.pages.admin')
        .directive('adminDashboard', adminDashboard);

    /** @ngInject */
    function adminDashboard() {
        return {
            restrict: 'E',
            controller: 'AdminDashboardCtrl',
            templateUrl: '/static/app/pages/administration/adminDashboard/adminDashboard.html'
        };
    }
})();