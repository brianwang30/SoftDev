//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
    }
    else {
        mode = "rect"
    }
}


var modeBut = document.getElementById("buttonToggle");
modeBut.addEventListener('click', toggleMode);

var drawRect = function(e) {
    var mouseX = e.clientX //gets X-coor of mouse when event is fired
    var mouseY = e.clientY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillRect(mouseX, mouseY, 10, 10)
}

var drawCircle = function(e) {
    var mouseX = e.clientX //gets X-coor of mouse when event is fired
    var mouseY = e.clientY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 10, 0, 2 * Math.PI);
    ctx.stroke();
}

//var draw = function(e){
var draw = (e) => {

    if (mode == "rect"){
        console.log("square")
        drawRect(e)
    }
    else{
        console.log("circle")
        drawCircle(e)
    }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {    
    console.log("reset")
    ctx.reset();
}

var clearBut = document.getElementById("buttonClear");
clearBut.addEventListener("click", wipeCanvas);

c.addEventListener("click", draw) //passes the mouse event as parameter for the function
