let myApp=angular.module('myApp');
myApp.controller('TestController', ['$scope', '$location', '$http', function($scope, $location, $http) {
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
        var req = {
            method: 'POST',
            url: 'http://127.0.0.1:8000',
            headers: {
                'Content-Type': undefined
            },
            data: { test: 'test' }
        };
        $http(req).then(function successCallback(response) {
            alert('hello');
        }, function errorCallback(response) {
            alert('error');
        })
    }
}]);