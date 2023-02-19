# Look Up The Sky

Use Python to receive an email notification whenever a satellite is visibile in the sky. :satellite::snake:

The script allows you to receive an email notification whenever the ISS satellite is nearby you after sunset hour.

The data of the satellite position are retrieved [here](http://api.open-notify.org/iss-now.json), while the sunset hour will be retrieved [here](https://sunrise-sunset.org/api) according to the latitude and longitude specified in the paramters.

Specify the necessary attributes in parameters.json. :pencil:

Schedule a crontab to run the script every minute. :calendar:

Enjoy the view! :telescope:
