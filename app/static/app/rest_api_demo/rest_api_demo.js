angular.module('RESTAPIDemo', []);

angular.module('RESTAPIDemo').controller('RESTAPIDemoController', function ($scope, $http) {
    $scope.requestToken = function () {
        var url = "/auth/getauthtoken";
        $http.get(url).success(function (data) {
            $scope.apiReturn = data;
            console.log($scope.apiReturn);
        });
    };

    $scope.accessPublicResource = function () {
        var url = '/api/hello'
        $http.get(url).success(function (data) {

            $scope.apiReturn = data;
        });
    };
    $scope.accessPrivateResource = function () {
        var url = '/getauthtoken'
        $http.get(url).success(function (data) {

            $scope.apiReturn.ii = data;
        });
    };
    $scope.accessAdminResource = function () {
        var url = '/getauthtoken'
        $http.get(url).success(function (data) {

            $scope.apiReturn = data;
        });
    };
});