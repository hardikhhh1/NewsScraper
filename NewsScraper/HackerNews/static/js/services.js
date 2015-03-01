angular.module("ScraperApp.services", ["ngResource"])
	.factory('Story', function($resource){

		// return "test"
		// console.log($resource('/api/story/:id'));
		return $resource('/api/story/:id');
	})
	