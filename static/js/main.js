KEY_EMAIL = "prototype.email";
KEY_PASS = "prototype.pass";
API_KEY = "AIzaSyBCs1C39-NwEtE3Gz04nwjsJDdkoV7hahk";

email = null;
pass = null;

isCredSaved = false;

var polygon = new google.maps.Polygon({
    paths: [
        new google.maps.LatLng(27.170161, 77.998363),
        new google.maps.LatLng(27.169682, 77.998155),
        new google.maps.LatLng(27.169607, 77.998423),
        new google.maps.LatLng(27.169773, 77.998602),
        new google.maps.LatLng(27.170060, 77.998573),
        new google.maps.LatLng(27.170161, 77.998363)
    ]

});

function success(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;

    var latLng = new google.maps.LatLng(lat, lng);
    console.log(latLng);

    var isInArea = google.maps.geometry.poly.containsLocation(latLng, polygon);
    isInArea = true; //@todo: only for testing purpose, remove on production
    if (isInArea) {
        console.log("TRUE");
        $.post(
            "mark_attendance", {
                isInArea: true,
                email: email
            },
            function (json) {
                console.log("post successful")
                window.alert("Successfully Marked Your Attendance!");
            }
        );
    } else
        window.alert("You are not in the office area right now.");
}

function error() {
    console.log("Error");
}

var geo_options = {
    enableHighAccuracy: true
};

function sendCoords() {
    if (!isCredSaved) {
        email = $("#email").val();
        pass = $("#pass").val();
        if (email.length == 0 || pass.length == 0) {
            window.alert("Please enter your credentials");
            return;
        }
        navigator.geolocation.getCurrentPosition(success, error, geo_options);
        localStorage.setItem(KEY_EMAIL, email);
        localStorage.setItem(KEY_PASS, pass);
    } else {
        console.log(email);
        navigator.geolocation.getCurrentPosition(success, error, geo_options);
    }
}

function getEmail() {
    return email;
}

function init() {
    $("#as_another").hide();
    var storage = window.localStorage;
    email = storage.getItem(KEY_EMAIL);
    pass = storage.getItem(KEY_PASS);

    if (email != null || pass != null) {
        $("#email").hide();
        $("#pass").hide();
        $("#email_display").text(email);
        isCredSaved = true;
        $("#as_another").show();
    }
}

function markAsAnother() {
    localStorage.clear();
    location.reload();
}
