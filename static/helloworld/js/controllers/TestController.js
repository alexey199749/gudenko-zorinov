let myApp=angular.module('myApp');
myApp.controller('TestController', ['$scope', '$location', function($scope, $location) {
    $scope.processes = [
        {
            name: 'Google Chrome',
            ID: 1000,
            user: 'Nik'
        },
        {
            name: 'Opera',
            ID: 1001,
            user: 'Nik'
        },
        {
            name: 'svchost',
            ID: 1002,
            user: 'System'
        }
    ];
    $scope.change = function(url) {
        $location.path(url);
    }
}]);