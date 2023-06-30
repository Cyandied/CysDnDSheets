const newSheet = document.querySelector("#new-sheet")
const newSheetName = document.querySelector("#sheet-name")
const loadSheet = document.querySelector("button[value = load-sheet")
const sheetSelector = document.querySelector("select[name = sheets]")
const back = document.querySelector("#back")
const form = document.querySelector("form")
const dmOpts = document.querySelector("#dmOpts")
const gameSelection = document.querySelector("select[name = game-selection]")

gameSelection.addEventListener("change",e=>{
    sheetSelector.querySelectorAll("option").forEach(option =>{
        if (option.dataset.game != gameSelection.value && gameSelection.value != "all"){
            option.classList.add("hidden")
        }
        else {option.classList.remove("hidden")}

        if (!option.value){
            option.selected = "selected"
        }
    })
})

newSheet.addEventListener("click", e=> {
    newSheet.innerHTML = "Continue";
    newSheet.classList.add("continue")

    newSheetName.classList.remove("hidden")
    loadSheet.classList.add("hidden")
    dmOpts.classList.add("hidden")
    sheetSelector.classList.add("hidden")
    back.classList.remove("hidden")

    document.querySelector("button.continue").addEventListener("click" ,_e => {
        if(newSheetName.value !== ""){
            form.requestSubmit()
        }
    })
})

back.addEventListener("click", e=> {
    newSheet.innerHTML = "New sheet";
    newSheet.classList.remove("continue")

    newSheetName.classList.add("hidden")
    newSheetName.value = ""
    loadSheet.classList.remove("hidden")
    dmOpts.classList.remove("hidden")
    sheetSelector.classList.remove("hidden")
    back.classList.add("hidden")
})

const gameIds = document.querySelectorAll(".game-id")

gameIds.forEach(gameId => {
    gameId.addEventListener("click", e=>{
        const parent = e.target.closest("div")
        const copytext = parent.querySelector(".id").innerHTML
        const button = parent.querySelector("button")
        const buttonText = "copy id"
        button.innerHTML = "id copied!"
        setTimeout(()=>{
            button.innerHTML = buttonText
        }, 2000)

        // Copy the text inside the text field
        navigator.clipboard.writeText(copytext)
    })
});