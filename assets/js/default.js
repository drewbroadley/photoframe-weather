$(document).ready(function() {

  var min = 60 * 1000;
  var hour = (min * 60);
  var day = (hour * 24);

  var photo_url;

  getWeather(); //Get the initial weather.

  getPhoto(); //Get the initial photo.

  setInterval(getWeather, min * 15); //Update the weather every 10 minutes.

  setInterval(getPhoto, min/4);

  setInterval(reloadPage, day);

});

function reloadPage()
{
  location.reload();
}

function getPhoto()
{

  $.ajax({
    url: "/api/photo/",
    success: function(photo)
    {
      console.log(photo);

      photo_url = photo;

      img = new Image();
      img.onload = function () {
        $("body").css('background-image', 'url(' + photo_url + ')')
      }

      img.src = photo_url;


    }
  });

}

function getWeather() {
  $.ajax({
    url: "/api/weather/",
    success: function(weather)
    {
      $("div#weather .temp span.degrees").text(weather.info.temp);

      $("div#weather .temp-feels-high-low span.feels").text(weather.info.windChill);

      //$("div#weather .temp-feels-high-low span.low").text(weather.forecast.today.min);
      $("div#weather .temp-feels-high-low span.high").text(weather.forecast.today.max);

      $("div#weather .desc span").text(weather.forecast.today.forecast);

      console.log(weather);
    }
  });
}
