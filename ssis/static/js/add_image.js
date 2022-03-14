const addImageInp = document.getElementById("add-image-inp")
const updateImageInp = document.getElementById("update-image-inp")

const addImage = () => addImageInp.click()
const updateImage = () => updateImageInp.click()

addImageInp.addEventListener("change", function(){
    const img = document.getElementById('add-selected-image')
    const file = this.files[0]
    if(file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
            addImageInp.value = reader.result
        }
        reader.readAsDataURL(file)
    }
});

updateImageInp.addEventListener("change", function(){
    console.log('here');
    let img = document.getElementById('displayed-image')
    let file = this.files[0]
    if(file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
            updateImageInp.value = reader.result
        }
        reader.readAsDataURL(file)
    }
});