angular.module('RESTAPIDemo', []);

angular.module('RESTAPIDemo').controller('RESTAPIDemoController', function ($scope, $http) {
    $scope.token;
    $scope.requestToken = function () {
        //var url = "/auth/getauthtoken";
        var url = "/api/1.0/tokenauth";
        var data={
            username:"ben",
            password:"123"
        }
        $http.post(url, data ).success(function (data) {
            $scope.apiReturn = data;
            $scope.token = data.token;
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
        //$scope.token  ????
        var url = '/api/1.0/privatehello'
        var config = {};
        config.headers['Token'] = $scope.token;
        $http.get(url, config).success(function (data) {

            $scope.apiReturn = data;
        });
    };
    $scope.accessAdminResource = function () {
        var url = '/getauthtoken'
        $http.get(url).success(function (data) {

            $scope.apiReturn = data;
        });
    };
});