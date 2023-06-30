const tab_buttons = document.querySelectorAll(".tab-button")
const tabs = document.querySelectorAll(".tab")
const last_tab = document.querySelector(".last-tab")

tab_buttons.forEach(tab_button => {
    tab_button.addEventListener("click", e=> {
        const desired_tab = e.target.dataset.tab
        tabs.forEach(tab=>{
            tab.classList.add("hidden")
            if(tab.dataset.tab == desired_tab){
                last_tab.value = desired_tab
                tab.classList.remove("hidden")
            }
        })
    })
})

function forceTab(){
    tabs.forEach(tab=>{
        if(tab.dataset.tab == last_tab.value){
            tab.classList.remove("hidden")
        }
    })
}

window.onload = forceTab()

const modal_buttons = document.querySelectorAll(".modal-button")
const hidden_input_item = document.querySelector(".add-to-category-item")
const hidden_input_spell = document.querySelector(".add-to-category-spell")

modal_buttons.forEach(button => {
    button.addEventListener("click", e=> {
        if(e.target.dataset.modal == "add-item"){
            hidden_input_item.value = e.target.dataset.category
        }
        else if(e.target.dataset.modal == "add-spell"){
            hidden_input_spell.value = e.target.dataset.category
        }
    })
})