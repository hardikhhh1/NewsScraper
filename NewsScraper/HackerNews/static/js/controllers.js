var hackerNewsController = angular.module('ScraperApp.controllers', []);

hackerNewsController.controller('StoryListController', function StoryCtrl($scope, Story){

	console.log("hacker news controller called")
  	$scope.home_message = "The list of stories are :";

  	// console.log(StoryService.name)
  	Story.query(function(response){
 		   $scope.stories = response;
  	})

  	$scope.submitReview = function (story){
      // console.log(story.is_interested)
  		// console.log(story)
      // story.is_interested = false;
  		story.$update(function (){
  			 console.log("story has been updated")
  		})
  	}


  	$scope.deleteReview = function (story){
  		story.$delete(function (){
  			 var index = $scope.stories.indexOf(story);
  			 $scope.stories.splice(index, 1);
  		})
  	}
});



