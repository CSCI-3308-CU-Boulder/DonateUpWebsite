
chrome.runtime.onMessage.addListener(function(request){
  alert(request)
})
function update(){
  var x= document.getElementById("yesNoPick").value;
if (x=="yes"){
  document.getElementById("mainForm").style.display='block';
  document.getElementById("nameDiv").style.display='block';
  document.getElementById("infoP").style.display='block';
  
}


else{
  document.getElementById("nameDiv").style.display='none';
  document.getElementById("infoP").style.display='block';
  document.getElementById("submitButton").style.display='block';
}
}
function pickCharityButton(){
  var charID = document.getElementById("selSite");
  var charName = charID.options[charID.selectedIndex].text;
  var selChar= document.getElementById("selSite").value;
if(selChar!="none"){
  document.getElementById("pickCharityTxt").innerHTML="Congradulations you just Donated to "+charName+"!";
  document.getElementById("pickCharityTxt").style.fontSize="20px";
  document.getElementById("pickCharityTxt").style.color="rgb(12, 70, 131)";
  document.getElementById("pickCharityTxt").style.textAlign="center";
  document.getElementById("selSite").style.display='none';
  document.getElementById("donate_b").style.display='none';

}
else{
  document.getElementById("pickCharityTxt").innerHTML='You must pick a Charity';
}
}

document.addEventListener('DOMContentLoaded',function(){
  document.querySelector('select').addEventListener('change',update)

});

document.addEventListener('DOMContentLoaded',function(){
document.getElementById("donate_b").addEventListener('click',pickCharityButton)
});


