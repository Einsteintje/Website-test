var activePage = 'Home'
function show(shown) {
    if (shown != activePage) {
        document.getElementById(shown).style.display = 'block';
        document.getElementById(activePage).style.display = 'none';
        activePage = shown;
    }
}