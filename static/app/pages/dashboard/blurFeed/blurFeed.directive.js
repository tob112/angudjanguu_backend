/**
 * @author v.lugovksy
 * created on 16.12.2015
 */
(function () {
  'use strict';

  angular.module('BlurAdmin.pages.dashboard')
      .directive('blurFeed', blurFeed);

  /** @ngInject */
  function blurFeed() {
    return {
      restrict: 'E',
      controller: 'BlurFeedCtrl',
      templateUrl: 'static/app/pages/dashboard/blurFeed/blurFeed.html'
    };
  }
})();