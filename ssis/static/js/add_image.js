const addImageInp = document.getElementById("add-image-inp")
let updateImageInp = document.getElementById("update-image-inp")
let studentID = ""

const addImage = () => addImageInp.click()
let updateImage = (studID) => {
    studentID = studID
    updateImageInp = document.getElementById("update-image-inp"+studentID)
    updateImageInp.click()
}

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

function updateDisplay(){
    let img = document.getElementById('displayed-image'+studentID)
    let file = updateImageInp.files[0]
    if (file){
        let reader = new FileReader()
        reader.onload = function(){
            img.src = reader.result
        }
        reader.readAsDataURL(file)
    }
}