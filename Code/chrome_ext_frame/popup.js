

//function to link nav bar to home page website
document.addEventListener('DOMContentLoaded', function () {
    //gets all links from html
  var links = document.getElementsByTagName("a");
  for (var i = 0; i < links.length; i++) {
      (function () {
          //loops through and stores all links in links[]
          var ln = links[i];
          var location = ln.href;
          ln.onclick = function () {
              chrome.tabs.create({active: true, url: location});
          };
      })();
  }
});



//function "yes" button to hide yes no buttons
  // also will display paypal button 
  document.getElementById("yesBtn").addEventListener("click", function(){
    document.getElementById("button_div").style.display="none";
    document.getElementById("charityChoice").style.display="initial";
    document.getElementById("footer").style.left="37%";
    document.getElementById("footer").style.position="fixed";
  });

  //function "no" button hides buttons displays message
  document.getElementById("noBtn").addEventListener("click", function(){
    document.getElementById("button_div").style.display="none";
    document.getElementById("no_selected").style.display="initial";
    document.getElementById("footer").style.left="37%";
    document.getElementById("footer").style.position="fixed";
  });

  // values for flask and chrarity pick buttons

    //waits for click and when charity is clicked it changes the value of paypal button
  document.getElementById("char_1").addEventListener("click",function(){
      //changes value in paypal button
      //////////////uncomment some stuff if clicking button shouldnt immediatley change to next button
    document.getElementById("charity_name").value =document.getElementById("char_1").innerHTML;
    //changes charity button to btn-secondary class
    // document.getElementById("char_1").classList.remove('btn-primary');
    // document.getElementById("char_1").classList.add('btn-secondary');
    // //make sure all other buttons are unselected //// this removes all classes then adds btn-primary
    // document.getElementById("char_2").classList.remove('btn-secondary');
    // document.getElementById("char_2").classList.remove('btn-primary');
    // document.getElementById("char_2").classList.add('btn-primary');
    // document.getElementById("char_3").classList.remove('btn-secondary');
    // document.getElementById("char_3").classList.remove('btn-primary');
    // document.getElementById("char_3").classList.add('btn-primary');
    // console.log(document.getElementById("charity_name").value);

    document.getElementById("charityChoice").style.display="none";
  document.getElementById("amountChoice").style.display="initial";
  });
  //second charity
  document.getElementById("char_2").addEventListener("click",function(){
    //changes value in paypal button
  document.getElementById("charity_name").value =document.getElementById("char_2").innerHTML;
  document.getElementById("charityChoice").style.display="none";
  document.getElementById("amountChoice").style.display="initial";
});
//third charity
document.getElementById("char_3").addEventListener("click",function(){
  //changes value in paypal button
document.getElementById("charity_name").value =document.getElementById("char_3").innerHTML;
//change to next slide
document.getElementById("charityChoice").style.display="none";
  document.getElementById("amountChoice").style.display="initial";
});

//amount button shows paypal button and hides amount choice.
document.getElementById("tencents").addEventListener("click",function(){
  document.getElementById("amountChoice").style.display="none";
  document.getElementById("paypal_div").style.display="initial";
  document.getElementById("cost").value =document.getElementById("tencents").value;
});
document.getElementById("fifcents").addEventListener("click",function(){
  document.getElementById("amountChoice").style.display="none";
  document.getElementById("paypal_div").style.display="initial";
  document.getElementById("cost").value =document.getElementById("fifcents").value;
});
document.getElementById("onecents").addEventListener("click",function(){
  document.getElementById("amountChoice").style.display="none";
  document.getElementById("paypal_div").style.display="initial";
  document.getElementById("cost").value =document.getElementById("onecents").value;
  console.log(document.getElementById("cost").value);
});
document.getElementById("5hun").addEventListener("click",function(){
  document.getElementById("amountChoice").style.display="none";
  document.getElementById("paypal_div").style.display="initial";
  document.getElementById("cost").value =document.getElementById("5hun").value;
  console.log(document.getElementById("cost").value);
});



// Toggle between showing and hiding the sidebar when clicking the menu icon

document.getElementById("mySidebar").addEventListener("click",function w3_open() {
var mySidebar = document.getElementById("mySidebar");

  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
  } else {
    mySidebar.style.display = 'block';
  }
});

// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
}
//calculate cost 
//paypal button
document.getElementById("cost").addEventListener("onLoad", function costCalc(){
  document.getElementById("cost").value = 99;
});






///background practice stuff

// grab url on tab update
// function handleUpdated(tabId, changeInfo, tabInfo) {
//   console.log("Updated tab: " + tabId);
//   console.log("Changed attributes: ");
//   console.log(changeInfo);
//   console.log("New tab Info: ");
//   console.log(tabInfo);
// }
var url_var; 
// chrome.tabs.onUpdated.addListener(handleUpdated);
document.getElementById("yesBtn").addEventListener("click", function(){
  chrome.tabs.query({ active: true, highlighted:true}, function(tabs){
    //console.log(tabs[0].url);
    url_var = tabs[0].url;
    console.log("Updated url: " + tabs[0].url);
    console.log("Updated url: " + tabs[1].url);
    console.log("Updated url: " + tabs[2].url);
    console.log("Updated url: " + tabs[3].url);
  });
 

});


async (event, steps) =>{
const axios = require("axios")
const cheerio = require("cheerio")

async function fetchHTML(url) {
  const { data } = await axios.get(url)
  return cheerio.load(data)
}

const $ = await fetchHTML("https://nike.com/cart")

// Print the full HTML
//console.log(`Site HTML: ${$.html()}\n\n`)

// Print some specific page content
console.log(`First h1 tag: ${$('h1').text()}`)

// Store the full HTML as a property of $event so we can 
// use it in later steps. See
// https://docs.pipedream.com/notebook/dollar-event/#modifying-event
this.html = $.html()
}



