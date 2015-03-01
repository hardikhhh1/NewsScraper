console.log("app.js loaded")

angular.module('ScraperApp', [
  'ui.router', 
  'ngResource',
  'ScraperApp.services',
  'ScraperApp.controllers',

  ])
.config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
  $interpolateProvider.startSymbol('[[').endSymbol(']]');

    console.log("config method called")
  // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    $urlRouterProvider.otherwise('/')

    $stateProvider.state('home', {
      url : '/',
      templateUrl : 'static/story_list.html',
      controller : 'StoryListController',
    })
})
