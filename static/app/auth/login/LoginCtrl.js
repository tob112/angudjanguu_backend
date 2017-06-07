/**
 * Created by tobi on 6/5/17.
 */


(function () {
    'use strict';

    angular.module('BlurAdmin.auth')
        .controller('LoginCtrl', LoginCtrl);

    /** @ngInject */
    function LoginCtrl($scope, $auth, $state) {


        var vm = this;


        vm.login = function () {

            var credentials = {
                username: vm.username,
                email: vm.email,
                password: vm.password

            };


            $auth.login(credentials).then(function (data) {

                $state.go('app.dashboard', {})

            })


        }


    }


})();
