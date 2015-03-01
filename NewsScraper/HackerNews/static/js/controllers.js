var hackerNewsController = angular.module('ScraperApp.controllers', []);

hackerNewsController.controller('StoryListController', function StoryCtrl($scope, Story){

	console.log("hacker news controller called")
  	$scope.home_message = "The list of stories are :";

  	// console.log(StoryService.name)
  	Story.query(function(response){
 		$scope.stories = response;
  	})

  	$scope.submitReview = function (story, is_interested){
  		story.is_interested  = is_interested;
  		// console.log(story)
  		// var updatedStory = new Story(story);
  		story.$update(function (){
  			 
  		})
  	}


  	$scope.deleteReview = function (story){
  		story.$delete(function (){
  			 var index = $scope.stories.indexOf(story);
  			 $scope.stories.splice(index, 1);
  		})
  	}
});



