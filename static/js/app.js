var taskApp = angular.module('taskApp',[],function($interpolateProvider){
    $interpolateProvider.startSymbol("[[");
    $interpolateProvider.endSymbol("]]");
});

taskApp.controller("MainController",['$scope','$http','$window', function($scope,$http,$window){
    // $scope.test_var = "testing scope";
    // $scope.changeText = function(){
    //     $('#testVarH2').text("changed text");

    $scope.submitForm = function(){
        // console.log($scope.usernameModel, $scope.passwordModel);

        /*
        $scope > to access angular variables that are created inside app.js as well as from html (ng-model)

        $scope can also be used to define function that are called from html controls (eg. form submission though ng-submit)
        */
        $http({
            url:"/messages",
            method:"post",
            data:JSON.stringify({"username":$scope.usernameModel,"password":$scope.passwordModel}),
            // JSON is an angular module that takes object string(like dictionary, key value pair) as input and converts it to JSON, which is then assigned to data:
            header:{"Content-Type":"application/json"}
        })
        .then(function onSuccess(response){
            $scope.submitResponse = response.data;
        }, function onError(response){})

    }
    $scope.getSecrets = function(){
            console.log("response")
        $http({
            url:"/secrets/getSecrets",
            method:"get"

        })
        .then(function onSuccess(response){
            // console.log(response)
            /* Refer secrt.html for ng-repeat, rows is the $scope variable */
            $scope.rows = response.data['data'];
        } )
    }
}]);