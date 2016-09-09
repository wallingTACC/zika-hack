jQuery.fn.extend({
    zikaSubmitMap: function() {
        return this.each(function() {
            var that = this;
            console.log("map init on", this);
            map = new google.maps.Map(this, {
              center: {lat: 0,lng: 0},
              zoom: 2
            });
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
        });
    }
});

$(document).ready(function() {
    console.log("document ready");
    $(".zikaSubmitMap").zikaSubmitMap();
});
