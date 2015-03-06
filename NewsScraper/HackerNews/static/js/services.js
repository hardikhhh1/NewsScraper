angular.module("ScraperApp.services", ["ngResource"])
	.factory('Story', function($resource){
		return $resource('/api/story/:id', { id: '@id' },
			 {
        		'update': { method:'PUT' }
    		})
	});
	

	