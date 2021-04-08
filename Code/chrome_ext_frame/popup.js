// docuent.addEventListener('DOMContentLoaded',function(){
//   document.querySelector('button').addEventListener('click',onclick,false)

//   function onclick () {
//     chrome.tabs.query({currentWindow: true, active: true},
//     fuction(tabs) {
//       chrome.tabs.sendMessage(tabs[0].id, 'hi')
//     })
//   }
// },false)

//function to link nav bar to home page website
document.addEventListener('DOMContentLoaded', function () {
  var links = document.getElementsByTagName("a");
  for (var i = 0; i < links.length; i++) {
      (function () {
          var ln = links[i];
          var location = ln.href;
          ln.onclick = function () {
              chrome.tabs.create({active: true, url: location});
          };
      })();
  }
});

//function to link the paypal button to 
document.addEventListener('DOMContentLoaded', function () {
  var links = document.getElementsByTagName("form");
  for (var i = 0; i < links.length; i++) {
      (function () {
          var ln = links[i];
          var location = "https://www.paypal.com/donate?token=KXeAv_tPqxWHXJLecDPFIgAA2u2mfMVlN9NMTxPF8PiaNXC-TU9wjbkpO5Or5blDKBD6ZD8uAnsdqIt4";
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
    document.getElementById("paypal_div").style.display="initial";
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

// possible tags for tabs. query:::: currentWindow: false,


//trying to pass variable url to python funciton. copied from stacks
// function pass_values() {
//   var pass_to_python = url_var

//                $.ajax(
//                {
//                    type:'POST',
//                    contentType:'application/json;charset-utf-08',
//                    dataType:'json',
//                    url:'http://127.0.0.1:5000/pass_val?value='+pass_to_python ,
//                    success:function (data) {
//                        var reply=data.reply;
//                        if (reply=="success")
//                        {
//                            return;
//                        }
//                        else
//                            {
//                            alert("some error ocured in session agent")
//                            }

//                    }
//                }
//            );
// }




