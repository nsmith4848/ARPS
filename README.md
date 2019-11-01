# ARPS
This is an augmented reality-based projection system designed for use with [Jerome Etienne's](https://github.com/jeromeetienne) AR.js framework and the a-frame VR framework.
## What can it do?
This system is designed to project a 2 dimensional image onto a three dimensional environment via the camera on a user's device.  The code listed here should be run on a web server.  Then users will be able to see the sample image in real time.
## Applications of this
We are currently incorporating this software onto a web server hosted by Western Michigan University.  It will be used as a teaching supplement by Professor Dean Johnson of the university's Electrical and Computer Engineering department.  
## How to use
### Running the website
First install an appropriate web hosting service.  Then include home.html ,the A-Frame and AR.js directories, and ARGeoJS.html in your html file directory.  Then put logicGates.png in your image directory.  Finally, get your web-hosting service up and running and you should be able to navigate to the appropriate pages in a web browser.
### Using home.html
This web page utilizes marker based augmented reality to display the appropriate image/s.  The first step in this process is printing the Hiro marker onto a sheet of paper.  Then, simply hover over the Hiro marker with your camera and an image should appear.  
WARNING:  Excessive lighting will occasionally interfere with your camera's ability to read the marker, especially if the device in question is slightly older.
### Using ARGeoJS.html
This web page utilizes Geo-coordinate-based augmented reality.  This means that the device that is using the website will be pinged for a location and then referenced to a location that is hard-coded onto the website.  To use this near where you are, you must find the gps location of the place where you want the image to be displayed.  Once that has been accomplished, you must replace the position on line 19 of the ARGeoJS.html page with your gps coordinate location.  Then, simply open up the web page and enjoy your location-based augmented reality.
WARNING: GPS pinging does not work indoors.  While most mobile devices have mitigated this by predicting location around an accelerometer, the position will likely still be off by a little, especially with older devices.  
## What can still be done?
Currently, we are working on bringing this system to production-level.  Before that, however, we must work out some bugs with asynchronous model updating.  Once these tasks have been accomplished we may work towards an interactive augmented reality experience, particularly with being able to answer questions in a classroom setting using "AR Buttons".  
## How to tinker with this project
If you are interested in building your own project based on this or simply adding to this project, I recommend viewing the documentation associated with each framework, in particular [AR.js here](https://github.com/jeromeetienne/AR.js/blob/master/README.md) and [A-frame here](https://aframe.io/).  Other than these two frameworks the project is basic javascript and component based html.  
