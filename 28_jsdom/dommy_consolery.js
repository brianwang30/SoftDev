/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //puts out AYO into console on web browser

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//running f(20) in the console will give you 50. this is bc 20+30=50

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
//if u type in o into the console, all of these elements willbe printed out like a dictionary.
//how to call the func x?

var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
//when u call addItem("text"), the function will append a list item.
//Therefore, running addItem("item 8") would result in the list having an eighth element. 8. item 8


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
// when calling just removeItem(8), you will get undefined as an output
// to solve that issue, set a var to the value of the element index you want to remove from the list and then run removeItem(8)

var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};
//adds red to the class list of each li element in the list
//if class list solely red, turns that element red

var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
//will have strips of red and blue text. each li item alternates between red and blue colors. if even, then red.

//insert your implementations here for...
// FIB
var fib = function(n) {
  console.log(n)
  if (n <= 1) {
      return n
  }
  
  var ret = fib(n - 1) + fib(n - 2);
  console.log(ret)
  return ret;
}
// FAC
var fact = function(n) {
  if (n < 2) {
      return 1
  }
  return n * fact(n - 1)
}
// GCD
var gcd = function(a, b) {
  if (!b){
    return a;
  }
  return gcd(b, a%b);
}

var handlefib = function(){
  console.log(fib(10));
}

  var fibbut = document.getElementById("fib");

  fibbut.addEventListener( 'click', handlefib);

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  var retVal = param1 + param2;
  return retVal;
};


