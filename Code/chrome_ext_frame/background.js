

chrome.runtime.onConnect.addListener(function(port){
    // port.postMessage({greeting:"message passed to content from backgrou"});
    chrome.windows.create({
        url: chrome.extension.getURL("templates/popup.html"), 
        type: "popup",
        height: 500,
        width: 350,
        left: 900,
        top: 100,
    });
  });


  

 