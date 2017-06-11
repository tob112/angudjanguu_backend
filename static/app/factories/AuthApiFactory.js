/**
 * Created by tobi on 6/11/17.
 */


/**
 * Created by tobi on 6/9/17.
 */


angular.module('BlurAdmin')
    .factory('AuthApiFactory', AuthApiFactory);

function AuthApiFactory($http, Restangular) {


    var baseUsers = Restangular.all('auth/');


    baseUsers.getLoggedInUser = function () {
        return baseUsers.get('user')
    };



    return baseUsers

}