let myApp=angular.module('myApp');
myApp.controller('testController', function() {
    this.processes = [
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
    ]
});