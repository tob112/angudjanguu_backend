/**
 * @author v.lugovksy
 * created on 16.12.2015
 */
(function () {
    'use strict';

    angular.module('BlurAdmin.pages.dashboard')
        .controller('UserTableCtrl', UserTableCtrl);

    /** @ngInject */
    function UserTableCtrl($scope, $filter, editableOptions, editableThemes) {


        $scope.smartTablePageSize = 10;

        $scope.smartTableData = [
            {
                id: 1,
                username: 'Mark',
                email: 'Otto',
                group: '@mdo'

            },
            {
                id: 2,
                username: 'Jacob',
                email: 'Thornton',
                group: '@fat'

            },
            {
                id: 3,
                username: 'Larry',
                email: 'Bird',
                group: '@twitter'

            }

        ];


        $scope.editableTableData = $scope.smartTableData.slice(0, 36);

        // $scope.peopleTableData = [
        //     {
        //         id: 1,
        //         username: 'Mark',
        //         email: 'Otto',
        //         username: '@mdo',
        //         email: 'mdo@gmail.com',
        //         age: '28',
        //         status: 'info'
        //     },
        //     {
        //         id: 2,
        //         username: 'Jacob',
        //         email: 'Thornton',
        //         username: '@fat',
        //         email: 'fat@yandex.ru',
        //         age: '45',
        //         status: 'primary'
        //     },
        //     {
        //         id: 3,
        //         username: 'Larry',
        //         email: 'Bird',
        //         username: '@twitter',
        //         email: 'twitter@outlook.com',
        //         age: '18',
        //         status: 'success'
        //     },
        //     {
        //         id: 4,
        //         username: 'John',
        //         email: 'Snow',
        //         username: '@snow',
        //         email: 'snow@gmail.com',
        //         age: '20',
        //         status: 'danger'
        //     },
        //     {
        //         id: 5,
        //         username: 'Jack',
        //         email: 'Sparrow',
        //         username: '@jack',
        //         email: 'jack@yandex.ru',
        //         age: '30',
        //         status: 'warning'
        //     }
        // ];

        $scope.metricsTableData = [
            {
                image: 'app/browsers/chrome.svg',
                browser: 'Google Chrome',
                visits: '10,392',
                isVisitsUp: true,
                purchases: '4,214',
                isPurchasesUp: true,
                percent: '45%',
                isPercentUp: true
            },
            {
                image: 'app/browsers/firefox.svg',
                browser: 'Mozilla Firefox',
                visits: '7,873',
                isVisitsUp: true,
                purchases: '3,031',
                isPurchasesUp: false,
                percent: '28%',
                isPercentUp: true
            },
            {
                image: 'app/browsers/ie.svg',
                browser: 'Internet Explorer',
                visits: '5,890',
                isVisitsUp: false,
                purchases: '2,102',
                isPurchasesUp: false,
                percent: '17%',
                isPercentUp: false
            },
            {
                image: 'app/browsers/safari.svg',
                browser: 'Safari',
                visits: '4,001',
                isVisitsUp: false,
                purchases: '1,001',
                isPurchasesUp: false,
                percent: '14%',
                isPercentUp: true
            },
            {
                image: 'app/browsers/opera.svg',
                browser: 'Opera',
                visits: '1,833',
                isVisitsUp: true,
                purchases: '83',
                isPurchasesUp: true,
                percent: '5%',
                isPercentUp: false
            }
        ];

        $scope.users = [
            {
                id: 1,
                username: 'Mark',
                email: 'Otto',
                group: '@mdo'

            },
            {
                id: 2,
                username: 'Jacob',
                email: 'Thornton',
                group: '@fat'

            },
            {
                id: 3,
                username: 'Larry',
                email: 'Bird',
                group: '@twitter'

            }

        ];


        $scope.groups = [
            {id: 1, text: 'user'},
            {id: 2, text: 'customer'},
            {id: 3, text: 'vip'},
            {id: 4, text: 'admin'}
        ];

        $scope.showGroup = function (user) {
            if (user.group && $scope.groups.length) {
                var selected = $filter('filter')($scope.groups, {id: user.group});
                return selected.length ? selected[0].text : 'Not set';
            } else return 'Not set'
        };

        $scope.showStatus = function (user) {
            var selected = [];
            if (user.status) {
                selected = $filter('filter')($scope.statuses, {value: user.status});
            }
            return selected.length ? selected[0].text : 'Not set';
        };


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