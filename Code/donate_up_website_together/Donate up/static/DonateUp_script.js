function buttonOver(x){
    x.classList.remove('btn-secondary');
    x.classList.add('btn-primary');
    x.style.color="#FFEDAD";
  }
  
  // function for onmouse out over button
  function normalButton(x){
    x.classList.remove('btn-primary');
    x.classList.add('btn-secondary');
    x.style.color="black";
  }
  // Toggle between showing and hiding the sidebar when clicking the menu icon
  var mySidebar = document.getElementById("mySidebar");
  
  function w3_open() {
    if (mySidebar.style.display === 'block') {
      mySidebar.style.display = 'none';
    } else {
      mySidebar.style.display = 'block';
    }
  }
  
  // Close the sidebar with the close button
  function w3_close() {
      mySidebar.style.display = "none";
  }
  
  /*toggle between hiding and showing the dropdown content */
  function sign_up_button() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  
    function costCalc(){
        document.getElementById("cost").value = 0;
    }

    //-------------------------------------animated modal-------------------------------------------------

function openModal(){
  let modal= document.querySelector('#modal-window');
  modal.classList.add("showModal");
  
}

function closeM(){

    let m= document.querySelector('#modal-window');
  m.classList.remove("showModal");
  
}