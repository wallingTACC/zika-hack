jQuery.fn.extend({
    zikaSubmitMap: function() {
        return this.each(function() {
            console.log("init map on", this);
            var that = this;
            map = new google.maps.Map(this, {
              center: {lat: 0,lng: 0},
              zoom: 2
            });
            var readonly = $(that).attr("readonly") || false;
            var usrLat = $(that).attr("data-lat");
            var usrLng = $(that).attr("data-lng");

            if (usrLat && usrLng) {
                var usrLatLng = new google.maps.LatLng({
                    lat: parseFloat(usrLat),
                    lng: parseFloat(usrLng)
                });
                map.marker = new google.maps.Marker({
                    position: usrLatLng,
                    map: map
                });
                map.panTo(usrLatLng);
                map.setZoom(5);
            }
            if (!readonly) {
                map.addListener('click', function(e) {
                    if (map.marker == undefined) {
                        map.marker = new google.maps.Marker(
                        {
                            position: e.latLng, 
                            map: map
                        }
                        );
                    } else {
                        map.marker.setPosition(e.latLng);
                    }
                    map.panTo(e.latLng);
                    map.setZoom(5);
                    $(that).attr('data-lat', e.latLng.lat());
                    $(that).attr('data-lng', e.latLng.lng());
                });
            }
        });
    }
});

$(document).ready(function() {
    console.log("hello world");
    $(".zikaSubmitMap").zikaSubmitMap();
});
