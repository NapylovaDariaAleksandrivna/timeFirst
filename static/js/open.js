
function show() {
    document.getElementById("mySidebar").style.width = "230px";
    document.getElementById("content").style.display = "none";
    alert("show");
}

function hide() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("content").style.display = "block";
    alert("hide");
}