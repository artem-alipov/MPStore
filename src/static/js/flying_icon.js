var flyingIcon = document.getElementById("flying-icon");

function animateIcon() {
  var angle = 0;
  setInterval(function() {
    angle += 0.1;
    var x = 50 + (Math.sin(angle) * 50);
    var y = 50 + (Math.cos(angle) * 50);
    flyingIcon.style.transform = "translate(" + x + "%, " + y + "%)";
  }, 50);
}

animateIcon();