var defaultBtn = document.getElementById("default-btn");

function defaultBtnActive(){
    defaultBtn.click();
}
defaultBtn.addEventListener("change", function(){
    var img = document.getElementById('selected-image');
    var file = this.files[0];
    if(file){
        var reader = new FileReader();
        reader.onload = function(){
            img.src = reader.result;
            document.getElementsByName("selected-image").value = reader.result;
        }
        reader.readAsDataURL(file);
    }
});


function afg(){
    var abtn = document.getElementById("a-btn")
    abtn.click();
}
document.getElementById("a-btn").addEventListener("change", function(){
    var img = document.getElementById('displayed-image');
    var inp = document.getElementsByName("selected-image")
    var file = this.files[0];
    if(file){
        var reader = new FileReader();
        reader.onload = function(){
            img.src = reader.result;
            inp.value = reader.result;
        }
        reader.readAsDataURL(file);
    }
});