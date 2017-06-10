/**
 * Created by tobi on 6/9/17.
 */


angular.module('BlurAdmin')
    .factory('UserApiFactory', UserApiFactory);

function UserApiFactory($http, Restangular) {


    var baseUsers = Restangular.all('auth/users/');


    baseUsers.list = function () {
        return baseUsers.getList()
    };


    baseUsers.getUser = function (username) {
        return baseUsers.get(username)

    };


    return baseUsers

}