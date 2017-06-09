/**
 * Created by tobi on 6/9/17.
 */


angular.module('BlurAdmin')
    .factory('UserApiFactory', UserApiFactory);

function UserApiFactory($http, Restangular) {


    var baseUsers = Restangular.all('api/v1/auth/users/');


    baseUsers.list = function () {
        return baseUsers.getList()
    };

    return baseUsers

}