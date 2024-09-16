function showContent(contentId) {
    var contentElements = document.getElementsByClassName('content');
    for (var i = 0; i < contentElements.length; i++) {
        contentElements[i].style.display = 'none';
    }
    document.getElementById(contentId + 'Content').style.display = 'block';
}
function loadContent(pageUrl, targetId) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById(targetId).innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", pageUrl, true);
    xhttp.send();
}
