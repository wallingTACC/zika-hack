jQuery.fn.extend({
    zikaSubmitMap: function() {
        return this.each(function() {
            var that = this;
            map = new google.maps.Map(this, {
              center: {lat: 0,lng: 0},
              zoom: 2
            });
            var readonly = $(that).attr("readonly") || false;
            var usrLat = $(that).attr("data-lat");
            var usrLng = $(that).attr("data-lng");

            $('[data-item="entry"]').each(function() {
                var newLatLng = new google.maps.LatLng({
                    lat: parseFloat($(this).attr('data-lat')),
                    lng: parseFloat($(this).attr('data-lng'))
                });
                var label = $(this).attr('data-label');
                var result = $(this).attr('data-result');

                /*
                // Choose icons for True/False result, add to repo
                var image;
                if (result == 'True') {
                    image = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/blu_circle';
                }
                else {
                    image = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/red_circle';
                }
                */

                var newMarker = new google.maps.Marker({
                    map: map,
                    position: newLatLng,
                    title: label +" : "+ result,
                    // Modify Marker icon
                    // icon: image
                });
            });

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
                    $(that).change();
                });
            }
        });
    }
});

$(document).ready(function() {
    $(".zikaSubmitMap").zikaSubmitMap();
});
