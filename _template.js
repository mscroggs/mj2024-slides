var nslides = {nslides}
var cSlide = 0

document.addEventListener('keydown', function(event){
    const currentCode = event.which || event.code;
    var currentKey = event.key;
    if (!currentKey) {
        currentKey = String.fromCharCode(currentCode);
    }
    const keyName = "" + currentKey
    process_key(keyName)
});

function process_key(keyName){
    document.getElementById("slide"+cSlide).style.display = "none"
    if((keyName == "ArrowRight" || keyName == "PageDown") && cSlide + 1 < nslides){
        cSlide++
    }
    if((keyName == "ArrowLeft" || keyName == "PageUp") && cSlide > 0){
        cSlide--
    }
    document.getElementById("slide"+cSlide).style.display = "block"
}
