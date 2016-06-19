angular.module('bottleProcess', [])
    .controller('MainCtrl', ['$scope', function ($scope) {
    }])
    .directive('bottleProcess', function () {
        function link(scope, element, attrs) {
            var maxWaterHeight = (attrs.per) * 400;
            var waterHeight = 0.6; // from 0 - 1.0

            var waterLevelTop = element.find('.waterLevelTop');
            var waterLevel = element.find('.waterLevel');

            var startPosition = element.find('.bottle').height();
            var stopPosition = maxWaterHeight * waterHeight;

            // set start position
            waterLevelTop.css({"height": "-10px"});
            waterLevel.css({"bottom": "-10px"});

            waterLevelTop.animate({
                    "height": stopPosition + "px"
                },
                {
                    duration: 3000,
                    easing: "easeOutCubic",
                    queue: false
                });

            waterLevel.animate({
                    "bottom": (stopPosition - 10) + "px"
                },
                {
                    duration: 3000,
                    easing: "easeOutCubic",
                    queue: false
                });
        }

        return {
            strict: 'E',
            scope: {},
            templateUrl: '/static/directive/bottle-process/app/bottle-process.html',
            link: link
        }
    })