
function get_target_date() {
    var t = document.getElementById('timer').getAttribute('data-target').split(/[- :\/]/);
    if(t.length == 6){
        secs = t[5];
    }else{
        secs = 0;
    }
    var target_date = new Date(t[0], t[1]-1, t[2], t[3], t[4], secs);

    // uncomment for testing, so the timer lasts 10 seconds
    // var target_date = new Date();
    // target_date.setSeconds(target_date.getSeconds() + 10);
    return target_date;
}

function populate() {
    document.getElementById("timer").innerHTML=`
  <div class="rotor-group"><div id="days" class="rotor"></div><div>Days</div>
  </div><div class="rotor-group"><div id="hours" class="rotor"></div><div>Hours</div>
  </div><div class="rotor-group"><div id="mins" class="rotor"></div><div>Minutes</div>
  </div><div class="rotor-group"><div id="secs" class="rotor"></div><div>Seconds</div>
  </div>
`;
}

function animate_landing() {
    document.getElementById("plane").classList.add("plane-arrive");
    document.getElementById("city-dest").classList.add("city-arrive");
    var clouds_close = document.querySelectorAll(".cloud.clo");
    for(var i=0; i<clouds_close.length; i++){
        clouds_close[i].classList.remove("clo");
        clouds_close[i].classList.add("mid");
    }
}

function update_count() {
    // Get today's date and time
    var now = new Date().getTime();
    // Find the distance between now and the count down date
    var distance = target_date - now;
    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    // Output the result in an element with id="demo"
    document.getElementById("days").innerHTML = days
    document.getElementById("hours").innerHTML = hours
    document.getElementById("mins").innerHTML = minutes
    document.getElementById("secs").innerHTML = seconds
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("timer").classList.add("count_expired");
        document.getElementById("timer").innerHTML = "Dito is here!";
        animate_landing();
    }
}

var target_date = get_target_date();
populate();
update_count();
var x = setInterval(update_count, 1000);
