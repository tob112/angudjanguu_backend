/**
 * @author v.lugovksy
 * created on 16.12.2015
 */
(function () {
    'use strict';

    angular.module('BlurAdmin.pages.admin')
        .directive('lol', adminUserListe);

    /** @ngInject */
    function adminUserListe() {
        return {
            templateUrl: '/static/app/pages/administration/userTable/userTable.html',
            controller: 'UserTableCtrl'
        };
    }
})();