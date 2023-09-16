var buttonColors = ["red", "green", "blue", "yellow"];

var gamePattern = [];

var userClickedPattern = [];

var startGame = false;

var level = 0;

$(document).keydown(function (event) {
  if (!startGame && (event.key === "A" || event.key === "a")) {
    startGame = true;
    nextSequence();
    $("h1").text("level " + level);
  }
});

function nextSequence() {
  userClickedPattern = [];
  var randomNumber = Math.floor(Math.random() * 4);
  var randomChosenColour = buttonColors[randomNumber];
  gamePattern.push(randomChosenColour);
  animatePress(randomChosenColour);
  playSound(randomChosenColour);
  level++;
  $("h1").text("level " + level);
}

$(".btn").click(function () {
  var userChosenColour = $(this).attr("id");
  userClickedPattern.push(userChosenColour);
  animatePress(userChosenColour);
  playSound(userChosenColour);
  var index = userClickedPattern.length - 1;
  checkAnswer(index);
});

function playSound(name) {
  var audio = new Audio("sounds/" + name + ".mp3");
  audio.play();
}

function animatePress(name) {
  var button = $("#" + name);
  button.addClass("pressed");
  setTimeout(function () {
    button.removeClass("pressed");
  }, 100);
}

function checkAnswer(index) {
  if (gamePattern[index] !== userClickedPattern[index]) {
    playSound("wrong");
    $("body").addClass("game-over");
    setTimeout(function() {
        $("body").removeClass("game-over");
      }, 200);  
      $("h1").text("Game Over, Press A to Restart");
      startOver();
  } else {
    if (index === level - 1) {
        setTimeout(function() {
            nextSequence();
          }, 1000);      
      }
  }
}

function startOver() {
    startGame = false;
    level = 0;
    gamePattern = [];
    userClickedPattern = [];
}

