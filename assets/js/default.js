$(document).ready(function() {

  var min = 60 * 1000;
  var hour = (min * 60);
  var day = (hour * 24);

  getWeather(); //Get the initial weather.

  getPhoto(); //Get the initial photo.

  setInterval(getWeather, min); //Update the weather every 10 minutes.

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

      $("body").css('background-image', 'url(' + photo + ')')
    }
  });

}

function getWeather() {
  $.ajax({
    url: "/api/weather/",
    success: function(weather)
    {
      $("div#weather .temp span").text(weather.info.temp);

      $("div#weather .temp-high-low span.low").text(weather.forecast.today.min);
      $("div#weather .temp-high-low span.high").text(weather.forecast.today.max);

      $("div#weather .desc span").text(weather.forecast.today.forecast);

      console.log(weather);
    }
  });
}
