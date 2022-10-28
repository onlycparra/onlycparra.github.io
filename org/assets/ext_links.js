function make_leetcode_external(val, i, arr) {
    if(arr[i].href.search(/leetcode\.com/) >= 0){
        arr[i].setAttribute("target", "_blank");
        arr[i].setAttribute("rel", "noopener noreferrer");
    }
}

links = document.querySelectorAll("a")
links.forEach(make_leetcode_external);
