var modal = document.getElementById("myModal");
var btn = document.getElementById("forgot");
var span = document.getElementsByClassName("modal-close")[0];
var okbtn = document.getElementsByClassName("recover-email")[0];

btn.onclick = function(){
  modal.style.display = "block";

}
span.onclick = function(){
  modal.style.display = "none";
  

}
okbtn.onclick = function(){
  modal.style.display = "none";
  

}

window.onclick = function(){
  if (event.target == modal){
      modal.style.display ="none";
  }
}   