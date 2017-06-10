/**
 * Created by tobi on 6/10/17.
 */


// (function () {
//     'use strict';
//
//     angular.module('BlurAdmin.pages.admin')
//         .directive('userTableSearch', userTableSearch);
//
//     /** @ngInject */
//     function userTableSearch() {
//         return {
//             restrict: 'E',
//             require: '^stTable',
//             scope: {
//                 searchWatchModel: '='
//             },
//             link: function (scope, ele, attr, ctrl) {
//                 var table = ctrl;
//                 scope.$watch('searchWatchModel', function (val) {
//                     ctrl.search(val)
//                 })
//             },
//             template: '<input type="text" ng-model="query"/>'
//
//         };
//     }
// })();