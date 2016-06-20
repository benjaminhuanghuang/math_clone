var autoDemoApp = angular.module('AngularAuthDemoApp', ['ui.router']);

autoDemoApp.config(function ($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/angulrauthdemo');

    $stateProvider
        .state('anonymous', {
            url: '/anonymouse',
            controller: '',
            templateUrl: '/static/app/angular_auth_demo/anonymouse.tpl.html'
        })
        .state('user', {
            url: '/use',
            controller: '',
            templateUrl: '/static/app/angular_auth_demo/user.tpl.html'
        })
        .state('admin', {
            url: '/admin',
            controller: '',
            templateUrl: '/static/app/angular_auth_demo/admin.tpl.html'
        });
});