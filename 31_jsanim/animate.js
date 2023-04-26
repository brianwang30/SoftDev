/*
Bread Wang, Sadi Nirloy 
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

var requestID;

var clear = (e) =>{
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;
var smaller = Math.min(c.width, c.height);

var drawDot = () => {
    clear();
    ctx.beginPath(); // A path is needed in order to isolate steps in coloring
    ctx.fillStyle = "black"; //circle color
    ctx.strokeStyle = "black"; // outline color
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();
    if (growing ){
        radius += 5;
    }else{
        radius -= 5;
    }

    if ( radius > smaller / 2 && growing){
        growing = false;
    }

    if (radius <= 0 && !growing){
        growing = true;
    }
    requestID = window.requestAnimationFrame(drawDot);
    dotButton.removeEventListener("click", drawDot); // I used this method to take away the power of the button to add layers of animation.
    // I need to do this since this method needs to requestAnimationFrame itself at all times it is running, so I could not limit its access to that step.
}

var stopIt = () =>{
    window.cancelAnimationFrame(requestID);
    dotButton.addEventListener("click", drawDot);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);