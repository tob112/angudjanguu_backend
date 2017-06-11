/**
 * Created by tobi on 6/7/17.
 */
/**
 * Created by tobi on 6/7/17.
 */

/**
 * Created by tobi on 6/5/17.
 */


(function () {
    'use strict';

    angular.module('BlurAdmin.pages.admin')
        .controller('AdminController', AdminController);

    /** @ngInject */
    function AdminController($scope, $filter, editableOptions, editableThemes, UserApiFactory) {
        $scope.userRowCollection = [];
        $scope.userDisplayedCollection = [];


        /* Ruft die api für die Userliste auf. Tabelle wird erst
         // angezeigt nachdem die Daten geladen werden.
         //
         */
        var callServer = function callServer(tableState) {

            $scope.isLoading = true;

            UserApiFactory.list().then(function (users) {
                $scope.isLoading = false;
                $scope.userRowCollection = users;

            });
            $scope.tablePageSize = 15;

        };

        callServer();


        $scope.removeUser = function (index) {
            $scope.userRowCollection.splice(index, 1);
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


        $scope.checkEmail = function (email) {
            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

            if (!re.test(email)) {
                return "Not a valid email adress";
            }
        };


        $scope.saveUser = function (user) {
            UserApiFactory.getUser(user.id).then(function (updatedUser) {
                updatedUser.username = user.username;
                updatedUser.email = user.email;
                UserApiFactory.updateUser(updatedUser).then(function () {
                    console.log("User saved");
                }, function (response) {
                    console.log(response)
                });
            });
        };

        editableOptions.theme = 'bs3';
        editableThemes['bs3'].submitTpl = '<button type="submit" class="btn btn-primary btn-with-icon"><i class="ion-checkmark-round"></i></button>';
        editableThemes['bs3'].cancelTpl = '<button type="button" ng-click="$form.$cancel()" class="btn btn-default btn-with-icon"><i class="ion-close-round"></i></button>';


    }


})();
