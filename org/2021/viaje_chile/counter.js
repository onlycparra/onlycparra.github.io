// Set the date we're counting down to
// var t = new Date();
// t.setSeconds(t.getSeconds() + 30);
// var countDownDate = t; // new Date("2021-12-13 00:05").getTime();
var t = document.getElementById('timer').getAttribute('data-target')
var target_date = new Date(t);
//target_date.setSeconds(target_date.getSeconds() + 30);

function populate() {
    document.getElementById("timer").innerHTML=`
  <div class="rotor-group"><div id="days" class="rotor"></div><div>Dias</div>
  </div><div class="rotor-group"><div id="hours" class="rotor"></div><div>Horas</div>
  </div><div class="rotor-group"><div id="mins" class="rotor"></div><div>Minutos</div>
  </div><div class="rotor-group"><div id="secs" class="rotor"></div><div>Segundos</div>
  </div>
`;
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
        document.getElementById("timer").innerHTML = "Ya Llegó!";
    }
}

populate();
update_count();
var x = setInterval(update_count, 1000);
