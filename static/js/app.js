define([
  'angular',
  'angularAnimate',
  'angularBootstrap',
  'angularHighlightjs',
  'angularLinkify',
  'angularLoadingBar',
  'angularRoute',
  'angularSanitize',
  'angularUIRouter',
  'modules/barChart',
  'modules/collection',
  'modules/flash',
  'modules/notify',
  'modules/pageTitle',
  'modules/pagination',
  'modules/stream'
  ], function (angular) {
    'use strict';

    return angular.module('app', [
      'barChart',
      'changes.pageTitle',
      'chieffancypants.loadingBar',
      'collection',
      'flash',
      'hljs',
      'linkify',
      'ngAnimate',
      'ngRoute',
      'ngSanitize',
      'notify',
      'pagination',
      'stream',
      'ui.bootstrap',
      'ui.router'
    ]);
});
