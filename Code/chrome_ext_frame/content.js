
//messaging practice to popup.js
//This line opens up a long-lived connection to your background page.
setTimeout(function(){ var port = chrome.runtime.connect({name:"mycontentscript"});
port.onMessage.addListener(function(message,sender){
  
    alert(message.greeting);
 
});}, 3000);


//grabs injected popup html to inject into content
// var iFrame  = document.createElement ("iframe");
// iFrame.src  = chrome.extension.getURL ("/templates/injected_popup.htm");

// document.body.after (iFrame, document.body);

