/**
 * @author v.lugovksy
 * created on 16.12.2015
 */
(function () {
    'use strict';

    angular.module('BlurAdmin.pages.dashboard')
        .controller('UserTableCtrl', UserTableCtrl);

    /** @ngInject */
    function UserTableCtrl($scope, $filter, editableOptions, editableThemes, UserApiFactory) {


        $scope.rowCollection = [];
        $scope.displayedCollection = [];


        /* Ruft die api für die Userliste auf. Tabelle wird erst
         // angezeigt nachdem die Daten geladen werden.
         //
         */
        var callServer = function callServer(tableState) {

            $scope.isLoading = true;

            UserApiFactory.list().then(function (users) {
                $scope.isLoading = false;
                $scope.rowCollection = users;

            });
            $scope.smartTablePageSize = 15;

        };

        callServer();


        $scope.groups = [
            {id: 1, text: 'user'},
            {id: 2, text: 'customer'},
            {id: 3, text: 'vip'},
            {id: 4, text: 'admin'}
        ];
        //
        // $scope.showGroup = function (user) {
        //     if (user.group && $scope.groups.length) {
        //         var selected = $filter('filter')($scope.groups, {id: user.group});
        //         return selected.length ? selected[0].text : 'Not set';
        //     } else return 'Not set'
        // };


        $scope.removeUser = function (index) {
            $scope.users.splice(index, 1);
        };

        $scope.addUser = function () {
            $scope.inserted = {
                id: $scope.users.length + 1,
                name: '',
                status: null,
                group: null
            };
            $scope.users.push($scope.inserted);
        };

        editableOptions.theme = 'bs3';
        editableThemes['bs3'].submitTpl = '<button type="submit" class="btn btn-primary btn-with-icon"><i class="ion-checkmark-round"></i></button>';
        editableThemes['bs3'].cancelTpl = '<button type="button" ng-click="$form.$cancel()" class="btn btn-default btn-with-icon"><i class="ion-close-round"></i></button>';


    }
})();