/**
 * Created by tobi on 6/9/17.
 */


angular.module('BlurAdmin')
    .factory('UserApiFactory', UserApiFactory);

function UserApiFactory($http, Restangular) {


    var __users = Restangular.all('api/v1/auth/users/');


    __users.list = function () {

        return __users.getList()


    };


    __users.show = function (id) {

        return __users.get(id);

    };


    __users.create = function (user) {


        __users.post(user).then(function () {


        })

    };


    return __users;

}