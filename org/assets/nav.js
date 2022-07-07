function remove_gohome_in_homepage() {
    if (descr.includes("homepage")) {
        document.querySelector("#nav_list").style.display = "none";
    }
}
function sticky_nav() {
    if (window.pageYOffset >= sticky_threshold) {
        navbar.classList.add("sticky");
        small_title.innerText = document.querySelector(".title").innerText;
    } else {
        navbar.classList.remove("sticky");
        small_title.innerText = "";
    }
}
var navbar = document.getElementById("navbar");
var sticky_threshold = navbar.offsetTop;
var small_title = document.querySelector("#small-title");
var descr = document.head.querySelector("meta[name=description]");

if (descr != null) {
    descr = descr.getAttribute("content").split(", ");
    remove_gohome_in_homepage();
}
window.onscroll = function() {sticky_nav()};
