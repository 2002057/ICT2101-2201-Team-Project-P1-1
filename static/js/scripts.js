window.addEventListener('DOMContentLoaded', event => {
    function checkPanel(){
        if(panel_contains.classList.contains('end'))
        {
              alert("You have won this game!");
              window.location.href = "/";
        }
        else if(panel_contains.classList.contains('white'))
        {
              alert("Wrong path!");
              location.reload();
        }
      }

      function checkForward(){
        if(panel_contains.classList.contains('no-forward'))
        {
           alert("You are out of the border!");
           location.reload();
        }
      }

      function checkBackward(){
        if(panel_contains.classList.contains('no-back'))
        {
           alert("You are out of the border!");
           location.reload();
        }
      }

      function checkRight(){
        if(panel_contains.classList.contains('no-right'))
        {
           alert("You are out of the border!");
           location.reload();
        }
      }

      function checkLeft(){
        if(panel_contains.classList.contains('no-left'))
        {
           alert("You are out of the border!");
           location.reload();
        }
      }

     var forward = document.getElementById("forward");
     var backward = document.getElementById("backward");
     var left = document.getElementById("left");
     var right = document.getElementById("right");

     car_panel = document.querySelector('.start').id
     car_location = document.getElementById(car_panel).children;
     
     forward.onclick = function() {
        document.getElementById(car_location[0].id).style.display = "none";
        panel_contains = document.getElementById(car_panel);
        checkForward();
        car_panel = parseInt(car_panel) + 1;
        car_panel = car_panel.toString();
        //alert(car_panel);
        car_location = document.getElementById(car_panel).children;
        document.getElementById(car_location[0].id).style.display = "inline";
        panel_contains = document.getElementById(car_panel);
        checkPanel();
        // alert(car_location[0].id)
     }

     backward.onclick = function() {
        document.getElementById(car_location[0].id).style.display = "none";
        panel_contains = document.getElementById(car_panel);
        checkBackward();
        car_panel = parseInt(car_panel) - 1;
        car_panel = car_panel.toString();
        car_location = document.getElementById(car_panel).children;
        document.getElementById(car_location[0].id).style.display = "inline";
        panel_contains = document.getElementById(car_panel);
        checkPanel();
     }

     left.onclick = function(){
        document.getElementById(car_location[0].id).style.display = "none";
        panel_contains = document.getElementById(car_panel);
        checkLeft();
        car_panel = parseInt(car_panel) - 6;
        car_panel = car_panel.toString();
        car_location = document.getElementById(car_panel).children;
        document.getElementById(car_location[0].id).style.display = "inline";
        panel_contains = document.getElementById(car_panel);
        checkPanel();
     }

     right.onclick = function(){
        document.getElementById(car_location[0].id).style.display = "none";
        panel_contains = document.getElementById(car_panel);
        checkRight();
        car_panel = parseInt(car_panel) + 6;
        car_panel = car_panel.toString();
        car_location = document.getElementById(car_panel).children;
        document.getElementById(car_location[0].id).style.display = "inline";
        panel_contains = document.getElementById(car_panel);
        checkPanel();
     }
});