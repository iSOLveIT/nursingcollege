function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    var refresh = setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);
    
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
    
        var output = minutes + " : " + seconds;
        display.textContent = output;
        $("title").html(output + " - Time Left");
    
        if (--timer < 0) {
            timer = duration;
            display.textContent = "Time's Up!";
            clearInterval(refresh);  // exit refresh loop
            localStorage.removeItem("seconds");
            localStorage.removeItem("minutes");
            document.getElementById('quizForm').submit();
            
            // alert("Time's Up!");
        }
      window.localStorage.setItem("seconds",seconds)
      window.localStorage.setItem("minutes",minutes)
    }, 1000);
    }
    
    window.onload = function () {
      sec  = parseInt(window.localStorage.getItem("seconds"))
      min = parseInt(window.localStorage.getItem("minutes"))

      if((parseInt(min*sec)) || (parseInt(min+sec))){
        var Second = (parseInt(min*60)+sec);
      }
      else{
        var Second = Seconds;
      }
      
      display = document.querySelector('#time');
      startTimer(Second, display);
    };




