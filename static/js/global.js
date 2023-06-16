const flash = document.querySelector(".flash")

function hideFlash(){
    flash.classList.add("end-flash")
    setTimeout(()=>{
        flash.classList.add("hidden")
    },200)
}

if(flash){
    flash.addEventListener("click", e=>{
        hideFlash()
    })

    setTimeout(()=>{
        hideFlash()
    },5000)
}

const clickToDisplay = document.querySelectorAll(".click-to-display")
const displays = document.querySelectorAll(".display")

function hideDisplay(display){
    display.classList.add("hide")
    setTimeout(()=>{
        display.classList.add("hidden")
    },200)
}

function showDisplay(display){
    display.classList.remove("hidden")
    setTimeout(()=>{
        display.classList.remove("hide")
    },1)
}


clickToDisplay.forEach(clickable => {
    clickable.addEventListener("click", e=>{
        const id = e.target.dataset.id
        displays.forEach(display => {
            const displayId = display.dataset.id
            if(displayId == id){
                if(display.classList.contains("hidden")){
                    showDisplay(display)
                }
                else{hideDisplay(display)}
            }
        })
    })
})

const modals = document.querySelectorAll(".modal")
const modalBackgrounds = document.querySelectorAll(".modal-bg")
const modalButton = document.querySelectorAll(".modal-button")
const closeModal = document.querySelectorAll(".close-modal")

modalButton.forEach(elem => {
    elem.addEventListener("click", e=>{
        const modalType = e.target.dataset.modal
        modalBackgrounds.forEach(modal => {
            if(modal.dataset.id == modalType){
                modal.classList.remove("hidden")
            }
            else{
                modal.classList.add("hidden")
            }
        })

    })
});

closeModal.forEach(close => {
    close.addEventListener("click",e=>{
        modalBackgrounds.forEach(modal => {
            modal.classList.add("hidden")
        })
    })
});
